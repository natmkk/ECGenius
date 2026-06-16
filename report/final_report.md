# ECGenius: Explainable ECG Classification from PTB-XL

## Abstract

This project presents ECGenius, a dry-lab biomedical engineering pipeline for classifying 12-lead ECG recordings as normal or abnormal using the PTB-XL public dataset. ECG waveform data were loaded from the 100 Hz signal files, transformed into engineered signal features, and used to train a baseline random forest classifier. The system also generated waveform visualizations, a confusion matrix, an ROC curve, class distribution plots, and feature importance rankings. On a subset of 1,000 ECG recordings, the baseline model achieved an accuracy of 0.73 and an ROC-AUC of 0.814. These results show that simple interpretable features can support meaningful ECG abnormality detection and provide a strong foundation for future extensions into broader abnormality-category and diagnosis-level prediction.

## Introduction

Electrocardiography is one of the most common noninvasive tools used to evaluate cardiac electrical activity. Because ECG recordings are widely used in clinical settings, automated analysis of ECG signals is an important biomedical engineering problem.

This project focuses on building a dry-lab computational pipeline for ECG classification using the PTB-XL public dataset. The baseline goal is to classify 12-lead ECG recordings as normal or abnormal using extracted signal features and a machine learning model.

In addition to classification, the project emphasizes interpretability and reproducibility. The workflow includes waveform visualization, feature extraction, model evaluation, and feature importance analysis, making the system useful both as an engineering prototype and as an open-source educational project.

The current version is limited to binary classification, but it is designed to support future extensions to broader abnormality-category prediction and more detailed diagnostic classification.

## Methods

### Dataset

This project uses the PTB-XL public electrocardiography dataset. For the baseline pipeline, the 100 Hz waveform files were used. Metadata and diagnostic label information were loaded from the provided PTB-XL CSV files.

### Label Definition

A binary classification task was defined:
- normal
- abnormal

An ECG recording was labeled as normal if its SCP code dictionary contained `NORM`. All other recordings were labeled as abnormal.

### Waveform Processing

Individual ECG recordings were loaded using the waveform file paths provided in the PTB-XL metadata table. The low-resolution waveform files (`filename_lr`) were used for the baseline version of the project.

### Feature Extraction

For each of the 12 ECG leads, the following basic signal features were extracted:

- mean
- standard deviation
- minimum
- maximum
- root mean square (RMS)

This produced a structured feature table used for classification.

### Model

A random forest classifier was used as the baseline model. The feature table was split into training and test sets using an 80/20 split with stratification by class.

### Evaluation

The model was evaluated using:
- accuracy
- precision
- recall
- F1-score
- ROC-AUC
- confusion matrix

Additional outputs included feature importance ranking and example ECG waveform plots.

## Results

### Binary Classification Performance

A baseline random forest classifier was trained on extracted ECG features from 1,000 PTB-XL recordings to distinguish normal and abnormal ECGs.

The model achieved the following performance:

- Accuracy: 0.73
- Precision (abnormal): 0.71
- Recall (abnormal): 0.72
- F1-score (abnormal): 0.72
- ROC-AUC: 0.814

### Generated Outputs

The current baseline pipeline produced the following result artifacts:

- confusion matrix
- ROC curve
- feature importance plot
- class distribution plot
- example ECG waveform plots
- saved feature importance table
- saved classification report
- saved metrics summary table

### Interpretation

The baseline results show that simple engineered ECG features combined with a random forest classifier can provide meaningful separation between normal and abnormal ECG recordings. The ROC-AUC above 0.8 suggests that the model captures useful signal-level differences, even with a relatively simple feature set and a limited subset of the full dataset.

### Current Limitation

This version performs binary classification only and does not yet distinguish among abnormality subtypes such as MI, STTC, CD, or HYP.

## Conclusion

This project developed a baseline dry-lab biomedical engineering pipeline for classifying 12-lead ECG recordings as normal or abnormal using the PTB-XL dataset.

The current system successfully loads waveform data, extracts simple signal features, trains a random forest classifier, and generates evaluation outputs including a confusion matrix, ROC curve, class distribution plot, and feature importance analysis.

The baseline results show that even simple engineered features can support meaningful discrimination between normal and abnormal ECG recordings. This makes the project a strong foundation for future extensions.

Future work will expand the system beyond binary classification to predict broader ECG abnormality categories such as MI, STTC, CD, and HYP, and later support finer-grained diagnostic prediction and stronger explainability methods.
