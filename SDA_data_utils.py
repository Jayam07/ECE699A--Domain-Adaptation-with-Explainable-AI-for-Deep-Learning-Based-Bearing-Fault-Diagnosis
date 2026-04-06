# SDA_data_utils.py
import os
import numpy as np
import scipy.io
from scipy.signal import resample, resample_poly

# -----------------------
# CWRU datasets
# -----------------------
# DATASETS = {
#     "12K0HP": ("BearingData_CaseWestern_12K1797",
#                ['97.mat','105.mat','118.mat','130.mat','169.mat','185.mat','197.mat','209.mat','222.mat','234.mat']),
#     "12K1HP": ("BearingData_CaseWestern_12K1772",
#                ['98.mat','106.mat','119.mat','131.mat','170.mat','186.mat','198.mat','210.mat','223.mat','235.mat']),
#     "12K2HP": ("BearingData_CaseWestern_12K1750",
#                ['99.mat','107.mat','120.mat','132.mat','171.mat','187.mat','199.mat','211.mat','224.mat','236.mat']),
#     "12K3HP": ("BearingData_CaseWestern_12K1730",
#                ['100.mat','108.mat','121.mat','133.mat','172.mat','188.mat','200.mat','212.mat','225.mat','237.mat']),
#     "48K1HP": ("BearingData_CaseWestern_48K1772",
#                ['98.mat','110.mat','123.mat','136.mat','175.mat','190.mat','202.mat','214.mat','227.mat','239.mat']),
#     "48K2HP": ("BearingData_CaseWestern_48K1750",
#                ['99.mat','111.mat','124.mat','137.mat','176.mat','191.mat','203.mat','215.mat','228.mat','240.mat']),
#     "48K3HP": ("BearingData_CaseWestern_48K1730",
#                ['100.mat','112.mat','125.mat','138.mat','177.mat','192.mat','204.mat','217.mat','229.mat','241.mat'])
# }

DATASETS = {
    "12K0HP": ("/content/drive/MyDrive/BearingData_CaseWestern_12K1797",
               ['97.mat','130.mat','105.mat']),
    "12K1HP": ("/content/drive/MyDrive/BearingData_CaseWestern_12K1772",
               ['98.mat','131.mat','106.mat']),
    "12K2HP": ("/content/drive/MyDrive/BearingData_CaseWestern_12K1750",
               ['99.mat','132.mat','107.mat']),
    "12K3HP": ("/content/drive/MyDrive/BearingData_CaseWestern_12K1730",
               ['100.mat','133.mat','108.mat']),
    "48K1HP": ("/content/drive/MyDrive/BearingData_CaseWestern_48K1772",
               ['98.mat','136.mat','110.mat']),
    "48K2HP": ("/content/drive/MyDrive/BearingData_CaseWestern_48K1750",
               ['99.mat','137.mat','111.mat']),
    "48K3HP": ("/content/drive/MyDrive/BearingData_CaseWestern_48K1730",
               ['100.mat','138.mat','112.mat'])
}
# -----------------------
# Paderborn datasets
# -----------------------
PADER_CONDITIONS = {
    "Condition1": {
        "folder": "/content/drive/MyDrive/Condition1",
        "basefiles": [
            ("N15_M07_F10_K001", 0),
            ("N15_M07_F10_KA01", 1),
            ("N15_M07_F10_KI01", 2)
        ]
    },
    "Condition2": {
        "folder": "/content/drive/MyDrive/Condition2",
        "basefiles": [
            ("N15_M01_F10_K001", 0),
            ("N15_M01_F10_KA01", 1),
            ("N15_M01_F10_KI01", 2)
        ]
    }
}
# PADER_SUFFIXES = ["_1.mat", "_2.mat", "_3.mat", "_4.mat", "_5.mat"] ## ["_1.mat"] ["_1.mat", "_2.mat", "_3.mat"]
PADER_SUFFIXES = ["_1.mat", "_2.mat", "_3.mat", "_4.mat", "_5.mat"] ## ["_1.mat"] ["_1.mat", "_2.mat", "_3.mat"]
PADER_FS = 64000  # fixed sampling rate

# -----------------------
# Utilities
# -----------------------
def resample_signal_to_rate(sig, orig_rate, target_rate):
    if orig_rate == target_rate:
        return sig
    gcd = np.gcd(int(orig_rate), int(target_rate))
    up = target_rate // gcd
    down = orig_rate // gcd
    try:
        return resample_poly(sig, up, down)
    except:
        n_samples = int(len(sig) * (target_rate / orig_rate))
        return resample(sig, n_samples)

def try_get_fs_from_mat(mat):
    possible = ['fs', 'Fs', 'SAMPLE_RATE', 'samp_freq', 'sampling_rate', 'SR']
    for k in possible:
        if k in mat:
            try:
                return float(np.squeeze(mat[k]))
            except: pass
    return None

# -----------------------
# Loaders
# -----------------------
def load_cwru_signals(dataset_key):
    folder, files = DATASETS[dataset_key]
    # determine fs from key
    if "48K" in dataset_key:
        fs_default = 48000
    elif "12K" in dataset_key:
        fs_default = 12000
    else:
        fs_default = 12000  # fallback

    signals, labels, rates = [], [], []
    for i, fname in enumerate(files):
        fpath = os.path.join(folder, fname)
        if not os.path.exists(fpath):
            print(f"[Warning] Missing CWRU file: {fpath}")
            continue
        mat = scipy.io.loadmat(fpath)
        key = next((k for k in mat.keys() if 'DE_time' in k), None)
        if key is None:
            for fb in ['acceleration','DE','DE_time','data']:
                if fb in mat:
                    key = fb; break
        if key is None:
            print(f"[Warning] No DE_time in {fname}")
            continue
        sig = np.array(mat[key]).flatten()
        signals.append(sig)
        labels.append(i)
        rates.append(fs_default)
    return signals, labels, rates


def extract_paderborn_signal(filepath):
    mat = scipy.io.loadmat(filepath, struct_as_record=False, squeeze_me=True)
    field = next(k for k in mat.keys() if not k.startswith("__"))
    struct = mat[field]
    Y = getattr(struct, 'Y', None)
    if Y is None:
        for attr in dir(struct):
            if 'Y' in attr:
                Y = getattr(struct, attr)
                break
    sig = np.array(Y[6].Data).flatten() if hasattr(Y[6],'Data') else np.array(Y[-1].Data).flatten()
    return sig, struct

def load_paderborn_signals(condition_name="Condition1"):
    cfg = PADER_CONDITIONS[condition_name]
    folder = cfg["folder"]
    basefiles = cfg["basefiles"]
    signals, labels, rates = [], [], []
    for base, lbl in basefiles:
        for suf in PADER_SUFFIXES:
            fpath = os.path.join(folder, base+suf)
            if not os.path.exists(fpath):
                print(f"[Warning] Missing Paderborn file: {fpath}")
                continue
            sig, _ = extract_paderborn_signal(fpath)
            signals.append(sig)
            labels.append(lbl)
            rates.append(PADER_FS)
    return signals, labels, rates

# -----------------------
# Segmentation & balancing
# -----------------------
def sampling_blocks(data, interval_length, samples_per_block, ignore_points=0):
    adjusted_length = len(data) - 2*ignore_points
    n_blocks = max(round(adjusted_length / interval_length) - round(samples_per_block / interval_length) - 1, 0)
    split_data = np.zeros([n_blocks, samples_per_block])
    for i in range(n_blocks):
        start = ignore_points + i*interval_length
        split_data[i,:] = data[start:start+samples_per_block].T
    return split_data

def segment_signals(signals, labels, interval_length=320, samples_per_block=1600):
    X, y = [], []
    for sig, lbl in zip(signals, labels):
        seg = sampling_blocks(sig, interval_length, samples_per_block)
        if seg.shape[0]==0: continue
        X.append(seg)
        y.extend([lbl]*len(seg))
    if len(X)==0: return np.zeros((0,samples_per_block,1)), np.array([])
    X = np.vstack(X)[..., np.newaxis]
    y = np.array(y)
    return X, y

def balance_after_segmentation(X, y, seed=42):
    rng = np.random.RandomState(seed)
    classes = np.unique(y)
    counts = {c: np.sum(y==c) for c in classes}
    min_count = min(counts.values())
    X_parts, y_parts = [], []
    for c in classes:
        idx = np.where(y==c)[0]
        chosen = idx if len(idx)<=min_count else rng.choice(idx, size=min_count, replace=False)
        X_parts.append(X[chosen])
        y_parts.append(y[chosen])
    X_new = np.vstack(X_parts)
    y_new = np.concatenate(y_parts)
    perm = rng.permutation(len(y_new))
    return X_new[perm], y_new[perm]

def maybe_resample_list(signals, rates, target_rate):
    new_sigs = []
    for i, s in enumerate(signals):
        r = rates[i] if rates is not None and i<len(rates) else None
        if r is None or int(r)==int(target_rate):
            new_sigs.append(s)
        else:
            new_sigs.append(resample_signal_to_rate(s, int(r), int(target_rate)))
    return new_sigs
