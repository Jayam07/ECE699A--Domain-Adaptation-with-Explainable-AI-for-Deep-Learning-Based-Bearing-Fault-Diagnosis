# -*- coding: utf-8 -*-
"""
Supervised Domain Adaptation (Balanced data) + 5-Fold CV
CWRU -> CWRU (10 classes) with:
- Balanced only
- Balanced + MMD
- Balanced + CORAL
- Balanced + MMD + CORAL

Also includes:
- Training history
- Confusion matrices
- t-SNE
- Grad-CAM (last fold only)
- SHAP (last fold only)

Notes:
- Uses 10 classes for CWRU -> CWRU
- Uses segmentation 400,400
- Applies downsampling for 12K normal class as in your professor code
"""

import os
import random
from datetime import datetime

import numpy as np
import pandas as pd
import scipy.io
import shap
import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.signal import resample
from sklearn.manifold import TSNE
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
)
from sklearn.model_selection import StratifiedKFold, train_test_split
from tensorflow.keras import layers, models


# =========================================================
# 0) CONFIG
# =========================================================
SEED = 42
random.seed(SEED)
np.random.seed(SEED)
tf.random.set_seed(SEED)
os.environ["PYTHONHASHSEED"] = str(SEED)

# ---------- DATASET PAIR ----------
SOURCE_NAME = "12K1HP"
TARGET_NAME = "12K2HP"

# ---------- DOMAIN ADAPTATION ----------
USE_MMD = True
USE_CORAL = False
MMD_WEIGHT = 0.1
CORAL_WEIGHT = 0.0

# ---------- TRAINING ----------
PRETRAIN_EPOCHS = 100
PATIENCE = 15
BATCH_SIZE = 64
KFOLD = 5

# ---------- SEGMENTATION ----------
INTERVAL = 400
SAMPLES_PER_BLOCK = 400

# ---------- XAI ----------
RUN_XAI_ONLY_LAST_FOLD = True
N_PER_CLASS_XAI = 3
SHAP_BG_SIZE = 50

# ---------- PATH ----------
BASE_SAVE_ROOT = "/content/drive/MyDrive/SDA_CWRU_CWRU_RESULTS"

VERBOSE = 1


# =========================================================
# 1) DATASET PATHS
# =========================================================
DATASETS = {
    "12K0HP": ("/content/drive/MyDrive/BearingData_CaseWestern_12K1797",
               ['97.mat', '105.mat', '118.mat', '130.mat', '169.mat',
                '185.mat', '197.mat', '209.mat', '222.mat', '234.mat']),

    "12K1HP": ("/content/drive/MyDrive/BearingData_CaseWestern_12K1772",
               ['98.mat', '106.mat', '119.mat', '131.mat', '170.mat',
                '186.mat', '198.mat', '210.mat', '223.mat', '235.mat']),

    "12K2HP": ("/content/drive/MyDrive/BearingData_CaseWestern_12K1750",
               ['99.mat', '107.mat', '120.mat', '132.mat', '171.mat',
                '187.mat', '199.mat', '211.mat', '224.mat', '236.mat']),

    "12K3HP": ("/content/drive/MyDrive/BearingData_CaseWestern_12K1730",
               ['100.mat', '108.mat', '121.mat', '133.mat', '172.mat',
                '188.mat', '200.mat', '212.mat', '225.mat', '237.mat']),

    "48K1HP": ("/content/drive/MyDrive/BearingData_CaseWestern_48K1772",
               ['98.mat', '110.mat', '123.mat', '136.mat', '175.mat',
                '190.mat', '202.mat', '214.mat', '227.mat', '239.mat']),

    "48K2HP": ("/content/drive/MyDrive/BearingData_CaseWestern_48K1750",
               ['99.mat', '111.mat', '124.mat', '137.mat', '176.mat',
                '191.mat', '203.mat', '215.mat', '228.mat', '240.mat']),

    "48K3HP": ("/content/drive/MyDrive/BearingData_CaseWestern_48K1730",
               ['100.mat', '112.mat', '125.mat', '138.mat', '177.mat',
                '192.mat', '204.mat', '217.mat', '229.mat', '241.mat'])
}


# =========================================================
# 2) DATA LOADING
# =========================================================
def load_signals(folder_path, files_with_labels):
    signals, labels = [], []

    for fname, lbl in files_with_labels:
        fpath = os.path.join(folder_path, fname)
        mat = scipy.io.loadmat(fpath)

        file_num = os.path.splitext(fname)[0]
        de_keys = [k for k in mat.keys() if 'DE_time' in k]
        match_keys = [k for k in de_keys if file_num in k]

        if match_keys:
            key = match_keys[0]
        elif de_keys:
            key = de_keys[0]
            print(f"[Warning] Using first DE_time key for {fname}: {key}")
        else:
            print(f"[Warning] No DE_time signal found in {fname}")
            continue

        sig = np.array(mat[key]).flatten()
        signals.append(sig)
        labels.append(lbl)

    return signals, labels


def load_source_data():
    folder, files = DATASETS[SOURCE_NAME]
    file_label_pairs = [(f, i) for i, f in enumerate(files)]
    return load_signals(folder, file_label_pairs)


def load_target_data():
    folder, files = DATASETS[TARGET_NAME]
    file_label_pairs = [(f, i) for i, f in enumerate(files)]
    return load_signals(folder, file_label_pairs)


# =========================================================
# 3) PREPROCESSING
# =========================================================
def downsample_raw_signals(signals, labels, factor=4):
    """
    Keep only 1 in every 4 signals for class 0, keep all others.
    This follows your professor's code logic.
    """
    signals = np.array(signals, dtype=object)
    labels = np.array(labels)

    keep_idx = []
    for cls in np.unique(labels):
        idx = np.where(labels == cls)[0]
        if cls == 0:
            keep_idx.extend(idx[::factor])
        else:
            keep_idx.extend(idx)

    keep_idx = np.array(keep_idx)
    return list(signals[keep_idx]), list(labels[keep_idx])


def resample_to_12K(signals, labels, orig_rate=48000, target_rate=12000):
    factor = orig_rate // target_rate
    new_signals = []
    for sig in signals:
        n_samples = len(sig) // factor
        sig_resampled = resample(sig, n_samples)
        new_signals.append(sig_resampled)
    return new_signals, labels


def sampling(data, interval_length, samples_per_block, ignore_points=0):
    adjusted_length = len(data) - 2 * ignore_points
    no_of_blocks = (
        round(adjusted_length / interval_length)
        - round(samples_per_block / interval_length)
        - 1
    )

    if no_of_blocks <= 0:
        return np.zeros((0, samples_per_block))

    split_data = np.zeros((no_of_blocks, samples_per_block))
    for i in range(no_of_blocks):
        start_idx = ignore_points + i * interval_length
        split_data[i, :] = data[start_idx:start_idx + samples_per_block].T

    return split_data


def segment_signals(signals, labels, interval_length=INTERVAL, samples_per_block=SAMPLES_PER_BLOCK, ignore_points=0):
    X, y = [], []

    for sig, lbl in zip(signals, labels):
        segments = sampling(sig, interval_length, samples_per_block, ignore_points)
        if segments.shape[0] == 0:
            continue
        X.append(segments)
        y.extend([lbl] * len(segments))

    if len(X) == 0:
        return np.zeros((0, samples_per_block, 1)), np.array([])

    X = np.vstack(X)[..., np.newaxis]
    y = np.array(y)
    return X, y


def balance_after_segmentation(X, y, per_class=None, seed=SEED):
    rng = np.random.RandomState(seed)
    classes = np.unique(y)
    counts = {c: np.sum(y == c) for c in classes}

    if per_class is None:
        per_class = int(min(counts.values()))

    X_parts, y_parts = [], []
    for c in classes:
        idx = np.where(y == c)[0]
        if len(idx) <= per_class:
            chosen = idx
        else:
            chosen = rng.choice(idx, size=per_class, replace=False)

        X_parts.append(X[chosen])
        y_parts.append(y[chosen])

    X_new = np.vstack(X_parts)
    y_new = np.concatenate(y_parts)
    perm = rng.permutation(len(y_new))
    return X_new[perm], y_new[perm]


# =========================================================
# 4) PLOTTING HELPERS
# =========================================================
def plot_confusion_matrix(y_true, y_pred, title, save_path):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title(title)
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()


def plot_tsne(source_feats, target_feats, save_path, perplexity=30, lr=200):
    X = np.concatenate([source_feats, target_feats], axis=0)
    domain_labels = np.array([0] * len(source_feats) + [1] * len(target_feats))

    tsne = TSNE(
        n_components=2,
        perplexity=perplexity,
        learning_rate=lr,
        random_state=SEED
    )
    X_tsne = tsne.fit_transform(X)

    plt.figure(figsize=(8, 6))
    plt.scatter(X_tsne[domain_labels == 0, 0], X_tsne[domain_labels == 0, 1],
                s=8, label='Source', alpha=0.6)
    plt.scatter(X_tsne[domain_labels == 1, 0], X_tsne[domain_labels == 1, 1],
                s=8, label='Target', alpha=0.6)
    plt.legend()
    plt.title("t-SNE Feature Distribution (Source vs Target)")
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()


def plot_training_history(history_log, folder_dir, fold_num):
    if len(history_log) == 0:
        return

    hist_df = pd.DataFrame(history_log)
    csv_path = os.path.join(folder_dir, f"Fold{fold_num}_Training_History.csv")
    hist_df.to_csv(csv_path, index=False)

    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.plot(hist_df['epoch'], hist_df['train_loss'], label='Train Loss')
    plt.plot(hist_df['epoch'], hist_df['val_loss'], label='Val Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title(f'Fold {fold_num} - Loss vs Epoch')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(hist_df['epoch'], hist_df['val_acc'], label='Val Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.title(f'Fold {fold_num} - Val Accuracy vs Epoch')
    plt.legend()

    plt.tight_layout()
    plt.savefig(os.path.join(folder_dir, f"Fold{fold_num}_Training_History.png"), dpi=300)
    plt.close()


# =========================================================
# 5) MODEL + LOSSES
# =========================================================
def build_cnn(input_shape=(INTERVAL, 1), num_classes=10):
    model = models.Sequential([
        layers.Input(shape=input_shape),

        layers.Conv1D(16, 3, activation='relu', padding='same', name="conv1"),
        layers.BatchNormalization(),
        layers.MaxPooling1D(2),

        layers.Conv1D(32, 3, activation='relu', padding='same', name="conv2"),
        layers.BatchNormalization(),
        layers.MaxPooling1D(2),

        layers.Conv1D(64, 3, activation='relu', padding='same', name="conv3"),
        layers.BatchNormalization(),
        layers.GlobalAveragePooling1D(),

        layers.Dense(128, activation='relu', name='feature_layer'),
        layers.Dense(num_classes, activation='softmax')
    ])
    return model


def mmd_loss(source_features, target_features):
    x_mean = tf.reduce_mean(source_features, axis=0)
    y_mean = tf.reduce_mean(target_features, axis=0)
    return tf.reduce_mean(tf.square(x_mean - y_mean))


def coral_loss(source_features, target_features):
    def covariance(x):
        n = tf.cast(tf.shape(x)[0], tf.float32)
        xm = x - tf.reduce_mean(x, axis=0, keepdims=True)
        cov = tf.matmul(tf.transpose(xm), xm) / (n - 1.0 + 1e-8)
        return cov

    cs = covariance(source_features)
    ct = covariance(target_features)
    d = tf.cast(tf.shape(cs)[0], tf.float32)
    loss = tf.reduce_sum(tf.square(cs - ct)) / (4.0 * d * d)
    return loss


# =========================================================
# 6) GRAD-CAM
# =========================================================
def get_last_conv1d_layer_name(model):
    for layer in reversed(model.layers):
        if isinstance(layer, tf.keras.layers.Conv1D):
            return layer.name
    raise ValueError("No Conv1D layer found in model.")


def compute_gradcam_1d(model, sample, class_index=None, last_conv_layer_name=None):
    grad_model = tf.keras.models.Model(
        inputs=model.inputs,
        outputs=[
            model.get_layer(last_conv_layer_name).output,
            model.outputs[0]
        ]
    )

    with tf.GradientTape() as tape:
        conv_outputs, predictions = grad_model(sample, training=False)

        if class_index is None:
            class_index = tf.argmax(predictions[0])

        class_score = predictions[:, class_index]

    grads = tape.gradient(class_score, conv_outputs)
    pooled_grads = tf.reduce_mean(grads, axis=1)

    conv_outputs = conv_outputs[0]
    pooled_grads = pooled_grads[0]

    cam = tf.reduce_sum(conv_outputs * pooled_grads, axis=-1)
    cam = tf.nn.relu(cam)

    cam = cam.numpy()
    if np.max(cam) > 0:
        cam = cam / np.max(cam)

    return cam


def resize_cam_to_signal(cam, signal_length):
    x_old = np.linspace(0, 1, len(cam))
    x_new = np.linspace(0, 1, signal_length)
    return np.interp(x_new, x_old, cam)


def save_gradcam_plot_1d(signal_1d, cam_1d, true_label, pred_label, save_path, title):
    if signal_1d.ndim > 1:
        signal_1d = signal_1d[:, 0]

    x = np.arange(len(signal_1d))

    fig, axes = plt.subplots(3, 1, figsize=(12, 8), sharex=True)

    axes[0].plot(x, signal_1d, linewidth=1)
    axes[0].set_title(f"{title}\nTrue={true_label}, Pred={pred_label}")
    axes[0].set_ylabel("Amplitude")
    axes[0].grid(True, alpha=0.3)

    im = axes[1].imshow(
        cam_1d.reshape(1, -1),
        aspect='auto',
        cmap='jet',
        extent=[0, len(signal_1d), 0, 1]
    )
    axes[1].set_title("Grad-CAM Importance")
    axes[1].set_yticks([])
    plt.colorbar(im, ax=axes[1], fraction=0.02, pad=0.02)

    ymin, ymax = signal_1d.min(), signal_1d.max()
    axes[2].plot(x, signal_1d, color='black', linewidth=1)
    axes[2].imshow(
        cam_1d.reshape(1, -1),
        aspect='auto',
        cmap='jet',
        alpha=0.35,
        extent=[0, len(signal_1d), ymin, ymax]
    )
    axes[2].set_title("Signal + Grad-CAM Overlay")
    axes[2].set_xlabel("Time Index")
    axes[2].set_ylabel("Amplitude")
    axes[2].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()


def generate_gradcam_examples(model, X_data, y_data, domain_name, save_root, n_per_class=3):
    os.makedirs(save_root, exist_ok=True)

    pred_probs = model.predict(X_data, verbose=0)
    y_pred = np.argmax(pred_probs, axis=1)
    y_true = y_data.reshape(-1)

    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(f"Confusion Matrix - {domain_name}")
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.tight_layout()
    plt.savefig(os.path.join(save_root, f"confusion_matrix_{domain_name}.png"), dpi=300)
    plt.close()

    last_conv_layer_name = get_last_conv1d_layer_name(model)
    classes = np.unique(y_true)

    for cls in classes:
        cls = int(cls)

        cls_correct_idx = np.where((y_true == cls) & (y_pred == cls))[0][:n_per_class]
        cls_wrong_idx = np.where((y_true == cls) & (y_pred != cls))[0][:n_per_class]

        correct_dir = os.path.join(save_root, f"class_{cls}", "correct")
        wrong_dir = os.path.join(save_root, f"class_{cls}", "misclassified")
        os.makedirs(correct_dir, exist_ok=True)
        os.makedirs(wrong_dir, exist_ok=True)

        for j, idx in enumerate(cls_correct_idx):
            sample = X_data[idx:idx+1]
            signal = sample[0]
            true_label = int(y_true[idx])
            pred_label = int(y_pred[idx])

            cam = compute_gradcam_1d(
                model, sample,
                class_index=pred_label,
                last_conv_layer_name=last_conv_layer_name
            )
            cam = resize_cam_to_signal(cam, signal.shape[0])

            save_path = os.path.join(
                correct_dir,
                f"gradcam_correct_idx{idx}_true{true_label}_pred{pred_label}_{j+1}.png"
            )
            save_gradcam_plot_1d(
                signal, cam, true_label, pred_label, save_path,
                f"{domain_name} | Correct Sample | Class {cls}"
            )

        for j, idx in enumerate(cls_wrong_idx):
            sample = X_data[idx:idx+1]
            signal = sample[0]
            true_label = int(y_true[idx])
            pred_label = int(y_pred[idx])

            cam = compute_gradcam_1d(
                model, sample,
                class_index=pred_label,
                last_conv_layer_name=last_conv_layer_name
            )
            cam = resize_cam_to_signal(cam, signal.shape[0])

            save_path = os.path.join(
                wrong_dir,
                f"gradcam_wrong_idx{idx}_true{true_label}_pred{pred_label}_{j+1}.png"
            )
            save_gradcam_plot_1d(
                signal, cam, true_label, pred_label, save_path,
                f"{domain_name} | Misclassified Sample | True Class {cls}"
            )


# =========================================================
# 7) SHAP
# =========================================================
def get_single_sample_shap_1d(explainer, sample, pred_label):
    shap_values = explainer.shap_values(sample)

    if isinstance(shap_values, list):
        sv = shap_values[pred_label][0, :, 0]
    else:
        sv = np.array(shap_values)
        if sv.ndim == 4 and sv.shape[0] == 1:
            sv = sv[0, :, 0, pred_label]
        elif sv.ndim == 4 and sv.shape[1] == 1:
            sv = sv[pred_label, 0, :, 0]
        elif sv.ndim == 3:
            sv = sv[0, :, 0]
        else:
            sv = sv.reshape(sample.shape[1])

    return sv


def save_shap_signal_plot_1d(signal_1d, shap_1d, true_label, pred_label, save_path, title):
    if signal_1d.ndim > 1:
        signal_1d = signal_1d[:, 0]

    x = np.arange(len(signal_1d))
    max_abs = np.max(np.abs(shap_1d)) + 1e-9

    fig, axes = plt.subplots(3, 1, figsize=(12, 8), sharex=True)

    axes[0].plot(x, signal_1d, linewidth=1)
    axes[0].set_title(f"{title}\nTrue={true_label}, Pred={pred_label}")
    axes[0].set_ylabel("Amplitude")
    axes[0].grid(True, alpha=0.3)

    im = axes[1].imshow(
        shap_1d.reshape(1, -1),
        aspect='auto',
        cmap='coolwarm',
        vmin=-max_abs,
        vmax=max_abs,
        extent=[0, len(signal_1d), 0, 1]
    )
    axes[1].set_title("SHAP Importance")
    axes[1].set_yticks([])
    plt.colorbar(im, ax=axes[1], fraction=0.02, pad=0.02)

    ymin, ymax = signal_1d.min(), signal_1d.max()
    axes[2].plot(x, signal_1d, color='black', linewidth=1, alpha=0.85)
    axes[2].imshow(
        shap_1d.reshape(1, -1),
        aspect='auto',
        cmap='coolwarm',
        alpha=0.35,
        vmin=-max_abs,
        vmax=max_abs,
        extent=[0, len(signal_1d), ymin, ymax]
    )
    axes[2].set_title("Signal + SHAP Overlay")
    axes[2].set_xlabel("Time Index")
    axes[2].set_ylabel("Amplitude")
    axes[2].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()


def generate_shap_examples(model, explainer, X_data, y_data, domain_name, save_root, n_per_class=3):
    os.makedirs(save_root, exist_ok=True)

    pred_probs = model.predict(X_data, verbose=0)
    y_pred = np.argmax(pred_probs, axis=1)
    y_true = y_data.reshape(-1)

    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(f"Confusion Matrix - {domain_name}")
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.tight_layout()
    plt.savefig(os.path.join(save_root, f"confusion_matrix_{domain_name}.png"), dpi=300)
    plt.close()

    classes = np.unique(y_true)

    for cls in classes:
        cls = int(cls)

        cls_correct_idx = np.where((y_true == cls) & (y_pred == cls))[0][:n_per_class]
        cls_wrong_idx = np.where((y_true == cls) & (y_pred != cls))[0][:n_per_class]

        correct_dir = os.path.join(save_root, f"class_{cls}", "correct")
        wrong_dir = os.path.join(save_root, f"class_{cls}", "misclassified")
        os.makedirs(correct_dir, exist_ok=True)
        os.makedirs(wrong_dir, exist_ok=True)

        for j, idx in enumerate(cls_correct_idx):
            sample = X_data[idx:idx+1]
            signal = sample[0]
            true_label = int(y_true[idx])
            pred_label = int(y_pred[idx])

            shap_1d = get_single_sample_shap_1d(explainer, sample, pred_label)

            save_path = os.path.join(
                correct_dir,
                f"shap_correct_idx{idx}_true{true_label}_pred{pred_label}_{j+1}.png"
            )
            save_shap_signal_plot_1d(
                signal, shap_1d, true_label, pred_label, save_path,
                f"{domain_name} | Correct Sample | Class {cls}"
            )

        for j, idx in enumerate(cls_wrong_idx):
            sample = X_data[idx:idx+1]
            signal = sample[0]
            true_label = int(y_true[idx])
            pred_label = int(y_pred[idx])

            shap_1d = get_single_sample_shap_1d(explainer, sample, pred_label)

            save_path = os.path.join(
                wrong_dir,
                f"shap_wrong_idx{idx}_true{true_label}_pred{pred_label}_{j+1}.png"
            )
            save_shap_signal_plot_1d(
                signal, shap_1d, true_label, pred_label, save_path,
                f"{domain_name} | Misclassified Sample | True Class {cls}"
            )


def save_shap_summary(model, explainer, Xt_test, save_path):
    summary_n = min(20, len(Xt_test))
    summary_samples = Xt_test[:summary_n]
    summary_preds = np.argmax(model.predict(summary_samples, verbose=0), axis=1)

    summary_shap = explainer.shap_values(summary_samples)

    summary_maps = []
    for i in range(summary_n):
        pred_cls = summary_preds[i]

        if isinstance(summary_shap, list):
            sv_i = summary_shap[pred_cls][i, :, 0]
        else:
            sv = np.array(summary_shap)
            if sv.ndim == 4 and sv.shape[0] == summary_n:
                sv_i = sv[i, :, 0, pred_cls]
            elif sv.ndim == 4 and sv.shape[0] != summary_n:
                sv_i = sv[pred_cls, i, :, 0]
            elif sv.ndim == 3:
                sv_i = sv[i, :, 0]
            else:
                sv_i = sv[i].reshape(summary_samples.shape[1])

        summary_maps.append(sv_i)

    summary_maps = np.array(summary_maps)
    summary_input = summary_samples[:, :, 0]

    shap.summary_plot(summary_maps, summary_input, show=False)
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()


# =========================================================
# 8) TRAINING + EVALUATION + XAI
# =========================================================
def train_supervised_da_kfold(
    Xs, ys, Xt, yt,
    k_folds=KFOLD,
    pretrain_epochs=PRETRAIN_EPOCHS,
    batch_size=BATCH_SIZE,
    use_mmd=USE_MMD,
    use_coral=USE_CORAL,
    mmd_weight=MMD_WEIGHT,
    coral_weight=CORAL_WEIGHT,
    patience=PATIENCE
):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    exp_name = f"SDA_{SOURCE_NAME}_TO_{TARGET_NAME}"
    base_dir = os.path.join(BASE_SAVE_ROOT, f"{exp_name}_{timestamp}")
    os.makedirs(base_dir, exist_ok=True)

    kfold = StratifiedKFold(n_splits=k_folds, shuffle=True, random_state=SEED)
    results_src = []
    results_tgt = []

    for fold, (train_idx, val_idx) in enumerate(kfold.split(Xs, ys), start=1):
        print(f"\n========== Fold {fold}/{k_folds} ==========")

        Xs_train, Xs_val = Xs[train_idx], Xs[val_idx]
        ys_train, ys_val = ys[train_idx], ys[val_idx]

        Xt_train, Xt_test, yt_train, yt_test = train_test_split(
            Xt, yt, test_size=0.2, random_state=SEED + fold, stratify=yt
        )

        if len(Xs_train) == 0 or len(Xt_train) == 0:
            raise ValueError("Empty train split encountered.")

        model = build_cnn(input_shape=(Xs.shape[1], 1), num_classes=10)
        feature_model = models.Model(
            inputs=model.inputs,
            outputs=model.get_layer('feature_layer').output
        )
        optimizer = tf.keras.optimizers.Adam(1e-4)
        ce_loss = tf.keras.losses.SparseCategoricalCrossentropy()

        best_val = 0.0
        epochs_since_improvement = 0
        fold_dir = os.path.join(base_dir, f"Fold_{fold}")
        os.makedirs(fold_dir, exist_ok=True)
        best_path = os.path.join(fold_dir, "best_model.weights.h5")
        history_log = []

        print(f"Training {pretrain_epochs} epochs | MMD={use_mmd} | CORAL={use_coral}")

        for ep in range(pretrain_epochs):
            train_loss_accum = 0.0
            train_steps = 0

            idx_s = np.random.permutation(len(Xs_train))
            idx_t = np.random.permutation(len(Xt_train))

            Xs_sh, ys_sh = Xs_train[idx_s], ys_train[idx_s]
            Xt_sh, yt_sh = Xt_train[idx_t], yt_train[idx_t]

            num_batches = min(len(Xs_sh), len(Xt_sh)) // batch_size
            if num_batches == 0:
                num_batches = 1

            for b in range(num_batches):
                s_start, s_end = b * batch_size, (b + 1) * batch_size
                t_start, t_end = b * batch_size, (b + 1) * batch_size

                Xs_b, ys_b = Xs_sh[s_start:s_end], ys_sh[s_start:s_end]
                Xt_b, yt_b = Xt_sh[t_start:t_end], yt_sh[t_start:t_end]

                if len(Xs_b) == 0 or len(Xt_b) == 0:
                    continue

                with tf.GradientTape() as tape:
                    logits_s = model(Xs_b, training=True)
                    logits_t = model(Xt_b, training=True)

                    loss_s = ce_loss(ys_b, logits_s)
                    loss_t = ce_loss(yt_b, logits_t)
                    loss_ce_total = 0.5 * (loss_s + loss_t)

                    align_loss = 0.0
                    if use_mmd:
                        fs = feature_model(Xs_b)
                        ft = feature_model(Xt_b)
                        align_loss += mmd_weight * mmd_loss(fs, ft)

                    if use_coral:
                        fs = feature_model(Xs_b) if not use_mmd else fs
                        ft = feature_model(Xt_b) if not use_mmd else ft
                        align_loss += coral_weight * coral_loss(fs, ft)

                    loss_total = loss_ce_total + align_loss

                grads = tape.gradient(loss_total, model.trainable_variables)
                optimizer.apply_gradients(zip(grads, model.trainable_variables))

                train_loss_accum += float(loss_total.numpy())
                train_steps += 1

            val_logits = model.predict(Xs_val, verbose=0)
            val_preds = np.argmax(val_logits, axis=1)
            val_acc = accuracy_score(ys_val, val_preds)
            val_loss = float(np.mean(
                tf.keras.losses.sparse_categorical_crossentropy(ys_val, val_logits).numpy()
            ))
            avg_train_loss = train_loss_accum / max(1, train_steps)

            if VERBOSE:
                print(f" Epoch {ep+1}/{pretrain_epochs} | TrainLoss={avg_train_loss:.4f} | ValAcc={val_acc:.4f}")

            history_log.append({
                "epoch": ep + 1,
                "train_loss": avg_train_loss,
                "val_loss": val_loss,
                "val_acc": val_acc
            })

            if val_acc > best_val:
                best_val = val_acc
                model.save_weights(best_path)
                epochs_since_improvement = 0
            else:
                epochs_since_improvement += 1

            if epochs_since_improvement >= patience:
                print(f"Early stopping triggered at epoch {ep+1} (no improvement in {patience} epochs)")
                break

        model.load_weights(best_path)
        feature_model = models.Model(
            inputs=model.inputs,
            outputs=model.get_layer('feature_layer').output
        )

        # ---------- TARGET EVAL ----------
        y_pred_t = np.argmax(model.predict(Xt_test, verbose=0), axis=1)
        acc_t = accuracy_score(yt_test, y_pred_t)
        prec_t = precision_score(yt_test, y_pred_t, average="macro", zero_division=0)
        rec_t = recall_score(yt_test, y_pred_t, average="macro", zero_division=0)
        f1_t = f1_score(yt_test, y_pred_t, average="macro", zero_division=0)
        results_tgt.append([acc_t, prec_t, rec_t, f1_t])

        plot_confusion_matrix(
            yt_test, y_pred_t,
            f"Fold {fold} Target ConfMat",
            os.path.join(fold_dir, f"Fold{fold}_Target_ConfMat.png")
        )

        # ---------- SOURCE EVAL ----------
        y_pred_s = np.argmax(model.predict(Xs_val, verbose=0), axis=1)
        acc_s = accuracy_score(ys_val, y_pred_s)
        prec_s = precision_score(ys_val, y_pred_s, average="macro", zero_division=0)
        rec_s = recall_score(ys_val, y_pred_s, average="macro", zero_division=0)
        f1_s = f1_score(ys_val, y_pred_s, average="macro", zero_division=0)
        results_src.append([acc_s, prec_s, rec_s, f1_s])

        plot_confusion_matrix(
            ys_val, y_pred_s,
            f"Fold {fold} Source ConfMat",
            os.path.join(fold_dir, f"Fold{fold}_Source_ConfMat.png")
        )

        plot_training_history(history_log, fold_dir, fold)

        # ---------- t-SNE ----------
        if fold == k_folds:
            src_feats = feature_model.predict(Xs_val, verbose=0)
            tgt_feats = feature_model.predict(Xt_test, verbose=0)
            plot_tsne(src_feats, tgt_feats, os.path.join(fold_dir, "TSNE_Final.png"))

        # ---------- XAI ----------
        should_run_xai = (fold == k_folds) if RUN_XAI_ONLY_LAST_FOLD else True
        if should_run_xai:
            print(f"\nRunning Grad-CAM + SHAP for Fold {fold}...")

            gradcam_source_dir = os.path.join(fold_dir, "gradcam_source")
            gradcam_target_dir = os.path.join(fold_dir, "gradcam_target")
            shap_source_dir = os.path.join(fold_dir, "shap_source")
            shap_target_dir = os.path.join(fold_dir, "shap_target")

            generate_gradcam_examples(
                model, Xs_val, ys_val,
                domain_name="source_domain",
                save_root=gradcam_source_dir,
                n_per_class=N_PER_CLASS_XAI
            )

            generate_gradcam_examples(
                model, Xt_test, yt_test,
                domain_name="target_domain",
                save_root=gradcam_target_dir,
                n_per_class=N_PER_CLASS_XAI
            )

            bg_size = min(SHAP_BG_SIZE, len(Xs_train))
            background = Xs_train[:bg_size]
            explainer = shap.GradientExplainer(model, background)

            generate_shap_examples(
                model, explainer, Xs_val, ys_val,
                domain_name="source_domain",
                save_root=shap_source_dir,
                n_per_class=N_PER_CLASS_XAI
            )

            generate_shap_examples(
                model, explainer, Xt_test, yt_test,
                domain_name="target_domain",
                save_root=shap_target_dir,
                n_per_class=N_PER_CLASS_XAI
            )

            save_shap_summary(
                model, explainer, Xt_test,
                os.path.join(shap_target_dir, "shap_summary_target_sda_1dcnn.png")
            )

            print("Grad-CAM and SHAP completed.")

    # ---------- SUMMARY ----------
    df_src = pd.DataFrame(results_src, columns=["Acc", "Prec", "Rec", "F1"])
    df_tgt = pd.DataFrame(results_tgt, columns=["Acc", "Prec", "Rec", "F1"])

    df_src["Type"] = "Source"
    df_tgt["Type"] = "Target"
    df_src["Fold"] = [f"Fold_{i+1}" for i in range(len(df_src))]
    df_tgt["Fold"] = [f"Fold_{i+1}" for i in range(len(df_tgt))]

    df = pd.concat([df_src, df_tgt], ignore_index=True)

    for t in ["Source", "Target"]:
        avg = df[df["Type"] == t][["Acc", "Prec", "Rec", "F1"]].mean()
        avg["Type"] = t
        avg["Fold"] = "Average"
        df = pd.concat([df, pd.DataFrame([avg])], ignore_index=True)

    save_path = os.path.join(base_dir, "Summary.xlsx")
    df.to_excel(save_path, index=False)
    print(f"\nSaved summary to {save_path}")


# =========================================================
# 9) MAIN
# =========================================================
if __name__ == "__main__":
    src_signals, src_labels = load_source_data()
    tgt_signals, tgt_labels = load_target_data()

    is_12K_source = SOURCE_NAME.startswith("12K")
    is_12K_target = TARGET_NAME.startswith("12K")
    is_48K_source = SOURCE_NAME.startswith("48K")
    is_48K_target = TARGET_NAME.startswith("48K")

    if is_12K_source:
        print("\n[Source] 12K detected → Applying downsampling (keep 1 of 4 for label 0)")
        src_signals, src_labels = downsample_raw_signals(src_signals, src_labels, factor=4)
    else:
        print("\n[Source] 48K detected → No downsampling")

    if is_12K_target:
        print("[Target] 12K detected → Applying downsampling (keep 1 of 4 for label 0)")
        tgt_signals, tgt_labels = downsample_raw_signals(tgt_signals, tgt_labels, factor=4)
    else:
        print("[Target] 48K detected → No downsampling")

    if is_48K_source and not is_48K_target:
        print("\n[Source] 48K detected → Resampling to 12K to match target")
        src_signals, src_labels = resample_to_12K(src_signals, src_labels)
    else:
        print("\n[Source] No resampling needed")

    if is_48K_target and not is_48K_source:
        print("[Target] 48K detected → Resampling to 12K to match source")
        tgt_signals, tgt_labels = resample_to_12K(tgt_signals, tgt_labels)
    else:
        print("[Target] No resampling needed")

    Xs, ys = segment_signals(src_signals, src_labels, INTERVAL, SAMPLES_PER_BLOCK)
    Xt, yt = segment_signals(tgt_signals, tgt_labels, INTERVAL, SAMPLES_PER_BLOCK)

    print("\nBefore balancing - Source counts:")
    for c in np.unique(ys):
        print(f" Class {c}: {np.sum(ys == c)}")

    print("Before balancing - Target counts:")
    for c in np.unique(yt):
        print(f" Class {c}: {np.sum(yt == c)}")

    Xs_bal, ys_bal = balance_after_segmentation(Xs, ys, per_class=None, seed=SEED)
    Xt_bal, yt_bal = balance_after_segmentation(Xt, yt, per_class=None, seed=SEED + 1)

    print("\nAfter balancing - Source counts:")
    for c in np.unique(ys_bal):
        print(f" Class {c}: {np.sum(ys_bal == c)}")

    print("\nAfter balancing - Target counts:")
    for c in np.unique(yt_bal):
        print(f" Class {c}: {np.sum(yt_bal == c)}")

    train_supervised_da_kfold(
        Xs_bal, ys_bal, Xt_bal, yt_bal,
        k_folds=KFOLD,
        pretrain_epochs=PRETRAIN_EPOCHS,
        batch_size=BATCH_SIZE,
        use_mmd=USE_MMD,
        use_coral=USE_CORAL,
        mmd_weight=MMD_WEIGHT,
        coral_weight=CORAL_WEIGHT,
        patience=PATIENCE
    )