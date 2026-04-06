# -*- coding: utf-8 -*-
"""
Supervised Domain Adaptation (Balanced data) + 5-Fold CV
Supports four modes:
 - Balanced only (supervised training on source + target labeled data with K-Fold)
 - Balanced + MMD
 - Balanced + CORAL
 - Balanced + MMD + CORAL

Notes:
 - Resample 12K normal data and 48K all data to 12K (because normal data measured using 48K)
 - if both source and target data are 48K no resampling
 - Balancing is done AFTER segmentation to guarantee equal numbers of windows per class.
 - No pseudo-labeling.
 - K-Fold is applied to SOURCE domain (train/val split). TARGET is split into train/test (20% test).
"""
import os
import numpy as np
import scipy.io
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.manifold import TSNE
from sklearn.model_selection import StratifiedKFold, train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from datetime import datetime


# -----------------------
# Config (edit these)
# -----------------------
SEED = 42
np.random.seed(SEED)
tf.random.set_seed(SEED)
os.environ['PYTHONHASHSEED'] = str(SEED)

SOURCE_NAME = "12K1HP"
TARGET_NAME = "12K3HP"

# Choose mode by flags:  #
USE_MMD = True      # set True to enable MMD loss, or False to disable it 
USE_CORAL = False    # set True to enable CORAL loss, or False to disable it 

# Loss weights
MMD_WEIGHT = 0.1
CORAL_WEIGHT = 0.0

# training hyperparams
PRETRAIN_EPOCHS = 100  # smaller for quick tests; increase for final runs
PATIENCE = 15
BATCH_SIZE = 64
KFOLD = 5
INTERVAL = 400
SAMPLES_PER_BLOCK = 400

# Misc
VERBOSE = 1

# -----------------------
# Loading signals
# -----------------------
def load_signals(folder_path, files):
    signals, labels = [], []
    for fname, lbl in files:
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

DATASETS = {
    "12K0HP": ("/content/drive/MyDrive/BearingData_CaseWestern_12K1797",
               ['97.mat','105.mat','118.mat','130.mat','169.mat',
                '185.mat','197.mat','209.mat','222.mat','234.mat']),

    "12K1HP": ("/content/drive/MyDrive/BearingData_CaseWestern_12K1772",
               ['98.mat','106.mat','119.mat','131.mat','170.mat',
                '186.mat','198.mat','210.mat','223.mat','235.mat']),

    "12K2HP": ("/content/drive/MyDrive/BearingData_CaseWestern_12K1750",
               ['99.mat','107.mat','120.mat','132.mat','171.mat',
                '187.mat','199.mat','211.mat','224.mat','236.mat']),

    "12K3HP": ("/content/drive/MyDrive/BearingData_CaseWestern_12K1730",
               ['100.mat','108.mat','121.mat','133.mat','172.mat',
                '188.mat','200.mat','212.mat','225.mat','237.mat']),

    "48K1HP": ("/content/drive/MyDrive/BearingData_CaseWestern_48K1772",
               ['98.mat','110.mat','123.mat','136.mat','175.mat',
                '190.mat','202.mat','214.mat','227.mat','239.mat']),

    "48K2HP": ("/content/drive/MyDrive/BearingData_CaseWestern_48K1750",
               ['99.mat','111.mat','124.mat','137.mat','176.mat',
                '191.mat','203.mat','215.mat','228.mat','240.mat']),

    "48K3HP": ("/content/drive/MyDrive/BearingData_CaseWestern_48K1730",
               ['100.mat','112.mat','125.mat','138.mat','177.mat',
                '192.mat','204.mat','217.mat','229.mat','241.mat'])
}
'/content/drive/MyDrive/BearingData_CaseWestern_12K1750'
# ---------------------------------------------------------
#   Downsample raw signals before segmentation Only for 12K datasets (1 of every 4 for label 0)
# ---------------------------------------------------------
def downsample_raw_signals(signals, labels, factor=4):
    signals = np.array(signals, dtype=object)
    labels = np.array(labels)

    keep_idx = []
    for cls in np.unique(labels):
        idx = np.where(labels == cls)[0]
        if cls == 0:
            # label 0 -> take 1 every 4
            keep_idx.extend(idx[::factor])
        else:
            # keep all other labels
            keep_idx.extend(idx)

    keep_idx = np.array(keep_idx)
    return list(signals[keep_idx]), list(labels[keep_idx])

from scipy.signal import resample

# -----------------------
# Resample 48K -> 12K
# -----------------------
def resample_to_12K(signals, labels, orig_rate=48000, target_rate=12000):
    factor = orig_rate // target_rate
    new_signals = []
    for sig in signals:
        # Resample to target number of points
        n_samples = len(sig) // factor
        sig_resampled = resample(sig, n_samples)
        new_signals.append(sig_resampled)
    return new_signals, labels


def load_source_data():
    folder, files = DATASETS[SOURCE_NAME]
    file_label_pairs = [(f, i) for i, f in enumerate(files)]
    return load_signals(folder, file_label_pairs)

def load_target_data():
    folder, files = DATASETS[TARGET_NAME]
    file_label_pairs = [(f, i) for i, f in enumerate(files)]
    return load_signals(folder, file_label_pairs)

# -----------------------
# Sampling & segmentation
# -----------------------
def Sampling(Data, interval_length, samples_per_block, ignore_points=0):
    adjusted_length = len(Data) - 2 * ignore_points
    No_of_blocks = (
        round(adjusted_length / interval_length) - round(samples_per_block / interval_length) - 1
    )
    if No_of_blocks <= 0:
        return np.zeros((0, samples_per_block))
    SplitData = np.zeros([No_of_blocks, samples_per_block])
    for i in range(No_of_blocks):
        start_idx = ignore_points + i * interval_length
        SplitData[i, :] = Data[start_idx:(start_idx + samples_per_block)].T
    return SplitData

def segment_signals(signals, labels, interval_length=INTERVAL, samples_per_block=SAMPLES_PER_BLOCK, ignore_points=0):
    X, y = [], []
    for sig, lbl in zip(signals, labels):
        segments = Sampling(sig, interval_length, samples_per_block, ignore_points)
        if segments.shape[0] == 0:
            continue
        X.append(segments)
        y.extend([lbl] * len(segments))
    if len(X) == 0:
        return np.zeros((0, samples_per_block, 1)), np.array([])
    X = np.vstack(X)[..., np.newaxis]
    y = np.array(y)
    return X, y

# -----------------------
# Balance (after segmentation) -> equal samples per class
# -----------------------
def balance_after_segmentation(X, y, per_class=None, seed=SEED):
    """
    Make dataset balanced by sampling each class to 'per_class' samples.
    If per_class is None, use min class count.
    Returns X_bal, y_bal (shuffled)
    """
    rng = np.random.RandomState(seed)
    classes = np.unique(y)
    counts = {c: np.sum(y == c) for c in classes}
    if per_class is None:
        per_class = int(min(counts.values()))
    X_parts = []
    y_parts = []
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

# -----------------------
# Utilities: plotting + logging
# -----------------------
def plot_confusion_matrix(y_true, y_pred, title, save_path):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title(title)
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def plot_tsne(source_feats, target_feats, save_path, perplexity=30, lr=200):
    X = np.concatenate([source_feats, target_feats], axis=0)
    domain_labels = np.array([0]*len(source_feats) + [1]*len(target_feats))
    tsne = TSNE(n_components=2, perplexity=perplexity, learning_rate=lr, random_state=SEED)
    X_tsne = tsne.fit_transform(X)
    plt.figure(figsize=(8,6))
    plt.scatter(X_tsne[domain_labels==0,0], X_tsne[domain_labels==0,1], s=8, label='Source', alpha=0.6)
    plt.scatter(X_tsne[domain_labels==1,0], X_tsne[domain_labels==1,1], s=8, label='Target', alpha=0.6)
    plt.legend()
    plt.title("T-SNE Feature Distribution (Source vs Target)")
    plt.tight_layout()
    plt.savefig(save_path)
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
    plt.savefig(os.path.join(folder_dir, f"Fold{fold_num}_Training_History.png"))
    plt.close()

# -----------------------
# Model
# -----------------------
def build_cnn(input_shape=(INTERVAL,1), num_classes=10):
    model = models.Sequential([
        layers.Input(shape=input_shape),

        layers.Conv1D(16, 3, activation='relu', padding='same'),
        layers.BatchNormalization(),
        layers.MaxPooling1D(2),

        layers.Conv1D(32, 3, activation='relu', padding='same'),
        layers.BatchNormalization(),
        layers.MaxPooling1D(2),

        layers.Conv1D(64, 3, activation='relu', padding='same'),
        layers.BatchNormalization(),
        layers.GlobalAveragePooling1D(),

        layers.Dense(128, activation='relu', name='feature_layer'),
        layers.Dense(num_classes, activation='softmax')
    ])
    return model

# -----------------------
# MMD (mean matching as in your original code)
# -----------------------
def mmd_loss(source_features, target_features):
    x_mean = tf.reduce_mean(source_features, axis=0)
    y_mean = tf.reduce_mean(target_features, axis=0)
    return tf.reduce_mean(tf.square(x_mean - y_mean))

# -----------------------
# CORAL (Deep CORAL) loss
# -----------------------
def coral_loss(source_features, target_features):
    """
    Deep CORAL: align covariance matrices of source and target features.
    Returns scalar loss.
    """
    def covariance(x):
        # x: [batch, feat]
        n = tf.cast(tf.shape(x)[0], tf.float32)
        xm = x - tf.reduce_mean(x, axis=0, keepdims=True)
        cov = tf.matmul(tf.transpose(xm), xm) / (n - 1.0 + 1e-8)
        return cov

    cs = covariance(source_features)
    ct = covariance(target_features)
    d = tf.cast(tf.shape(cs)[0], tf.float32)
    loss = tf.reduce_sum(tf.square(cs - ct)) / (4.0 * d * d)
    return loss

# -----------------------
# Train (supervised DA) with K-Fold on SOURCE
# -----------------------
def train_supervised_da_kfold(Xs, ys, Xt, yt,
                              k_folds=KFOLD,
                              pretrain_epochs=PRETRAIN_EPOCHS,
                              batch_size=BATCH_SIZE,
                              use_mmd=USE_MMD,
                              use_coral=USE_CORAL,
                              mmd_weight=MMD_WEIGHT,
                              coral_weight=CORAL_WEIGHT,
                              patience=PATIENCE):  # NEW
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_dir = f"Results_SupervisedDA_{timestamp}"
    os.makedirs(base_dir, exist_ok=True)

    kfold = StratifiedKFold(n_splits=k_folds, shuffle=True, random_state=SEED)
    fold = 1
    results_src = []
    results_tgt = []

    for train_idx, val_idx in kfold.split(Xs, ys):
        print(f"\n========== Fold {fold}/{k_folds} ==========")

        # split source into train/val
        Xs_train, Xs_val = Xs[train_idx], Xs[val_idx]
        ys_train, ys_val = ys[train_idx], ys[val_idx]

        # split target into train/test
        Xt_train, Xt_test, yt_train, yt_test = train_test_split(Xt, yt, test_size=0.2, random_state=SEED+fold, stratify=yt)

        # ensure batches are not empty
        if len(Xs_train) == 0 or len(Xt_train) == 0:
            raise ValueError("Empty train split encountered.")

        model = build_cnn(input_shape=(Xs.shape[1], 1), num_classes=10)
        feature_model = models.Model(inputs=model.inputs, outputs=model.get_layer('feature_layer').output)
        optimizer = tf.keras.optimizers.Adam(1e-4)
        ce_loss = tf.keras.losses.SparseCategoricalCrossentropy()

        # early stopping setup
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

            # shuffle
            idx_s = np.random.permutation(len(Xs_train))
            idx_t = np.random.permutation(len(Xt_train))
            Xs_sh = Xs_train[idx_s]; ys_sh = ys_train[idx_s]
            Xt_sh = Xt_train[idx_t]; yt_sh = yt_train[idx_t]

            num_batches = min(len(Xs_sh), len(Xt_sh)) // batch_size
            if num_batches == 0:
                num_batches = 1

            for b in range(num_batches):
                s_start, s_end = b*batch_size, (b+1)*batch_size
                t_start, t_end = b*batch_size, (b+1)*batch_size

                Xs_b = Xs_sh[s_start:s_end]; ys_b = ys_sh[s_start:s_end]
                Xt_b = Xt_sh[t_start:t_end]; yt_b = yt_sh[t_start:t_end]

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
                        loss_m = mmd_loss(fs, ft)
                        align_loss += mmd_weight * loss_m
                    if use_coral:
                        fs = feature_model(Xs_b) if not use_mmd else fs
                        ft = feature_model(Xt_b) if not use_mmd else ft
                        loss_c = coral_loss(fs, ft)
                        align_loss += coral_weight * loss_c

                    loss_total = loss_ce_total + align_loss

                grads = tape.gradient(loss_total, model.trainable_variables)
                optimizer.apply_gradients(zip(grads, model.trainable_variables))

                train_loss_accum += float(loss_total.numpy())
                train_steps += 1

            # validation on source_val
            val_logits = model.predict(Xs_val, verbose=0)
            val_preds = np.argmax(val_logits, axis=1)
            val_acc = accuracy_score(ys_val, val_preds)
            val_loss = float(np.mean(tf.keras.losses.sparse_categorical_crossentropy(ys_val, val_logits).numpy()))
            avg_train_loss = train_loss_accum / max(1, train_steps)

            if VERBOSE:
                print(f" Epoch {ep+1}/{pretrain_epochs} | TrainLoss={avg_train_loss:.4f} | ValAcc={val_acc:.4f}")

            history_log.append({
                "epoch": ep+1,
                "train_loss": avg_train_loss,
                "val_loss": val_loss,
                "val_acc": val_acc
            })

            # -----------------------
            # Early stopping check
            # -----------------------
            if val_acc > best_val:
                best_val = val_acc
                model.save_weights(best_path)
                epochs_since_improvement = 0
            else:
                epochs_since_improvement += 1

            if epochs_since_improvement >= patience:
                print(f"Early stopping triggered at epoch {ep+1} (no improvement in {patience} epochs)")
                break

        # reload best model
        model.load_weights(best_path)
        feature_model = models.Model(inputs=model.inputs, outputs=model.get_layer('feature_layer').output)
        # -----------------------
        # Evaluation
        # -----------------------
        # target test
        y_pred_t = np.argmax(model.predict(Xt_test), axis=1)
        acc_t = accuracy_score(yt_test, y_pred_t)
        prec_t = precision_score(yt_test, y_pred_t, average="macro", zero_division=0)
        rec_t = recall_score(yt_test, y_pred_t, average="macro", zero_division=0)
        f1_t = f1_score(yt_test, y_pred_t, average="macro", zero_division=0)
        results_tgt.append([acc_t, prec_t, rec_t, f1_t])
        plot_confusion_matrix(yt_test, y_pred_t, f"Fold {fold} Target ConfMat",
                              os.path.join(fold_dir, f"Fold{fold}_Target_ConfMat.png"))

        # source val metrics
        y_pred_s = np.argmax(model.predict(Xs_val), axis=1)
        acc_s = accuracy_score(ys_val, y_pred_s)
        prec_s = precision_score(ys_val, y_pred_s, average="macro", zero_division=0)
        rec_s = recall_score(ys_val, y_pred_s, average="macro", zero_division=0)
        f1_s = f1_score(ys_val, y_pred_s, average="macro", zero_division=0)
        results_src.append([acc_s, prec_s, rec_s, f1_s])

        # save history and plots
        plot_training_history(history_log, fold_dir, fold)

        # t-SNE for last fold
        if fold == k_folds:
            src_feats = feature_model.predict(Xs_val)
            tgt_feats = feature_model.predict(Xt_test)
            plot_tsne(src_feats, tgt_feats, os.path.join(fold_dir, "TSNE_Final.png"))

        fold += 1

    # -----------------------
    # Summary
    # -----------------------
    df_src = pd.DataFrame(results_src, columns=["Acc","Prec","Rec","F1"])
    df_tgt = pd.DataFrame(results_tgt, columns=["Acc","Prec","Rec","F1"])
    df_src["Type"]="Source"; df_tgt["Type"]="Target"
    df_src["Fold"]=[f"Fold_{i+1}" for i in range(len(df_src))]
    df_tgt["Fold"]=[f"Fold_{i+1}" for i in range(len(df_tgt))]
    df = pd.concat([df_src, df_tgt], ignore_index=True)

    for t in ["Source","Target"]:
        avg = df[df["Type"]==t][["Acc","Prec","Rec","F1"]].mean()
        avg["Type"]=t; avg["Fold"]="Average"
        df = pd.concat([df, pd.DataFrame([avg])], ignore_index=True)

    save_path = os.path.join(base_dir, "Summary.xlsx")
    df.to_excel(save_path, index=False)
    print(f"\nSaved summary to {save_path}")


# -----------------------
# Main
# -----------------------

if __name__ == "__main__":
    # Load raw signals
    src_signals, src_labels = load_source_data()
    tgt_signals, tgt_labels = load_target_data()

    # ============================
    # Detect dataset type
    # ============================
    is_12K_source = SOURCE_NAME.startswith("12K")
    is_12K_target = TARGET_NAME.startswith("12K")
    is_48K_source = SOURCE_NAME.startswith("48K")
    is_48K_target = TARGET_NAME.startswith("48K")

    # ============================
    # Downsampling for 12K datasets only
    # ============================
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

    # ============================
    # Resample 48K → 12K only if needed
    # ============================
    # If both source and target are 48K, keep full 48K
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

    # ============================
    # Segment signals
    # ============================
    Xs, ys = segment_signals(src_signals, src_labels, INTERVAL, SAMPLES_PER_BLOCK)
    Xt, yt = segment_signals(tgt_signals, tgt_labels, INTERVAL, SAMPLES_PER_BLOCK)

    print(f"Before balancing - Source counts:")
    for c in np.unique(ys):
        print(f" Class {c}: {np.sum(ys==c)}")
    print(f"Before balancing - Target counts:")
    for c in np.unique(yt):
        print(f" Class {c}: {np.sum(yt==c)}")

    # ============================
    # Balance classes (optional)
    # ============================
    Xs_bal, ys_bal = balance_after_segmentation(Xs, ys, per_class=None, seed=SEED)
    Xt_bal, yt_bal = balance_after_segmentation(Xt, yt, per_class=None, seed=SEED+1)

    print(f"\nAfter balancing - Source counts:")
    for c in np.unique(ys_bal):
        print(f" Class {c}: {np.sum(ys_bal==c)}")
    print(f"\nAfter balancing - Target counts:")
    for c in np.unique(yt_bal):
        print(f" Class {c}: {np.sum(yt_bal==c)}")

    # ============================
    # Training
    # ============================
    train_supervised_da_kfold(Xs_bal, ys_bal, Xt_bal, yt_bal,
                              k_folds=KFOLD,
                              pretrain_epochs=PRETRAIN_EPOCHS,
                              batch_size=BATCH_SIZE,
                              use_mmd=USE_MMD,
                              use_coral=USE_CORAL,
                              mmd_weight=MMD_WEIGHT,
                              coral_weight=CORAL_WEIGHT,
                              patience=PATIENCE)
