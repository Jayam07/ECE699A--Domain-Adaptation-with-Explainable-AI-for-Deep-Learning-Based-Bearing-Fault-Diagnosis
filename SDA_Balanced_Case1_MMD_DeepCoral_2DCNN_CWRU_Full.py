# -*- coding: utf-8 -*-
"""
Supervised Domain Adaptation using 2D CNN (Balanced Data) + 5-Fold CV
Supports:
 - Balanced supervised only
 - Balanced + MMD
 - Balanced + CORAL
 - Balanced + MMD + CORAL

Recommended experiments:
 - 12K1HP -> 12K2HP
 - 12K1HP -> 12K3HP
 - 12K1HP -> 48K1HP
"""

import os
import numpy as np
import scipy.io
import pandas as pd
import tensorflow as tf

from datetime import datetime
from scipy.signal import resample_poly
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import StratifiedKFold, train_test_split
from tensorflow.keras import layers, models

# -----------------------
# Config
# -----------------------
SEED = 42
np.random.seed(SEED)
tf.random.set_seed(SEED)
os.environ["PYTHONHASHSEED"] = str(SEED)

# -----------------------
# CHANGE THESE FOR EXPERIMENTS
# -----------------------
SOURCE_NAME = "12K1HP"
TARGET_NAME = "12K2HP"
# SOURCE_NAME = "12K1HP"; TARGET_NAME = "12K3HP"
# SOURCE_NAME = "12K1HP"; TARGET_NAME = "48K1HP"

USE_MMD = True
USE_CORAL = False

MMD_WEIGHT = 0.1
CORAL_WEIGHT = 0.0

KFOLD = 5
PRETRAIN_EPOCHS = 100
PATIENCE = 15
BATCH_SIZE = 64

# For 2D CNN, use 400 -> 20x20
INTERVAL = 400
SAMPLES_PER_BLOCK = 400

VERBOSE = 1

BASE_SAVE_ROOT = "/content/drive/MyDrive/SDA_2DCNN_CWRU_RESULTS"

# -----------------------
# Load signals
# -----------------------
def load_signals(folder_path, files):
    signals, labels = [], []
    for fname, lbl in files:
        fpath = os.path.join(folder_path, fname)
        mat = scipy.io.loadmat(fpath)

        file_num = os.path.splitext(fname)[0]
        de_keys = [k for k in mat.keys() if "DE_time" in k]
        match_keys = [k for k in de_keys if file_num in k]

        if match_keys:
            key = match_keys[0]
        elif de_keys:
            key = de_keys[0]
            print(f"[Warning] Using first DE_time key for {fname}: {key}")
        else:
            print(f"[Warning] No DE_time found: {fname}")
            continue

        signals.append(np.array(mat[key]).flatten())
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


def load_source_data():
    folder, files = DATASETS[SOURCE_NAME]
    return load_signals(folder, [(f, i) for i, f in enumerate(files)])


def load_target_data():
    folder, files = DATASETS[TARGET_NAME]
    return load_signals(folder, [(f, i) for i, f in enumerate(files)])


# -----------------------
# Segmentation
# -----------------------
def Sampling(data, interval_length, samples_per_block, ignore_points=0):
    adjusted_length = len(data) - 2 * ignore_points
    n_blocks = (
        round(adjusted_length / interval_length)
        - round(samples_per_block / interval_length)
        - 1
    )

    if n_blocks <= 0:
        return np.zeros((0, samples_per_block))

    X = np.zeros((n_blocks, samples_per_block))
    for i in range(n_blocks):
        start = ignore_points + i * interval_length
        X[i, :] = data[start:start + samples_per_block]
    return X


def segment_signals(signals, labels, interval_length, samples_per_block):
    X, y = [], []
    for sig, lbl in zip(signals, labels):
        segs = Sampling(sig, interval_length, samples_per_block)
        if segs.shape[0] > 0:
            X.append(segs)
            y.extend([lbl] * len(segs))

    if len(X) == 0:
        return np.zeros((0, samples_per_block)), np.array([])

    X = np.vstack(X)
    y = np.array(y)
    return X, y


# -----------------------
# Downsampling / Resampling
# -----------------------
def downsample_raw_signals(signals, labels, factor=4):
    """
    Keep 1 out of every 4 raw signals only for class 0, as in your 1D code.
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


def resample_to_12K(signals, labels):
    """
    Downsample 48K raw signals to 12K by factor 4.
    """
    new_signals = [resample_poly(sig, up=1, down=4) for sig in signals]
    return new_signals, labels


# -----------------------
# Reshape 1D -> 2D
# -----------------------
def reshape_to_2d(X_1d, block_size=400):
    side = int(np.sqrt(block_size))
    if side * side != block_size:
        raise ValueError(f"block_size={block_size} is not a perfect square.")
    return X_1d.reshape((-1, side, side, 1))


# -----------------------
# Balance dataset
# -----------------------
def balance_after_segmentation(X, y, per_class=None, seed=42):
    classes = np.unique(y)
    counts = {c: np.sum(y == c) for c in classes}
    if per_class is None:
        per_class = int(min(counts.values()))

    X_parts, y_parts = [], []
    rng = np.random.RandomState(seed)

    for c in classes:
        idx = np.where(y == c)[0]
        if len(idx) > per_class:
            idx = rng.choice(idx, per_class, replace=False)
        X_parts.append(X[idx])
        y_parts.append(y[idx])

    X_new = np.vstack(X_parts)
    y_new = np.concatenate(y_parts)

    perm = rng.permutation(len(y_new))
    return X_new[perm], y_new[perm]


# -----------------------
# 2D CNN MODEL
# -----------------------
def build_cnn_2d(input_shape, num_classes=10):
    inputs = layers.Input(shape=input_shape)

    x = layers.Conv2D(16, (3, 3), padding="same", activation="relu", name="conv1")(inputs)
    x = layers.BatchNormalization()(x)
    x = layers.MaxPooling2D((2, 2))(x)

    x = layers.Conv2D(32, (3, 3), padding="same", activation="relu", name="conv2")(x)
    x = layers.BatchNormalization()(x)
    x = layers.MaxPooling2D((2, 2))(x)

    x = layers.Conv2D(64, (3, 3), padding="same", activation="relu", name="conv3")(x)
    x = layers.BatchNormalization()(x)
    x = layers.GlobalAveragePooling2D()(x)

    feature = layers.Dense(128, activation="relu", name="feature_layer")(x)
    output = layers.Dense(num_classes, activation="softmax")(feature)

    model = models.Model(inputs=inputs, outputs=output)
    return model


# -----------------------
# MMD + CORAL losses
# -----------------------
def mmd_loss(fs, ft):
    return tf.reduce_mean(tf.square(tf.reduce_mean(fs, axis=0) - tf.reduce_mean(ft, axis=0)))


def coral_loss(fs, ft):
    def cov(x):
        x = x - tf.reduce_mean(x, axis=0, keepdims=True)
        n = tf.cast(tf.shape(x)[0], tf.float32)
        return tf.matmul(x, x, transpose_a=True) / (n - 1 + 1e-8)

    cs = cov(fs)
    ct = cov(ft)
    d = tf.cast(tf.shape(cs)[0], tf.float32)
    return tf.reduce_sum(tf.square(cs - ct)) / (4 * d * d)


# -----------------------
# TRAINING
# -----------------------
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
    exp_name = f"2DCNN_SDA_{SOURCE_NAME}_TO_{TARGET_NAME}"
    base_dir = os.path.join(BASE_SAVE_ROOT, f"{exp_name}_{timestamp}")
    os.makedirs(base_dir, exist_ok=True)

    kfold = StratifiedKFold(n_splits=k_folds, shuffle=True, random_state=SEED)

    results_src, results_tgt = [], []

    for fold, (train_idx, val_idx) in enumerate(kfold.split(Xs, ys), start=1):
        print(f"\n=========== Fold {fold}/{k_folds} ===========")

        Xs_tr, Xs_val = Xs[train_idx], Xs[val_idx]
        ys_tr, ys_val = ys[train_idx], ys[val_idx]

        Xt_tr, Xt_te, yt_tr, yt_te = train_test_split(
            Xt, yt, test_size=0.2, random_state=SEED + fold, stratify=yt
        )

        model = build_cnn_2d(input_shape=Xs_tr.shape[1:], num_classes=len(np.unique(ys)))
        feature_model = models.Model(model.input, model.get_layer("feature_layer").output)

        optimizer = tf.keras.optimizers.Adam(1e-4)
        ce = tf.keras.losses.SparseCategoricalCrossentropy()

        best_val = 0.0
        patience_cnt = 0
        fold_dir = os.path.join(base_dir, f"Fold_{fold}")
        os.makedirs(fold_dir, exist_ok=True)
        best_path = os.path.join(fold_dir, "best_model.weights.h5")

        for ep in range(pretrain_epochs):
            idx_s = np.random.permutation(len(Xs_tr))
            idx_t = np.random.permutation(len(Xt_tr))
            Xs_sh, ys_sh = Xs_tr[idx_s], ys_tr[idx_s]
            Xt_sh, yt_sh = Xt_tr[idx_t], yt_tr[idx_t]

            num_batches = min(len(Xs_sh), len(Xt_sh)) // batch_size
            if num_batches == 0:
                num_batches = 1

            train_loss_sum = 0.0

            for b in range(num_batches):
                s = slice(b * batch_size, (b + 1) * batch_size)

                Xs_b, ys_b = Xs_sh[s], ys_sh[s]
                Xt_b, yt_b = Xt_sh[s], yt_sh[s]

                if len(Xs_b) == 0 or len(Xt_b) == 0:
                    continue

                with tf.GradientTape() as tape:
                    log_s = model(Xs_b, training=True)
                    log_t = model(Xt_b, training=True)

                    loss_ce = 0.5 * (ce(ys_b, log_s) + ce(yt_b, log_t))

                    fs = feature_model(Xs_b, training=True)
                    ft = feature_model(Xt_b, training=True)

                    loss_align = 0.0
                    if use_mmd:
                        loss_align += mmd_weight * mmd_loss(fs, ft)
                    if use_coral:
                        loss_align += coral_weight * coral_loss(fs, ft)

                    loss_total = loss_ce + loss_align

                grads = tape.gradient(loss_total, model.trainable_variables)
                optimizer.apply_gradients(zip(grads, model.trainable_variables))
                train_loss_sum += float(loss_total.numpy())

            val_pred = np.argmax(model.predict(Xs_val, verbose=0), axis=1)
            val_acc = accuracy_score(ys_val, val_pred)

            if VERBOSE:
                print(f"Epoch {ep+1}/{pretrain_epochs} | TrainLoss={train_loss_sum/max(num_batches,1):.4f} | ValAcc={val_acc:.4f}")

            if val_acc > best_val:
                best_val = val_acc
                patience_cnt = 0
                model.save_weights(best_path)
            else:
                patience_cnt += 1

            if patience_cnt >= patience:
                print("Early stopping.")
                break

        # Load best model
        model.load_weights(best_path)

        # Evaluate on source validation
        src_pred = np.argmax(model.predict(Xs_val, verbose=0), axis=1)
        acc = accuracy_score(ys_val, src_pred)
        prec = precision_score(ys_val, src_pred, average="macro", zero_division=0)
        rec = recall_score(ys_val, src_pred, average="macro", zero_division=0)
        f1 = f1_score(ys_val, src_pred, average="macro", zero_division=0)
        results_src.append([acc, prec, rec, f1])

        # Evaluate on target test
        tgt_pred = np.argmax(model.predict(Xt_te, verbose=0), axis=1)
        acc = accuracy_score(yt_te, tgt_pred)
        prec = precision_score(yt_te, tgt_pred, average="macro", zero_division=0)
        rec = recall_score(yt_te, tgt_pred, average="macro", zero_division=0)
        f1 = f1_score(yt_te, tgt_pred, average="macro", zero_division=0)
        results_tgt.append([acc, prec, rec, f1])

        print(f"Fold {fold} | Source Acc={results_src[-1][0]:.4f} | Target Acc={results_tgt[-1][0]:.4f}")

    # -----------------------
    # Summary
    # -----------------------
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


# -----------------------
# Main
# -----------------------
if __name__ == "__main__":
    # Load raw signals
    src_signals, src_labels = load_source_data()
    tgt_signals, tgt_labels = load_target_data()

    # Detect dataset type
    is_12K_source = SOURCE_NAME.startswith("12K")
    is_12K_target = TARGET_NAME.startswith("12K")
    is_48K_source = SOURCE_NAME.startswith("48K")
    is_48K_target = TARGET_NAME.startswith("48K")

    # Downsampling for 12K datasets only
    if is_12K_source:
        print("\n[Source] 12K detected -> Applying downsampling (keep 1 of 4 for label 0)")
        src_signals, src_labels = downsample_raw_signals(src_signals, src_labels, factor=4)
    else:
        print("\n[Source] 48K detected -> No downsampling")

    if is_12K_target:
        print("[Target] 12K detected -> Applying downsampling (keep 1 of 4 for label 0)")
        tgt_signals, tgt_labels = downsample_raw_signals(tgt_signals, tgt_labels, factor=4)
    else:
        print("[Target] 48K detected -> No downsampling")

    # Resample 48K -> 12K only if needed
    if is_48K_source and not is_48K_target:
        print("\n[Source] 48K detected -> Resampling to 12K to match target")
        src_signals, src_labels = resample_to_12K(src_signals, src_labels)
    else:
        print("\n[Source] No resampling needed")

    if is_48K_target and not is_48K_source:
        print("[Target] 48K detected -> Resampling to 12K to match source")
        tgt_signals, tgt_labels = resample_to_12K(tgt_signals, tgt_labels)
    else:
        print("[Target] No resampling needed")

    # Segment signals
    Xs, ys = segment_signals(src_signals, src_labels, INTERVAL, SAMPLES_PER_BLOCK)
    Xt, yt = segment_signals(tgt_signals, tgt_labels, INTERVAL, SAMPLES_PER_BLOCK)

    print(f"\nBefore balancing - Source counts:")
    for c in np.unique(ys):
        print(f" Class {c}: {np.sum(ys == c)}")

    print(f"\nBefore balancing - Target counts:")
    for c in np.unique(yt):
        print(f" Class {c}: {np.sum(yt == c)}")

    # Balance
    Xs_bal, ys_bal = balance_after_segmentation(Xs, ys, per_class=None, seed=SEED)
    Xt_bal, yt_bal = balance_after_segmentation(Xt, yt, per_class=None, seed=SEED + 1)

    print(f"\nAfter balancing - Source counts:")
    for c in np.unique(ys_bal):
        print(f" Class {c}: {np.sum(ys_bal == c)}")

    print(f"\nAfter balancing - Target counts:")
    for c in np.unique(yt_bal):
        print(f" Class {c}: {np.sum(yt_bal == c)}")

    # Reshape 1D -> 2D
    Xs_bal = reshape_to_2d(Xs_bal, SAMPLES_PER_BLOCK)
    Xt_bal = reshape_to_2d(Xt_bal, SAMPLES_PER_BLOCK)

    print("\n2D shapes:")
    print("Xs_bal:", Xs_bal.shape)
    print("Xt_bal:", Xt_bal.shape)

    # Training
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