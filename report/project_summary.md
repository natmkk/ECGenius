# Project Summary

## Title
OpenECG-XAI: Explainable ECG Classification from PTB-XL

## Overview
This project builds a dry-lab biomedical engineering pipeline for classifying 12-lead ECG recordings as normal or abnormal using the PTB-XL dataset.

## Objective
The objective is to develop an interpretable machine learning baseline that can process ECG waveform data, extract useful signal features, and classify recordings into normal or abnormal categories.

## Dataset
The project uses the PTB-XL public ECG dataset and focuses on the 100 Hz waveform files for the baseline version.

## Methods
The workflow includes metadata loading, label processing, ECG waveform visualization, feature extraction, random forest classification, and evaluation using confusion matrix, ROC curve, and feature importance analysis.

## Current Results
The current version uses 1,000 ECG samples and a random forest baseline model. Output artifacts include waveform figures, evaluation plots, saved metrics, a trained model file, and feature importance tables.

## Current Scope
Version 1 performs binary classification only:
- normal
- abnormal

## Future Extensions
Future versions will extend the project to:
- broad abnormality category prediction
- MI vs STTC vs CD vs HYP classification
- finer diagnosis-level prediction
- stronger explainability methods