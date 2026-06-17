> Early open-source release: an educational and research prototype for explainable ECG classification on PTB-XL. Not for clinical use.
> 
# ECGenius

ECGenius is an open-source dry-lab biomedical engineering project for classifying 12-lead ECG recordings as **normal** or **abnormal** using the **PTB-XL** dataset.

## Why this project exists

This project was built to make ECG machine learning more:

- accessible
- reproducible
- interpretable
- easy to extend

It is designed as a clean starting point for students, researchers, and developers interested in biomedical signal processing, health AI, and ECG classification.

## Current Version

Version 1 includes:

- PTB-XL metadata loading
- binary label generation (`normal` vs `abnormal`)
- ECG waveform loading
- single-lead and 12-lead ECG plotting
- basic feature extraction from all 12 leads
- baseline random forest classification
- confusion matrix
- ROC curve
- feature importance ranking
- saved metrics and result tables

## Project Goal

The current goal is to build an interpretable ECG classification pipeline that can distinguish between normal and abnormal ECG recordings using simple engineered features.

This baseline version is meant to be a strong foundation for later extensions into:

- broad abnormality category prediction
- MI vs STTC vs CD vs HYP classification
- finer diagnosis-level prediction
- stronger explainability methods

## Dataset

## Who this is for

This repo is useful for:

- students learning biomedical machine learning
- people learning ECG signal analysis
- beginner health-AI developers
- anyone wanting a PTB-XL starter pipeline

## How to Run

### 1. Create a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate

### 2. Install the required dependencies:
pip install -r requirements.txt

### 3. Download the PTB-XL dataset and place the files in:
data/raw/ptbxl/
The folder should contain:
ptbxl_database.csv
scp_statements.csv
records100/
records500/

### 4. Build the binary normal-vs-abnormal labels:
``bash
python main.py
This creates: data/processed/ptbxl_binary_labels.csv

### 5. Check that waveform loading works correctly:
``bash
python -m src.waveform_check

### 6. Generate ECG example plots:
``bash
python -m src.plot_one_ecg
python -m src.plot_12lead_ecg
python -m src.plot_normal_vs_abnormal

### 7. Build the feature table used for model training:
``bash
python -m src.build_feature_table

### 8. Train the baseline random forest model:
``bash
python -m src.train_baseline
*This generates a trained model, a confusion matrix, and a classification report.

### 9. Generate the remaining evaluation outputs:
``bash
python -m src.plot_feature_importance
python -m src.plot_class_distribution
python -m src.plot_roc_curve
python -m src.save_metrics_summary
python -m src.export_results_table

## After running the full pipeline, the main generated outputs include:

Figures

* figures/example_ecg_lead1.png
* figures/example_ecg_12lead.png
* figures/normal_vs_abnormal_lead1.png
* figures/confusion_matrix_baseline.png
* figures/feature_importance_baseline.png
* figures/class_distribution_1000.png
* figures/roc_curve_baseline.png

Results

* results/feature_table_1000.csv
* results/classification_report_baseline.txt
* results/feature_importance_baseline.csv
* results/metrics_summary.json
* results/results_summary_table.csv

Model

* models/random_forest_baseline.joblib


