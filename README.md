# OpenECG-XAI

OpenECG-XAI is a dry-lab biomedical engineering project for classifying 12-lead ECG recordings as normal or abnormal using the PTB-XL dataset.

## Project Goal

This project builds an interpretable machine learning pipeline that:

- loads ECG waveform data from PTB-XL
- extracts basic signal features
- trains a baseline classifier
- evaluates classification performance
- generates figures and result tables for analysis

## Current Version

Version 1 performs:

- binary classification: normal vs abnormal ECG
- waveform visualization
- feature extraction
- baseline random forest classification
- confusion matrix generation
- ROC curve plotting
- feature importance analysis

## Dataset

- PTB-XL
- 12-lead ECG records
- 100 Hz waveform version used for the baseline pipeline

## Current Outputs

Generated outputs include:

- `figures/example_ecg_lead1.png`
- `figures/example_ecg_12lead.png`
- `figures/normal_vs_abnormal_lead1.png`
- `figures/confusion_matrix_baseline.png`
- `figures/feature_importance_baseline.png`
- `figures/class_distribution_1000.png`
- `figures/roc_curve_baseline.png`
- `results/feature_table_1000.csv`
- `results/classification_report_baseline.txt`
- `results/feature_importance_baseline.csv`
- `results/metrics_summary.json`
- `results/results_summary_table.csv`
- `models/random_forest_baseline.joblib`

## Baseline Result

The current baseline model is a random forest trained on extracted ECG features from 1,000 samples.

## Next Planned Extensions

- broader ECG abnormality category prediction
- MI vs STTC vs CD vs HYP classification
- more advanced explainability
- improved feature engineering
- report and presentation packaging