# Code File Documentation

This section explains the purpose of each Python file in the project. The goal is to make it clear which file should be used for data loading, baseline training, supervised domain adaptation, unsupervised domain adaptation, and explainability analysis.

---

## 1. Data Loading and Preprocessing Files

### `CWRU_data.py`

**Purpose:**  
This file contains dataset-specific loading functions for the CWRU and Paderborn datasets.

**Main role in the project:**  
It acts as a raw data loading module. Other training scripts call functions from this file to import vibration signals for different load and sampling-frequency conditions.

**Main functions included:**
- `ImportData_PD_Condition1()`
- `ImportData_CWRU_LHP0_12K()`
- `ImportData_CWRU_LHP1_12K()`
- `ImportData_CWRU_LHP2_12K()`
- `ImportData_CWRU_LHP3_12K()`
- `ImportData_CWRU_LHP0_48K()`
- `ImportData_CWRU_LHP1_48K()`
- `ImportData_CWRU_LHP2_48K()`
- `ImportData_CWRU_LHP3_48K()`

**What it does:**
- Loads CWRU vibration data for different load conditions.
- Loads 12 kHz and 48 kHz drive-end vibration signals.
- Loads Paderborn Condition 1 data.
- Returns class-wise vibration signals for model training and testing.

**Used for:**
- Baseline CNN experiments.
- CWRU-to-CWRU experiments.
- CWRU-to-Paderborn experiments.

---

### `SDA_data_utils.py`

**Purpose:**  
General data utility file for supervised domain adaptation experiments.

**Main role in the project:**  
This file provides reusable preprocessing functions for loading CWRU and Paderborn data, resampling, segmenting, balancing, and preparing data for CNN models.

**Main components:**
- `DATASETS`
- `PADER_CONDITIONS`
- `PADER_SUFFIXES`
- `PADER_FS`

**Main functions:**
- `load_cwru_signals(dataset_key)`
- `load_paderborn_signals(condition_name)`
- `extract_paderborn_signal(filepath)`
- `try_get_fs_from_mat(mat)`
- `resample_signal_to_rate(sig, orig_rate, target_rate)`
- `maybe_resample_list(signals, rates, target_rate)`
- `sampling_blocks(data, interval_length, samples_per_block)`
- `segment_signals(signals, labels, interval_length, samples_per_block)`
- `balance_after_segmentation(X, y)`

**What it does:**
- Loads source-domain CWRU signals using a dataset key such as `12K1HP`, `12K2HP`, or `48K1HP`.
- Loads target-domain Paderborn signals using a condition name such as `Condition1`.
- Extracts vibration signals from `.mat` files.
- Resamples signals when source and target sampling frequencies differ.
- Segments continuous vibration signals into fixed-length windows.
- Balances the number of samples per class after segmentation.

**Used for:**
- Modular SDA training scripts.
- UDA training scripts.
- Cross-dataset CWRU-to-Paderborn experiments.

---

### `SDA_data_utils_cwru.py`

**Purpose:**  
CWRU-focused version of the SDA data utility file.

**Main role in the project:**  
This file is similar to `SDA_data_utils.py`, but it is configured for experiments that rely more heavily on CWRU data and multiple Paderborn file suffixes.

**Difference from `SDA_data_utils.py`:**
- Uses multiple Paderborn suffixes:
  - `_1.mat`
  - `_2.mat`
  - `_3.mat`
  - `_4.mat`
  - `_5.mat`

**What it does:**
- Loads multiple recordings from Paderborn for a given condition.
- Loads CWRU source and target datasets.
- Performs resampling, segmentation, and balancing.
- Helps increase the target-domain data coverage when using Paderborn.

**Used for:**
- CWRU-to-Paderborn training variants.
- More complete Paderborn target-domain experiments.

---

## 2. Baseline CNN Files

### `CNN1D_TS_CWRU_12K_NOL.py`

**Purpose:**  
Baseline 1D CNN training script for CWRU 12 kHz time-series data.

**Main role in the project:**  
This file trains a standard 1D CNN without domain adaptation.

**Main functions/classes:**
- `ImportData()`
- `Sampling()`
- `DataPreparation()`
- `resample_48K_to_12K()`
- `CNN_1D`
- `ConfusionMatrix()`

**What it does:**
- Loads CWRU vibration signals.
- Segments raw time-series signals into fixed-length samples.
- Trains a 1D CNN model on CWRU data.
- Evaluates the model using accuracy and confusion matrix.
- Acts as a baseline for comparing domain adaptation methods.

**Used for:**
- Same-domain CWRU performance.
- Initial baseline performance before SDA/UDA.

---

### `CNN1D_TS_CWRU_12K_NOL_f.py`

**Purpose:**  
Enhanced baseline 1D CNN script with Grad-CAM support.

**Main role in the project:**  
This file extends the baseline 1D CNN experiment by adding explainability functions.

**Additional functions compared to the basic version:**
- `get_last_conv1d_layer_name(model)`
- `compute_gradcam_1d(sample, class_idx)`
- `plot_gradcam_1d(signal_1d, heatmap, true_label, pred_label, save_path, title)`

**What it does:**
- Trains or loads a 1D CNN baseline model.
- Computes Grad-CAM heatmaps for 1D vibration signals.
- Visualizes important time regions used by the CNN for prediction.
- Helps compare correct and misclassified samples.

**Used for:**
- Baseline Grad-CAM analysis.
- Understanding which signal regions influence baseline predictions.

---

### `CNN1D_TS_CWRU_12K_NOL_test.py`

**Purpose:**  
Testing script for the baseline 1D CNN.

**Main role in the project:**  
This file evaluates a trained 1D CNN model on test data.

**What it does:**
- Loads test data.
- Uses the trained CNN model for prediction.
- Computes evaluation metrics.
- Generates confusion matrix.

**Used for:**
- Independent testing of baseline 1D CNN.
- Checking model performance after training.

---

### `CNN1D_TS_CWRU_12K_NOL_test_f.py`

**Purpose:**  
Testing and Grad-CAM script for the baseline 1D CNN.

**Main role in the project:**  
This file evaluates the trained baseline 1D CNN and generates Grad-CAM explanations.

**What it does:**
- Loads trained 1D CNN model.
- Tests it on selected samples.
- Computes Grad-CAM for predicted or true classes.
- Saves Grad-CAM plots.

**Used for:**
- Explainability analysis of baseline 1D CNN.
- Correct vs misclassified sample interpretation.

---

### `CNN2D_TS_CWRU_12K_NOL.py`

**Purpose:**  
Baseline 2D CNN training script for CWRU data.

**Main role in the project:**  
This file trains a 2D CNN using image-like or spectrogram-like representations of vibration signals.

**Main functions/classes:**
- `ImportData()`
- `Sampling()`
- `DataPreparation()`
- `min_max_norm()`
- `generate_spectrogram_image()`
- `resample_48K_to_12K()`
- `CNN_2D`
- `ConfusionMatrix()`

**What it does:**
- Loads CWRU vibration signals.
- Converts signal segments into 2D image-like representations.
- Normalizes data.
- Trains a 2D CNN model.
- Evaluates performance using confusion matrix and accuracy.

**Used for:**
- Baseline 2D CNN comparison with 1D CNN.
- Spectrogram/image-based fault classification.

---

### `CNN2D_TS_CWRU_12K_NOL_test.py`

**Purpose:**  
Testing script for baseline 2D CNN.

**Main role in the project:**  
This file evaluates a trained 2D CNN model on test data.

**What it does:**
- Loads or prepares 2D test samples.
- Runs prediction using trained 2D CNN.
- Computes accuracy and confusion matrix.

**Used for:**
- Baseline 2D CNN evaluation.
- Comparison with domain-adapted 2D CNN models.

---

## 3. Supervised Domain Adaptation: Full Standalone Scripts

These files are standalone scripts. Each script contains its own data loading, preprocessing, model definition, MMD/CORAL loss functions, training loop, evaluation, and visualization.

---

### `SDA_Balanced_Case1_MMD_DeepCoral_1DCNN_CWRU_Full.py`

**Purpose:**  
Full supervised domain adaptation pipeline for 1D CNN on CWRU data.

**Experiment configuration:**
- Source: `12K1HP`
- Target: `12K2HP`
- Model: 1D CNN
- Adaptation: MMD and/or CORAL
- Default: `MMD_WEIGHT = 0.1`, `CORAL_WEIGHT = 0.0`
- K-fold: 5

**What it does:**
- Loads source and target CWRU signals.
- Resamples signals when needed.
- Segments signals into windows.
- Balances source and target classes.
- Builds a 1D CNN classifier.
- Trains using:
  - supervised classification loss
  - MMD loss
  - CORAL loss if enabled
- Performs k-fold training.
- Evaluates source and target performance.
- Saves confusion matrices.
- Saves t-SNE feature visualizations.
- Saves training history.

**Used for:**
- Main 1D CNN supervised domain adaptation experiment.
- Cross-load CWRU-to-CWRU adaptation.

---

### `SDA_Balanced_Case1_MMD_DeepCoral_2DCNN_CWRU_Full.py`

**Purpose:**  
Full supervised domain adaptation pipeline for 2D CNN on CWRU data.

**Experiment configuration:**
- Source: `12K1HP`
- Target: `12K2HP`
- Model: 2D CNN
- Input: 2D reshaped blocks from vibration signals
- Adaptation: MMD and/or CORAL
- K-fold: 5

**What it does:**
- Loads source and target CWRU data.
- Segments signals into blocks.
- Reshapes each 1D segment into a 2D representation.
- Builds a 2D CNN.
- Trains the 2D CNN using supervised domain adaptation.
- Applies MMD/CORAL alignment between source and target feature distributions.
- Evaluates source and target test performance.
- Saves confusion matrices and t-SNE plots.

**Used for:**
- Main 2D CNN supervised domain adaptation experiment.
- Comparing 1D vs 2D CNN feature learning.

---

### `SDA_12K1HP_12K3HP_2nd.py`

**Purpose:**  
1D CNN supervised domain adaptation for cross-load CWRU experiment.

**Experiment configuration:**
- Source: `12K1HP`
- Target: `12K3HP`
- Model: 1D CNN
- Domain shift type: load-condition shift

**What it does:**
- Trains on CWRU 12 kHz, 1HP data.
- Adapts to CWRU 12 kHz, 3HP data.
- Uses MMD/CORAL to reduce load-induced distribution shift.
- Evaluates target-domain accuracy.
- Saves plots and metrics.

**Used for:**
- Testing whether the model generalizes from one load condition to another within CWRU.

---

### `SDA_12K1HP_48K1HP_2nd.py`

**Purpose:**  
1D CNN supervised domain adaptation for cross-frequency CWRU experiment.

**Experiment configuration:**
- Source: `12K1HP`
- Target: `48K1HP`
- Model: 1D CNN
- Domain shift type: sampling-frequency shift

**What it does:**
- Uses 12 kHz CWRU data as source.
- Uses 48 kHz CWRU data as target.
- Resamples 48 kHz data where required.
- Trains using classification + MMD/CORAL alignment.
- Evaluates how well the model transfers across sampling frequency.

**Used for:**
- Studying domain shift caused by different acquisition frequencies.

---

### `SDA_2DCNN_12K1HP_12K3HP.py`

**Purpose:**  
2D CNN supervised domain adaptation for CWRU cross-load experiment.

**Experiment configuration:**
- Source: `12K1HP`
- Target: `12K3HP`
- Model: 2D CNN
- Domain shift type: load-condition shift

**What it does:**
- Loads source and target vibration signals.
- Segments and reshapes them into 2D blocks.
- Builds a 2D CNN model.
- Applies supervised domain adaptation with MMD/CORAL.
- Evaluates performance across load conditions.

**Used for:**
- 2D CNN version of cross-load SDA.

---

### `SDA_2DCNN_12K1HP_48K1HP.py`

**Purpose:**  
2D CNN supervised domain adaptation for CWRU cross-frequency experiment.

**Experiment configuration:**
- Source: `12K1HP`
- Target: `48K1HP`
- Model: 2D CNN
- Domain shift type: sampling-frequency shift

**What it does:**
- Loads 12 kHz source and 48 kHz target data.
- Resamples target data to match source frequency.
- Converts segmented data into 2D blocks.
- Trains 2D CNN using MMD/CORAL-based adaptation.
- Evaluates target-domain accuracy.

**Used for:**
- 2D CNN cross-frequency domain adaptation.

---

### `CWRU_PADERBORN_3CLASS_12K1HP_C1.py`

**Purpose:**  
Cross-dataset domain adaptation from CWRU to Paderborn.

**Experiment configuration:**
- Source: CWRU `12K1HP`
- Target: Paderborn `Condition1`
- Classes: 3 classes
  - Normal
  - Inner race fault
  - Outer race fault
- Model: 1D CNN style SDA pipeline
- Adaptation: MMD and/or CORAL

**What it does:**
- Loads CWRU source data and Paderborn target data.
- Converts both datasets into a compatible 3-class problem.
- Segments source and target signals.
- Applies supervised domain adaptation.
- Evaluates how well the model transfers from CWRU to Paderborn.
- Saves confusion matrices, t-SNE plots, and training history.

**Used for:**
- Main cross-dataset experiment between two real benchmark datasets.

---

## 4. Modular Supervised Domain Adaptation Training Scripts

These files use reusable utilities such as `SDA_data_utils.py` and `SDA_model_utils.py`. They are cleaner and more modular than the standalone scripts.

---

### `SDA_model_utils.py`

**Purpose:**  
Model and loss utility file for SDA experiments.

**Main functions/classes:**
- `build_cnn1d(input_shape, num_classes)`
- `build_cnn2d(input_shape, num_classes)`
- `mmd_loss(source_features, target_features)`
- `coral_loss(source, target)`
- `DAModel(tf.keras.Model)`

**What it does:**
- Defines reusable 1D CNN architecture.
- Defines reusable 2D CNN architecture.
- Implements MMD loss for distribution alignment.
- Implements CORAL loss for covariance alignment.
- Provides a custom domain adaptation model class.

**Used for:**
- Modular 1D/2D SDA training scripts.
- Avoiding repeated model and loss definitions across files.

---

### `SDA_train_1DCNN.py`

**Purpose:**  
General modular 1D CNN SDA training script.

**Experiment configuration:**
- Source: `12K2HP`
- Target: `Condition1`
- Model: 1D CNN
- Adaptation: MMD/CORAL
- K-fold: 5

**What it does:**
- Uses `SDA_data_utils.py` for loading CWRU and Paderborn.
- Uses `SDA_model_utils.py` for model and loss functions.
- Trains 1D CNN under supervised domain adaptation.
- Evaluates source and target domains.
- Saves confusion matrices, training plots, and t-SNE visualizations.

**Used for:**
- General reusable 1D CNN SDA experiments.

---

### `SDA_train_1DCNN_cwru.py`

**Purpose:**  
Modular 1D CNN SDA script for CWRU-to-CWRU adaptation.

**Experiment configuration:**
- Source: `12K1HP`
- Target: `12K2HP`
- K-fold: 3
- Model: 1D CNN

**What it does:**
- Trains on one CWRU load condition.
- Adapts to another CWRU load condition.
- Uses MMD/CORAL alignment.
- Evaluates cross-load CWRU transfer.

**Used for:**
- Smaller/faster CWRU-to-CWRU SDA test.

---

### `SDA_train_1DCNN_2hp_1hp.py`

**Purpose:**  
CWRU cross-load experiment from 2HP to 1HP.

**Experiment configuration:**
- Source: `12K2HP`
- Target: `12K1HP`
- Model: 1D CNN

**What it does:**
- Trains model using 2HP source-domain signals.
- Tests/adapts to 1HP target-domain signals.
- Applies MMD/CORAL to align features.
- Measures robustness under load variation.

**Used for:**
- Cross-load adaptation in reverse direction.

---

### `SDA_train_1DCNN_13k.py`

**Purpose:**  
CWRU cross-load experiment from 1HP to 3HP.

**Experiment configuration:**
- Source: `12K1HP`
- Target: `12K3HP`
- Model: 1D CNN

**What it does:**
- Loads 12K 1HP data as source.
- Loads 12K 3HP data as target.
- Trains with supervised domain adaptation.
- Evaluates adaptation across load conditions.

**Used for:**
- CWRU 1HP to 3HP domain adaptation.

---

### `SDA_train_1DCNN_1481K.py`

**Purpose:**  
CWRU cross-frequency experiment from 12K 1HP to 48K 1HP.

**Experiment configuration:**
- Source: `12K1HP`
- Target: `48K1HP`
- Model: 1D CNN

**What it does:**
- Loads source and target CWRU data with different sampling frequencies.
- Performs resampling where needed.
- Trains with MMD/CORAL adaptation.
- Evaluates target-domain performance.

**Used for:**
- Testing adaptation when sampling frequency changes.

---

### `SDA_train_1DCNN_12k1hp_pa.py`

**Purpose:**  
CWRU-to-Paderborn modular 1D CNN SDA experiment.

**Experiment configuration:**
- Source: CWRU `12K1HP`
- Target: Paderborn `Condition1`
- Model: 1D CNN
- MMD weight: 0.5

**What it does:**
- Loads CWRU source data.
- Loads Paderborn target data.
- Segments and balances samples.
- Trains 1D CNN using supervised domain adaptation.
- Evaluates cross-dataset transfer performance.

**Used for:**
- Main modular CWRU-to-Paderborn 1D CNN adaptation experiment.

---

### `SDA_train_1DCNN_DEMO.py`

**Purpose:**  
Demonstration/debugging script for 1D CNN SDA.

**Experiment configuration:**
- Source: `12K2HP`
- Target: `Condition1`
- Model: 1D CNN

**What it does:**
- Runs a simplified SDA experiment.
- Useful for checking whether data loading, segmentation, model training, and evaluation work correctly.
- Can be used before running larger full experiments.

**Used for:**
- Debugging.
- Quick demonstration.
- Testing pipeline correctness.

---

### `SDA_train_2DCNN.py`

**Purpose:**  
General modular 2D CNN SDA training script.

**Experiment configuration:**
- Source: `12K2HP`
- Target: `Condition2`
- Model: 2D CNN
- MMD weight: 0.1
- CORAL weight: 0.1

**What it does:**
- Loads source CWRU data and target Paderborn data.
- Segments vibration signals.
- Converts 1D signal windows into 2D blocks.
- Trains 2D CNN using supervised domain adaptation.
- Applies MMD and CORAL to align source and target features.
- Evaluates source and target accuracy.
- Saves confusion matrix, t-SNE, and training history.

**Used for:**
- General 2D CNN supervised domain adaptation experiment.

---

## 5. Explainability and XAI File

### `Finalsda_gradshap.py`

**Purpose:**  
Main explainability file for Grad-CAM and SHAP analysis on SDA-trained models.

**Experiment configuration:**
- Source: `12K1HP`
- Target: `12K2HP`
- Model: 1D CNN
- Adaptation: MMD/CORAL
- XAI: Grad-CAM and SHAP

**Main functions:**
- `compute_gradcam_1d()`
- `resize_cam_to_signal()`
- `save_gradcam_plot_1d()`
- `generate_gradcam_examples()`
- `get_single_sample_shap_1d()`
- `save_shap_signal_plot_1d()`
- `generate_shap_examples()`
- `save_shap_summary()`

**What it does:**
- Trains or loads SDA model.
- Applies Grad-CAM to selected samples.
- Applies SHAP to selected samples.
- Saves Grad-CAM visualizations for each class.
- Saves SHAP signal-level importance plots.
- Generates SHAP summary plots.
- Helps compare:
  - correct vs incorrect predictions
  - baseline vs adapted behavior
  - source vs target feature importance

**Used for:**
- Explainable AI results in the report.
- Understanding why a model predicts a class.
- Identifying important signal regions.
- Failure analysis of misclassified samples.

---

## 6. Unsupervised Domain Adaptation Files

### `UDA_model_2dcnn_mmd_coral.py`

**Purpose:**  
Model utility file for unsupervised domain adaptation using 2D CNN.

**Main functions:**
- `build_feature_extractor(input_shape, feature_dim=128)`
- `build_classifier(feature_dim, num_classes)`
- `mmd_loss(source, target)`
- `coral_loss(source, target)`

**What it does:**
- Defines the 2D CNN feature extractor.
- Defines the classifier head.
- Implements MMD loss for source-target distribution alignment.
- Implements CORAL loss for covariance alignment.
- Separates feature extraction and classification so that UDA training can align features before classification.

**Used for:**
- UDA 2D CNN training.
- Grad-CAM/SHAP explanation after combining feature extractor and classifier.

---

### `UDA_train_2DCNN.py`

**Purpose:**  
Modular unsupervised domain adaptation training script for 2D CNN.

**Experiment configuration:**
- Source: `12K2HP`
- Target: `Condition1`
- Model: 2D CNN
- MMD weight: 0.1
- CORAL weight: 0.1
- K-fold: 2

**What it does:**
- Loads labeled CWRU source data.
- Loads unlabeled or partially used Paderborn target data for adaptation.
- Resamples source/target signals to a common sampling frequency.
- Segments vibration signals.
- Converts segments into 2D blocks.
- Trains feature extractor and classifier jointly.
- Uses:
  - classification loss on labeled source data
  - MMD loss between source and target features
  - CORAL loss between source and target features
- Saves:
  - `feat.weights.h5`
  - `clf.weights.h5`
  - source confusion matrix
  - target confusion matrix
  - source t-SNE
  - target t-SNE
  - domain t-SNE
  - summary spreadsheet

**Used for:**
- UDA experiments where target labels are not used for training.
- Extension of the project from SDA to UDA.

---

### `UDA_Balanced_Case1_MMD_DeepCoral_2DCNN_CWRU_Full.py`

**Purpose:**  
Standalone unsupervised domain adaptation script for 2D CNN on CWRU.

**Experiment configuration:**
- Source: `12K2HP`
- Target: `48K2HP`
- Model: 2D CNN
- MMD weight: 0.1
- CORAL weight: 0.1
- K-fold: 5

**What it does:**
- Loads CWRU source and target domains.
- Uses source labels for classification training.
- Does not use target labels during adaptation.
- Aligns source and target feature distributions using MMD and CORAL.
- Converts segmented vibration signals into 2D blocks.
- Trains a 2D CNN model.
- Evaluates on source and target domains.
- Saves confusion matrices, t-SNE plots, and performance metrics.

**Used for:**
- CWRU-to-CWRU unsupervised domain adaptation.
- Comparing supervised and unsupervised adaptation behavior.

---

## 7. Recommended Execution Order

### Step 1: Run baseline models
Use these files first to establish baseline performance:
- `CNN1D_TS_CWRU_12K_NOL.py`
- `CNN2D_TS_CWRU_12K_NOL.py`

### Step 2: Run baseline tests
Use:
- `CNN1D_TS_CWRU_12K_NOL_test.py`
- `CNN2D_TS_CWRU_12K_NOL_test.py`

### Step 3: Run supervised domain adaptation
For 1D CNN:
- `SDA_Balanced_Case1_MMD_DeepCoral_1DCNN_CWRU_Full.py`
- or modular files such as `SDA_train_1DCNN_*.py`

For 2D CNN:
- `SDA_Balanced_Case1_MMD_DeepCoral_2DCNN_CWRU_Full.py`
- `SDA_train_2DCNN.py`

### Step 4: Run explainability
Use:
- `Finalsda_gradshap.py`

### Step 5: Run unsupervised domain adaptation
Use:
- `UDA_train_2DCNN.py`
- `UDA_Balanced_Case1_MMD_DeepCoral_2DCNN_CWRU_Full.py`

---

## 8. Output Files Generated

Depending on the script, the following outputs are generated:

- trained model weights
- feature extractor weights
- classifier weights
- confusion matrices
- accuracy, precision, recall, F1-score
- training history plots
- t-SNE source feature plots
- t-SNE target feature plots
- t-SNE domain alignment plots
- Grad-CAM visualizations
- SHAP explanations
- summary Excel/CSV files

---

## 9. Notes for Reproducing Experiments

1. Update dataset paths before running scripts.
2. Ensure CWRU and Paderborn data files are available locally or in Google Drive.
3. Use GPU runtime when running in Google Colab.
4. For Grad-CAM, ensure the final convolution layer is named properly in the model.
5. Do not upload raw dataset files to GitHub because they are large.
6. Keep output folders such as `Results/` out of version control if they contain large files.
