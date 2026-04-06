# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 23:41:44 2024

@author: YLiu
"""

"""
import os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = ""

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Hide TensorFlow debug logs
 
import tensorflow as tf
import numpy as np
import random as rn
 
sd = 1 # Here sd means seed.
np.random.seed(sd)
rn.seed(sd)
os.environ['PYTHONHASHSEED']=str(sd)
 
from keras import backend as K
config = tf.compat.v1.ConfigProto(intra_op_parallelism_threads=1,inter_op_parallelism_threads=1)
tf.random.set_seed(sd)
# sess = tf.compat.v1.Session(graph=tf.compat.v1.get_default_graph(), config=config)
# K.set_session(sess)

# No need to manually set session in TF 2.x
tf.compat.v1.disable_eager_execution()  # Optional: Only if using old TF1 code
sess = tf.compat.v1.Session()
tf.compat.v1.keras.backend.set_session(sess)

import logging
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Hide TensorFlow debug logs
tf.debugging.set_log_device_placement(False)  # Disable device placement logs
logging.getLogger("tensorflow").setLevel(logging.ERROR)  # Suppress TensorFlow logs
"""

import tensorflow as tf
import numpy as np
import random
import os

# Set a fixed seed value for reproducibility
SEED = 1
random.seed(SEED)            # Python random module
np.random.seed(SEED)         # NumPy
tf.random.set_seed(SEED)     # TensorFlow

# Enforce deterministic behavior for GPU operations
os.environ['TF_DETERMINISTIC_OPS'] = '1'  # Ensure deterministic execution
os.environ['TF_CUDNN_DETERMINISTIC'] = '1'  # Deterministic cuDNN algorithms

# Control GPU memory allocation (prevents TensorFlow from using all GPU memory)
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)  # Enable memory growth

# Restrict parallelism (ensures consistent execution order)
tf.config.threading.set_inter_op_parallelism_threads(1)
tf.config.threading.set_intra_op_parallelism_threads(1)


## V2: modify sample numbers and data point number 
# import os
import scipy.io 
# import numpy as np
from sklearn.model_selection import train_test_split, KFold
from sklearn.metrics import confusion_matrix
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd

from sklearn.model_selection import StratifiedKFold
from scipy.signal import resample_poly

from CWRU_data import ImportData_CWRU_LHP2_12K

"""
def ImportData():
  folder_path = '../Classification_of_bearing_faults_using_ML-main/BearingData_CaseWestern' 
  # X99_normal = scipy.io.loadmat('content/drive/MyDrive/BearingData_CaseWestern/99.mat')['X099_DE_time'] 
  file_path1 = os.path.join(folder_path, '99.mat')
  X99_normal = scipy.io.loadmat(file_path1)['X099_DE_time']
    
  # X111_InnerRace_007 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/111.mat')['X111_DE_time']
  file_path2 = os.path.join(folder_path, '111.mat')
  X111_InnerRace_007  = scipy.io.loadmat(file_path2)['X111_DE_time']

  # X124_Ball_007 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/124.mat')['X124_DE_time']
  file_path3 = os.path.join(folder_path, '124.mat')
  X124_Ball_007 = scipy.io.loadmat(file_path3)['X124_DE_time']

  # X137_Outer_007 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/137.mat')['X137_DE_time']
  file_path4 = os.path.join(folder_path, '137.mat')
  X137_Outer_007 = scipy.io.loadmat(file_path4)['X137_DE_time']
    
  # X176_InnerRace_014 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/176.mat')['X176_DE_time']
  file_path5 = os.path.join(folder_path, '176.mat')
  X176_InnerRace_014 = scipy.io.loadmat(file_path5)['X176_DE_time']

  # X191_Ball_014 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/191.mat')['X191_DE_time']
  file_path6 = os.path.join(folder_path, '191.mat')
  X191_Ball_014 = scipy.io.loadmat(file_path6)['X191_DE_time']
    
  # X203_Outer_014 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/203.mat')['X203_DE_time']
  file_path7 = os.path.join(folder_path, '203.mat')
  X203_Outer_014  = scipy.io.loadmat(file_path7)['X203_DE_time']

  #  X215_InnerRace_021 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/215.mat')['X215_DE_time']
  file_path8 = os.path.join(folder_path, '215.mat')
  X215_InnerRace_021  = scipy.io.loadmat(file_path8)['X215_DE_time']
    
  # X228_Ball_021 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/228.mat')['X228_DE_time']
  file_path9 = os.path.join(folder_path, '228.mat')
  X228_Ball_021  = scipy.io.loadmat(file_path9)['X228_DE_time']

  # X240_Outer_021 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/240.mat')['X240_DE_time']
  file_path10 = os.path.join(folder_path, '240.mat')
  X240_Outer_021  = scipy.io.loadmat(file_path10)['X240_DE_time'] 
    
  return [X99_normal,X111_InnerRace_007,X124_Ball_007,X137_Outer_007,X176_InnerRace_014,X191_Ball_014,X203_Outer_014,X215_InnerRace_021,X228_Ball_021,X240_Outer_021]
"""

# def Sampling(Data, interval_length, samples_per_block):
#     No_of_blocks = (round(len(Data)/interval_length) - round(samples_per_block/interval_length) - 1)
#     SplitData = np.zeros([No_of_blocks, samples_per_block])
#     for i in range(No_of_blocks):
#         SplitData[i,:] = Data[i*interval_length:(i*interval_length)+samples_per_block].T
#     return SplitData

def Sampling(Data, interval_length, samples_per_block, ignore_points=0):
    # Adjust data length to ignore the first and last 'ignore_points'
    adjusted_length = len(Data) - 2 * ignore_points
    # Adjust the number of blocks
    No_of_blocks = (round(adjusted_length / interval_length) - round(samples_per_block / interval_length) - 1)
    SplitData = np.zeros([No_of_blocks, samples_per_block])
    
    for i in range(No_of_blocks):
        # Skip the first 'ignore_points' and start sampling from that position
        start_idx = ignore_points + i * interval_length
        SplitData[i, :] = Data[start_idx:(start_idx + samples_per_block)].T
    
    return SplitData


def DataPreparation(Data, interval_length, samples_per_block):
  for count,i in enumerate(Data):
    SplitData = Sampling(i, interval_length, samples_per_block)
    y = np.zeros([len(SplitData),10])
    y[:,count] = 1
    y1 = np.zeros([len(SplitData),1])
    y1[:,0] = count
    # Stack up and label the data   
    if count==0:
      X = SplitData
      LabelPositional = y
      Label = y1
    else:
      X = np.append(X, SplitData, axis=0)
      LabelPositional = np.append(LabelPositional,y,axis=0)
      Label = np.append(Label,y1,axis=0)
  return X, LabelPositional, Label

def resample_48K_to_12K(signal_48K):
    """
    Resample a 1D signal from 48 kHz to 12 kHz using polyphase resampling.
    Assumes signal_48k is a 1D numpy array.
    """
    # downsample by factor 4 -> up=1, down=4
    sig_12K = resample_poly(signal_48K, up=1, down=4)
    return sig_12K

# Read data files
Data = ImportData_CWRU_LHP2_12K()
# Downsample data for Normal class from 48K to 12K
data_12K = resample_48K_to_12K(Data[0])
Data[0] = data_12K

# Data = ImportData()
interval_length = 400 #290 #200  
samples_per_block = 400 #1600 #1650-2*25


# Y_CNN is of shape (n, 10) representing 10 classes as 10 columns. In each sample, for the class to which it belongs, 
# the corresponding column value is marked 1 and the rest as 0, facilitating Softmax implementation in CNN 
# Y is of shape (m, 1) where column values are between 0 and 9 representing the classes directly. - 1-hot encoding
X, Y_CNN, Y = DataPreparation(Data, interval_length, samples_per_block) 


print('Shape of Input Data =', X.shape)
print('Shape of Label Y_CNN =', Y_CNN.shape)
print('Shape of Label Y =', Y.shape)

# XX = {'X':X}
# scipy.io.savemat('Data.mat', XX)

# k-fold cross validation 
kSplits = 5
# kfold = KFold(n_splits=kSplits, random_state=42, shuffle=True)
kfold = StratifiedKFold(n_splits=kSplits, random_state=42, shuffle=True)

## 1-Dimensional Convolutional Neural Network Classification
# Reshape the data - 1 dimensional feed 
Input_1D = X.reshape([-1,samples_per_block,1])

print(Input_1D.shape)

# Test-Train Split 
X_1D_train, X_1D_test, y_1D_train, y_1D_test, y_label_train, y_label_test = train_test_split(Input_1D, Y_CNN, Y, train_size=0.8, test_size=0.2, random_state=42, stratify=Y)
# X_1D_train, X_1D_test, y_1D_train, y_1D_test = train_test_split(Input_1D, Y_CNN, train_size=0.8,test_size=0.2, random_state=42)

input_shape = (samples_per_block, 1)   # Reshaped input

"""
# Define the CNN Classification model (Setting 1)
class CNN_1D():
  def __init__(self):
    self.model = self.CreateModel()

  def CreateModel(self):
    model = models.Sequential([
        layers.Conv1D(filters=16, kernel_size=3, strides=2, activation='relu'),
        layers.MaxPool1D(pool_size=2),
        layers.Conv1D(filters=32, kernel_size=3, strides=2, activation='relu'),
        layers.MaxPool1D(pool_size=2),
        layers.Conv1D(filters=64, kernel_size=3, strides=2, activation='relu'),
        layers.MaxPool1D(pool_size=2),
        layers.Conv1D(filters=128, kernel_size=3, strides=2, activation='relu'),
        layers.MaxPool1D(pool_size=2),
        layers.Flatten(),
        layers.InputLayer(),
        layers.Dense(100,activation='relu'),
        layers.Dense(50,activation='relu'),
        layers.Dense(10),
        layers.Softmax()
        ])
    model.compile(optimizer='adam',
              loss=tf.keras.losses.CategoricalCrossentropy(),
              metrics=['accuracy'])
    return model
"""

class CNN_1D():
    def __init__(self):
        self.model = self.CreateModel()
        self.model.summary()

    def CreateModel(self):
        model = models.Sequential([
            layers.Conv1D(filters=16, kernel_size=3, strides=1, padding='same', activation='relu', input_shape=input_shape),
            layers.BatchNormalization(),
            layers.MaxPool1D(pool_size=2),
            
            layers.Conv1D(filters=32, kernel_size=3, strides=1, padding='same', activation='relu'),
            layers.BatchNormalization(),
            layers.MaxPool1D(pool_size=2),

            layers.Conv1D(filters=64, kernel_size=3, strides=1, padding='same', activation='relu'),
            layers.BatchNormalization(),
            layers.MaxPool1D(pool_size=2),

            layers.GlobalAveragePooling1D(),
            layers.Dense(64, activation='relu'),
            # layers.Dropout(0.3),
            layers.Dense(10, activation='softmax')
        ])

        # Optimizer with a slightly higher learning rate
        model.compile(optimizer='adam',
                      loss=tf.keras.losses.CategoricalCrossentropy(),
                      metrics=['accuracy'])
        return model


# foldername = "CNN1D_results/CNN1D_TS_NOL_exp2/"
foldername = "/content/drive/MyDrive/CNN1D_TS_CWRU_12K_NOL_LHP2/"
os.makedirs(foldername, exist_ok=True)
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.models import load_model


accuracy_train = []
accuracy_val = []
accuracy_test = []
pred_all_val = np.zeros([len(X_1D_train),10])
y_1D_val = np.zeros([len(X_1D_train),10])
kfold_test_len = []

k = 1
fl1 = 0

early_stop = EarlyStopping(monitor='val_accuracy', patience=50, restore_best_weights=True)

# Train the model 
# for train, test in kfold.split(X_1D_train,y_1D_train):
for fold, (train, test) in enumerate(kfold.split(X_1D_train, y_label_train)):    

  # Define where to save the best model
  checkpoint_filepath = foldername + "best_model_" + str(k) + ".h5"
  
  
  # Create a ModelCheckpoint callback
  checkpoint = ModelCheckpoint(
      filepath=checkpoint_filepath,
      monitor='val_accuracy',  # Monitor validation accuracy
      save_best_only=True,  # Save only the best model
      mode='max',  # Maximize accuracy
      verbose=1
  )        
    
  Classification_1D = CNN_1D()
  # history = Classification_1D.model.fit(X_1D_train[train], y_1D_train[train], verbose=1, epochs=50)  ## epochs=12

  history = Classification_1D.model.fit(
        X_1D_train[train], y_1D_train[train],
        validation_data=(X_1D_train[test], y_1D_train[test]),  # Validation set for monitoring
        epochs=200,
        verbose=1,
        callbacks=[checkpoint, early_stop]  # Save the best model
  )
  

  print("Best model saved at:", checkpoint_filepath)
  CNN_1D_best_model = load_model(checkpoint_filepath)
  print("Best model loaded successfully!")
  
  fl2 = fl1 + len(test)
  pred_all_val[fl1:fl2,:] = CNN_1D_best_model.predict(X_1D_train[test])
  y_1D_val[fl1:fl2,:] = y_1D_train[test]
  kfold_test_len.append(fl2-fl1)
  fl1 = fl2

  # Evaluate the accuracy of the model on the training set 
  train_loss, train_accuracy = CNN_1D_best_model.evaluate(X_1D_train[train], y_1D_train[train]) 
  accuracy_train.append(train_accuracy)

  # Evaluate the accuracy of the model on the validation set 
  val_loss, val_accuracy = CNN_1D_best_model.evaluate(X_1D_train[test], y_1D_train[test]) 
  accuracy_val.append(val_accuracy)

  # Evaluate the accuracy of the model on the test set 
  test_loss, test_accuracy = CNN_1D_best_model.evaluate(X_1D_test, y_1D_test) 
  accuracy_test.append(test_accuracy)
  
  k = k + 1


# Classification_1D.model.summary()

CNN_1D_train_accuracy = np.average(accuracy_train)*100
print('CNN 1D train accuracy =', CNN_1D_train_accuracy)
# print(accuracy_train)

CNN_1D_val_accuracy = np.average(accuracy_val)*100
print('CNN 1D validation accuracy =', CNN_1D_val_accuracy)
# print(accuracy_val)

CNN_1D_test_accuracy = np.average(accuracy_test)*100
print('CNN 1D test accuracy =', CNN_1D_test_accuracy)
# print(accuracy_test)

"""
# Ensemble Classifier
k = 1
checkpoint_filepath = foldername + "best_model_" + str(k) + ".h5"
model1 = load_model(checkpoint_filepath)
pred1 = model1.predict(X_1D_test)
pred_label1 = np.argmax(pred1, axis=1)
pred1_trn = model1.predict(X_1D_train)
pred_label1_trn = np.argmax(pred1_trn, axis=1)
k = 2
checkpoint_filepath = foldername + "best_model_" + str(k) + ".h5"
model2 = load_model(checkpoint_filepath)
pred2 = model2.predict(X_1D_test)
pred_label2 = np.argmax(pred2, axis=1)
pred2_trn = model2.predict(X_1D_train)
pred_label2_trn = np.argmax(pred2_trn, axis=1)
k = 3
checkpoint_filepath = foldername + "best_model_" + str(k) + ".h5"
model3 = load_model(checkpoint_filepath)
pred3 = model3.predict(X_1D_test)
pred_label3 = np.argmax(pred3, axis=1)
pred3_trn = model3.predict(X_1D_train)
pred_label3_trn = np.argmax(pred3_trn, axis=1)
k = 4
checkpoint_filepath = foldername + "best_model_" + str(k) + ".h5"
model4 = load_model(checkpoint_filepath)
pred4 = model4.predict(X_1D_test)
pred_label4 = np.argmax(pred4, axis=1)
pred4_trn = model4.predict(X_1D_train)
pred_label4_trn = np.argmax(pred4_trn, axis=1)
k = 5
checkpoint_filepath = foldername + "best_model_" + str(k) + ".h5"
model5 = load_model(checkpoint_filepath)
pred5 = model5.predict(X_1D_test)
pred_label5 = np.argmax(pred5, axis=1)
pred5_trn = model5.predict(X_1D_train)
pred_label5_trn = np.argmax(pred5_trn, axis=1)

target_label = np.argmax(y_1D_test, axis=1)
target_label_trn = np.argmax(y_1D_train, axis=1)

predictions = np.column_stack((pred_label1, pred_label2, pred_label3, pred_label4, pred_label5, target_label))
pred_trn = np.column_stack((pred_label1_trn, pred_label2_trn, pred_label3_trn, pred_label4_trn, pred_label5_trn, target_label_trn))
pred = np.column_stack((pred1, pred2, pred3, pred4, pred5, y_1D_test))
pred_trn = np.column_stack((pred1_trn, pred2_trn, pred3_trn, pred4_trn, pred5_trn, y_1D_train))
pred_val = np.column_stack((pred_all_val, y_1D_val))
# np.savetxt("pred_CNN1D_V4_bm.csv", predictions, delimiter=",", fmt="%d")
# np.savetxt("pred_trn_CNN1D_V4_bm.csv", pred_trn, delimiter=",", fmt="%d")
np.savetxt("yp_CNN1D_V4_bm.csv", pred, delimiter=",", fmt="%.8e")
np.savetxt("yp_trn_CNN1D_V4_bm.csv", pred_trn, delimiter=",", fmt="%.8e")
# np.savetxt("yp_val_CNN1D_V4_bm.csv", pred_val, delimiter=",", fmt="%.8e")
# np.savetxt("kfold_CNN1D_V4_bm.csv", kfold_test_len, delimiter=",", fmt="%d")
# print("Predictions saved successfully to 'pred_CNN1D_V4_bm.csv'")

# Evaluate the accuracy of the model on the test set
# CNN_1D_test_loss, CNN_1D_test_accuracy = Classification_1D.model.evaluate(X_1D_test, y_1D_test)
# CNN_1D_test_accuracy*=100
# print('CNN 1D test accuracy =', CNN_1D_test_accuracy)
"""

# Confusion Matrix Calculation
def ConfusionMatrix(Model, X, y):
  y_pred = np.argmax(Model.predict(X), axis=1)
  ConfusionMat = confusion_matrix(np.argmax(y, axis=1), y_pred)
  return ConfusionMat

#Plot results - CNN 1D
plt.figure(1)
plt.title('Confusion Matrix - CNN 1D Train') 
sns.heatmap(ConfusionMatrix(CNN_1D_best_model, X_1D_train, y_1D_train),
            annot=True, fmt='d', annot_kws={"fontsize":8}, cmap="YlGnBu")

plt.savefig(foldername + "confusion_matrix_train.png", dpi=300)
plt.show()

plt.figure(2)
plt.title('Confusion Matrix - CNN 1D Test') 
sns.heatmap(ConfusionMatrix(CNN_1D_best_model, X_1D_test, y_1D_test),
            annot=True, fmt='d', annot_kws={"fontsize":8}, cmap="YlGnBu")

plt.savefig(foldername + "confusion_matrix_test.png", dpi=300)
plt.show()

plt.figure(3)
plt.title('Train - Accuracy - CNN 1D')
plt.bar(np.arange(1,kSplits+1),[i*100 for i in accuracy_val])
plt.ylabel('accuracy')
plt.xlabel('folds')
plt.ylim([70,100])
plt.show()

plt.figure(4)
plt.title('Train vs Test Accuracy - CNN 1D')
plt.bar([1,2],[CNN_1D_train_accuracy,CNN_1D_test_accuracy])
plt.ylabel('accuracy')
plt.xlabel('folds')
plt.xticks([1,2],['Train', 'Test'])
plt.ylim([70,100])
plt.show()

# ==========================================
# ROBUST 1D Grad-CAM for CNN_1D_best_model
# ==========================================

import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# ------------------------------------------
# 0) Save folder
# ------------------------------------------
gradcam_dir = os.path.join(foldername, "gradcam_results")
os.makedirs(gradcam_dir, exist_ok=True)

# ------------------------------------------
# 1) Find last Conv1D layer
# ------------------------------------------
def get_last_conv1d_layer_name(model):
    for layer in reversed(model.layers):
        if isinstance(layer, tf.keras.layers.Conv1D):
            return layer.name
    raise ValueError("No Conv1D layer found in model.")

LAST_CONV_LAYER = get_last_conv1d_layer_name(CNN_1D_best_model)
print("Using last Conv1D layer:", LAST_CONV_LAYER)

# ------------------------------------------
# 2) Build models for Grad-CAM
# ------------------------------------------
last_conv_layer = CNN_1D_best_model.get_layer(LAST_CONV_LAYER)

# Model from input -> last conv output
conv_model = tf.keras.Model(
    inputs=CNN_1D_best_model.inputs,
    outputs=last_conv_layer.output
)

# Classifier head: from last conv output -> final prediction
classifier_input = tf.keras.Input(shape=last_conv_layer.output.shape[1:])

x = classifier_input
start_collecting = False
for layer in CNN_1D_best_model.layers:
    if layer.name == LAST_CONV_LAYER:
        start_collecting = True
        continue
    if start_collecting:
        x = layer(x)

classifier_model = tf.keras.Model(classifier_input, x)

# ------------------------------------------
# 3) Compute 1D Grad-CAM
# ------------------------------------------
def compute_gradcam_1d(sample, class_idx=None):
    """
    sample: shape (1, T, 1)
    returns:
        heatmap_resized: shape (T,)
        pred_class: int
    """
    sample_tensor = tf.cast(sample, tf.float32)

    with tf.GradientTape() as tape:
        conv_outputs = conv_model(sample_tensor, training=False)
        tape.watch(conv_outputs)

        preds = classifier_model(conv_outputs, training=False)

        if class_idx is None:
            class_idx = int(tf.argmax(preds[0]))
        else:
            class_idx = int(class_idx)

        loss = preds[:, class_idx]

    grads = tape.gradient(loss, conv_outputs)

    if grads is None:
        raise ValueError("Gradients are None. Grad-CAM could not be computed.")

    # conv_outputs: (1, T_conv, C)
    # grads:        (1, T_conv, C)

    conv_outputs = conv_outputs[0]   # (T_conv, C)
    grads = grads[0]                 # (T_conv, C)

    # Global average pooling over time dimension
    pooled_grads = tf.reduce_mean(grads, axis=0)   # (C,)

    # Weighted sum of feature maps
    heatmap = tf.reduce_sum(conv_outputs * pooled_grads, axis=-1)   # (T_conv,)

    # ReLU
    heatmap = tf.maximum(heatmap, 0)

    # Normalize
    heatmap = heatmap / (tf.reduce_max(heatmap) + 1e-9)
    heatmap = heatmap.numpy()

    # Resize to original signal length
    T_original = sample.shape[1]
    T_conv = len(heatmap)
    x_old = np.linspace(0, 1, T_conv)
    x_new = np.linspace(0, 1, T_original)
    heatmap_resized = np.interp(x_new, x_old, heatmap)

    return heatmap_resized, class_idx

# ------------------------------------------
# 4) Plot function
# ------------------------------------------
def plot_gradcam_1d(signal_1d, heatmap, true_label, pred_label, save_path, title):
    T = len(signal_1d)
    x = np.arange(T)

    fig, axes = plt.subplots(3, 1, figsize=(12, 8), sharex=True)

    # Original signal
    axes[0].plot(x, signal_1d, linewidth=1)
    axes[0].set_title(f"{title}\nTrue={true_label}, Pred={pred_label}")
    axes[0].set_ylabel("Amplitude")
    axes[0].grid(True, alpha=0.3)

    # Grad-CAM band
    im = axes[1].imshow(
        heatmap.reshape(1, -1),
        aspect='auto',
        cmap='jet',
        extent=[0, T, 0, 1]
    )
    axes[1].set_yticks([])
    axes[1].set_title("Grad-CAM Attention")
    plt.colorbar(im, ax=axes[1], fraction=0.02, pad=0.02)

    # Overlay
    ymin, ymax = signal_1d.min(), signal_1d.max()
    axes[2].plot(x, signal_1d, color='black', linewidth=1, alpha=0.85)
    axes[2].imshow(
        heatmap.reshape(1, -1),
        aspect='auto',
        cmap='jet',
        alpha=0.35,
        extent=[0, T, ymin, ymax]
    )
    axes[2].set_title("Signal + Grad-CAM Overlay")
    axes[2].set_xlabel("Time Index")
    axes[2].set_ylabel("Amplitude")
    axes[2].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.show()
    print("Saved:", save_path)

# ------------------------------------------
# 5) Predictions on test set
# ------------------------------------------
y_true = np.argmax(y_1D_test, axis=1)
pred_probs = CNN_1D_best_model.predict(X_1D_test, verbose=0)
y_pred = np.argmax(pred_probs, axis=1)

correct_idx = np.where(y_pred == y_true)[0]
wrong_idx = np.where(y_pred != y_true)[0]

print("Correct samples:", len(correct_idx))
print("Misclassified samples:", len(wrong_idx))

# ------------------------------------------
# 6) Generate MULTIPLE Grad-CAM examples
# ------------------------------------------
N_PER_CLASS = 3   # change to 5 if you want more
print("Generating multiple Grad-CAM examples per class...")

classes = np.unique(y_true)

for cls in classes:
    cls = int(cls)

    # correct samples of this class
    cls_correct_idx = np.where((y_true == cls) & (y_pred == cls))[0][:N_PER_CLASS]

    # misclassified samples whose true class is this class
    cls_wrong_idx = np.where((y_true == cls) & (y_pred != cls))[0][:N_PER_CLASS]

    # folders
    correct_cls_dir = os.path.join(gradcam_dir, f"class_{cls}", "correct")
    wrong_cls_dir = os.path.join(gradcam_dir, f"class_{cls}", "misclassified")
    os.makedirs(correct_cls_dir, exist_ok=True)
    os.makedirs(wrong_cls_dir, exist_ok=True)

    # -----------------------
    # Correct examples
    # -----------------------
    for j, idx_c in enumerate(cls_correct_idx):
        idx_c = int(idx_c)
        sample_c = X_1D_test[idx_c:idx_c+1]
        signal_c = sample_c[0, :, 0]
        true_c = int(y_true[idx_c])
        pred_c = int(y_pred[idx_c])

        heatmap_c, _ = compute_gradcam_1d(sample_c, class_idx=pred_c)

        save_c = os.path.join(
            correct_cls_dir,
            f"gradcam_correct_idx{idx_c}_true{true_c}_pred{pred_c}_{j+1}.png"
        )
        plot_gradcam_1d(
            signal_c, heatmap_c, true_c, pred_c, save_c,
            f"Correct Sample | Class {cls}"
        )

    # -----------------------
    # Misclassified examples
    # -----------------------
    for j, idx_w in enumerate(cls_wrong_idx):
        idx_w = int(idx_w)
        sample_w = X_1D_test[idx_w:idx_w+1]
        signal_w = sample_w[0, :, 0]
        true_w = int(y_true[idx_w])
        pred_w = int(y_pred[idx_w])

        heatmap_w, _ = compute_gradcam_1d(sample_w, class_idx=pred_w)

        save_w = os.path.join(
            wrong_cls_dir,
            f"gradcam_wrong_idx{idx_w}_true{true_w}_pred{pred_w}_{j+1}.png"
        )
        plot_gradcam_1d(
            signal_w, heatmap_w, true_w, pred_w, save_w,
            f"Misclassified Sample | True Class {cls}"
        )

print("Multiple Grad-CAM generation completed.")