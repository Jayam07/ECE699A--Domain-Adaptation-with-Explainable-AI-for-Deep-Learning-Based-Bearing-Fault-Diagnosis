# train.py
import os
import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.model_selection import StratifiedKFold, train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow.keras import models, layers, optimizers, losses

from SDA_data_utils import (
    load_cwru_signals, load_paderborn_signals,
    segment_signals, maybe_resample_list, balance_after_segmentation
)
from SDA_model_utils import build_cnn1d, mmd_loss, coral_loss

# -------------------------------
# Settings
# -------------------------------
SOURCE_KEY = "12K2HP"        # pick from CWRU DATASETS
TARGET_COND = "Condition1"   # pick from PADER_CONDITIONS

USE_TARGET_FRACTION =  1  ##split the target data for 20 percent later in the test part
KFOLD = 5
PRETRAIN_EPOCHS = 200
BATCH_SIZE = 64
PATIENCE = 20
MMD_WEIGHT = 0.1  ## 0.0 means no mmd can try 0.1, 0.5, and 1
CORAL_WEIGHT = 0.0 ## 0.0 means no Coral 0.1~1
USE_MMD = MMD_WEIGHT>0
USE_CORAL = CORAL_WEIGHT>0
SEED = 42
VERBOSE = True

# Segmentation parameters
INTERVAL_LENGTH = 400    # can change
SAMPLES_PER_BLOCK = 1600  # can change  1600
# INTERVAL_LENGTH = 400     # can change
# SAMPLES_PER_BLOCK = 400  # can change  1600

# -------------------------------
# Utilities
# -------------------------------
def plot_confusion_matrix(y_true, y_pred, title, save_path=None):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(6,5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title(title)
    if save_path: plt.savefig(save_path)
    plt.show()
    plt.close()

def plot_training_history(history_log, fold_dir, fold):
    epochs = [h["epoch"] for h in history_log]
    train_loss = [h["train_loss"] for h in history_log]
    val_acc = [h["val_acc"] for h in history_log]

    plt.figure()
    plt.plot(epochs, train_loss, label="Train Loss")
    plt.plot(epochs, val_acc, label="Val Acc")
    plt.xlabel("Epoch")
    plt.ylabel("Value")
    plt.title(f"Fold {fold} Training History")
    plt.legend()
    plt.savefig(os.path.join(fold_dir, f"Fold{fold}_History.png"))
    plt.close()

def plot_tsne(src_feats, tgt_feats, save_path):
    feats = np.vstack([src_feats, tgt_feats])
    labels = np.array([0]*len(src_feats) + [1]*len(tgt_feats))
    tsne = TSNE(n_components=2, random_state=SEED)
    feat_2d = tsne.fit_transform(feats)
    plt.figure()
    plt.scatter(feat_2d[labels==0,0], feat_2d[labels==0,1], label="Source", alpha=0.6)
    plt.scatter(feat_2d[labels==1,0], feat_2d[labels==1,1], label="Target", alpha=0.6)
    plt.legend()
    plt.title("t-SNE Source vs Target")
    plt.savefig(save_path)
    plt.close()

# -------------------------------
# Load & prepare data
# -------------------------------
src_signals, src_labels, src_rates = load_cwru_signals(SOURCE_KEY)
tgt_signals, tgt_labels, tgt_rates = load_paderborn_signals(TARGET_COND)

# -------------------------------
# Training loop (supervised DA, K-Fold)
# -------------------------------
def train_supervised_da_kfold(src_signals, src_labels,
                              tgt_signals, tgt_labels,
                              src_rates, tgt_rates,
                              interval_length=INTERVAL_LENGTH,
                              samples_per_block=SAMPLES_PER_BLOCK):
    np.random.seed(SEED)
    tf.random.set_seed(SEED)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_dir = f"Results_SupervisedDA_FromCWRUToPader_{timestamp}"
    os.makedirs(base_dir, exist_ok=True)

    # -------------------------------
    # Frequency alignment
    # -------------------------------
    target_fs = min(src_rates)
    src_signals_res = maybe_resample_list(src_signals, src_rates, target_fs)
    tgt_signals_res = maybe_resample_list(tgt_signals, tgt_rates, target_fs)
    print(f"Source sampling rates: {src_rates}")
    print(f"Target sampling rates: {tgt_rates}")

    # -------------------------------
    # Segment and balance
    # -------------------------------
    X_src, y_src = segment_signals(src_signals_res, src_labels,
                               interval_length=interval_length,
                               samples_per_block=samples_per_block)
    X_tgt, y_tgt = segment_signals(tgt_signals_res, tgt_labels,
                               interval_length=interval_length,
                               samples_per_block=samples_per_block)

    X_src, y_src = balance_after_segmentation(X_src, y_src)
    X_tgt, y_tgt = balance_after_segmentation(X_tgt, y_tgt)
    
    print("Source class distribution:", np.bincount(y_src))
    print("Target class distribution:", np.bincount(y_tgt))
    
    # print source data number
    print(f"Source samples after segmentation and balancing: {len(X_src)}")
    
    # sample fraction of target
    if USE_TARGET_FRACTION < 1.0:
        n_tgt = int(len(X_tgt)*USE_TARGET_FRACTION)
        idx = np.random.choice(len(X_tgt), n_tgt, replace=False)
        X_tgt, y_tgt = X_tgt[idx], y_tgt[idx]
    
    # print target data number
    print(f"Target samples after segmentation and sampling: {len(X_tgt)}")

    # -------------------------------
    # K-Fold Training
    # -------------------------------
    kfold = StratifiedKFold(n_splits=KFOLD, shuffle=True, random_state=SEED)
    fold = 1
    results_src, results_tgt = [], []

    for train_idx, val_idx in kfold.split(X_src, y_src):
        print(f"\n========== Fold {fold}/{KFOLD} ==========")
        Xs_train, Xs_val = X_src[train_idx], X_src[val_idx]
        ys_train, ys_val = y_src[train_idx], y_src[val_idx]

        # split target into train/test
        Xt_train, Xt_test, yt_train, yt_test = train_test_split(
            X_tgt, y_tgt, test_size=0.2, random_state=SEED+fold, stratify=y_tgt
        )

        # SAVE SAME TEST SET FOR LATER COMPARISON
        fold_dir = os.path.join(base_dir, f"Fold_{fold}")
        os.makedirs(fold_dir, exist_ok=True)
        np.save(os.path.join(fold_dir, "Xt_test_fold.npy"), Xt_test)
        np.save(os.path.join(fold_dir, "yt_test_fold.npy"), yt_test)

        # build model
        num_classes = len(np.unique(y_src))
        model = build_cnn1d(X_src.shape[1:], num_classes)

        # build once so inputs/outputs exist
        _ = model(tf.zeros((1,) + X_src.shape[1:]))

        feature_model = models.Model(
            inputs=model.inputs,
            outputs=model.layers[-3].output
        )

        optimizer = optimizers.Adam(1e-4)
        ce_loss = losses.SparseCategoricalCrossentropy()

        # early stopping setup
        best_val = 0.0
        epochs_since_improve = 0
        best_path = os.path.join(fold_dir, "best_model.weights.h5")
        history_log = []

        for ep in range(PRETRAIN_EPOCHS):
            # shuffle
            idx_s = np.random.permutation(len(Xs_train))
            idx_t = np.random.permutation(len(Xt_train))
            Xs_sh, ys_sh = Xs_train[idx_s], ys_train[idx_s]
            Xt_sh, yt_sh = Xt_train[idx_t], yt_train[idx_t]

            num_batches = max(min(len(Xs_sh), len(Xt_sh)) // BATCH_SIZE, 1)
            train_loss_accum = 0.0

            for b in range(num_batches):
                s_start, s_end = b*BATCH_SIZE, (b+1)*BATCH_SIZE
                t_start, t_end = b*BATCH_SIZE, (b+1)*BATCH_SIZE
                Xs_b, ys_b = Xs_sh[s_start:s_end], ys_sh[s_start:s_end]
                Xt_b, yt_b = Xt_sh[t_start:t_end], yt_sh[t_start:t_end]
                if len(Xs_b)==0 or len(Xt_b)==0: continue

                with tf.GradientTape() as tape:
                    logits_s = model(Xs_b, training=True)
                    
                    # If using MMD/CORAL, include target for alignment
                    if USE_MMD or USE_CORAL:
                        logits_t = model(Xt_b, training=True)
                        loss_s = ce_loss(ys_b, logits_s)
                        loss_t = ce_loss(yt_b, logits_t)
                        loss_ce = 0.5 * (loss_s + loss_t)
                        
                        align_loss = 0.0
                        if USE_MMD:
                            fs = feature_model(Xs_b)
                            ft = feature_model(Xt_b)
                            align_loss += MMD_WEIGHT * mmd_loss(fs, ft)
                        if USE_CORAL:
                            fs = feature_model(Xs_b) if not USE_MMD else fs
                            ft = feature_model(Xt_b) if not USE_MMD else ft
                            align_loss += CORAL_WEIGHT * coral_loss(fs, ft)
                        
                        loss_total = loss_ce + align_loss
                    else:
                        # Pure source training
                        loss_total = ce_loss(ys_b, logits_s)


                grads = tape.gradient(loss_total, model.trainable_variables)
                optimizer.apply_gradients(zip(grads, model.trainable_variables))
                train_loss_accum += float(loss_total.numpy())

            # source validation
            val_logits = model.predict(Xs_val, verbose=0)
            val_preds = np.argmax(val_logits, axis=1)
            print("Validation true distribution:", np.bincount(ys_val))
            print("Validation pred distribution:", np.bincount(val_preds, minlength=num_classes))
            print("Validation confusion matrix:\n", confusion_matrix(ys_val, val_preds))
            val_acc = accuracy_score(ys_val, val_preds)
            val_loss = float(np.mean(tf.keras.losses.sparse_categorical_crossentropy(ys_val, val_logits).numpy()))
            history_log.append({"epoch": ep+1, "train_loss": train_loss_accum/num_batches, "val_loss": val_loss, "val_acc": val_acc})

            if VERBOSE:
                print(f"Epoch {ep+1} | TrainLoss={train_loss_accum/num_batches:.4f} | ValAcc={val_acc:.4f}")

            # early stopping
            if val_acc > best_val:
                best_val = val_acc
                model.save_weights(best_path)
                epochs_since_improve = 0
            else:
                epochs_since_improve += 1
            if epochs_since_improve >= PATIENCE:
                print(f"Early stopping at epoch {ep+1}")
                break
            # after training finishes for this fold
            print("Best val accuracy in this fold:", best_val)
        # reload best model
        model.load_weights(best_path)

        _ = model(tf.zeros((1,) + X_src.shape[1:]))

        feature_model = models.Model(
            inputs=model.inputs,
            outputs=model.layers[-3].output
        )

        # target test metrics
        y_pred_t = np.argmax(model.predict(Xt_test), axis=1)
        results_tgt.append([
            accuracy_score(yt_test, y_pred_t),
            precision_score(yt_test, y_pred_t, average="macro", zero_division=0),
            recall_score(yt_test, y_pred_t, average="macro", zero_division=0),
            f1_score(yt_test, y_pred_t, average="macro", zero_division=0)
        ])
        plot_confusion_matrix(yt_test, y_pred_t, f"Fold {fold} Target ConfMat",
                              os.path.join(fold_dir, f"Fold{fold}_Target_ConfMat.png"))

        # source val metrics
        y_pred_s = np.argmax(model.predict(Xs_val), axis=1)
        results_src.append([
            accuracy_score(ys_val, y_pred_s),
            precision_score(ys_val, y_pred_s, average="macro", zero_division=0),
            recall_score(ys_val, y_pred_s, average="macro", zero_division=0),
            f1_score(ys_val, y_pred_s, average="macro", zero_division=0)
        ])
        plot_training_history(history_log, fold_dir, fold)

        # t-SNE last fold
        if fold == KFOLD:
            src_feats = feature_model.predict(Xs_val)
            tgt_feats = feature_model.predict(Xt_test)
            plot_tsne(src_feats, tgt_feats, os.path.join(fold_dir, "TSNE_Final.png"))

        fold += 1

    # -------------------------------
    # Save summary
    # -------------------------------
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

    save_path = os.path.join(base_dir,"Summary.xlsx")
    df.to_excel(save_path, index=False)
    print(f"Saved summary to {save_path}")

# -------------------------------
# Run training
# -------------------------------
train_supervised_da_kfold(src_signals, src_labels, tgt_signals, tgt_labels, src_rates, tgt_rates)
