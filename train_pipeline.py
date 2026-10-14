"""
Heart Disease Prediction System - Full ML Production Pipeline
Student Name: Vivek Vardhan
Course: Machine Learning & AI
Module: Week 4 (Major Project / Capstone)
Submission Date: October 2026
"""

import os
import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    precision_score,
    recall_score,
    roc_auc_score,
    roc_curve,
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

def run_pipeline():
    # ---------------------------------------------------------
    # Step 1: Load Clinical Dataset (Kaggle Heart Disease UCI)
    # ---------------------------------------------------------
    # Features: age, sex, cp (chest pain), trestbps, chol, fbs, restecg,
    # thalach, exang, oldpeak, slope, ca, thal, target (1=Heart Disease, 0=Healthy)
    data_path = 'heart.csv' if os.path.exists('heart.csv') else os.path.join('data', 'heart.csv')
    df = pd.read_csv(data_path)
    print(f"Dataset ingested successfully from '{data_path}'. Dimensions: {df.shape}")

    # ---------------------------------------------------------
    # Step 2: Data Cleaning & Preprocessing
    # ---------------------------------------------------------
    # Verify null entries and impute numerical attributes if needed
    null_count = df.isnull().sum().sum()
    print(f"Initial missing values count: {null_count}")
    if null_count > 0:
        df.fillna(df.median(numeric_only=True), inplace=True)
        print("Median imputation completed successfully.")

    X = df.drop(columns=['target'])
    y = df['target']

    # Stratified Split (80% Train, 20% Test)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    print(f"Stratified split completed -> Train: {X_train.shape[0]} samples, Test: {X_test.shape[0]} samples")

    # Feature Scaling (Fit only on training set to avoid data leakage)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # ---------------------------------------------------------
    # Step 3: Train Benchmark Models (Logistic Regression vs Decision Tree)
    # ---------------------------------------------------------
    # 1. Logistic Regression Model
    log_reg = LogisticRegression(random_state=42, max_iter=1000)
    log_reg.fit(X_train_scaled, y_train)

    # 2. Decision Tree Classifier
    dt_clf = DecisionTreeClassifier(max_depth=4, random_state=42)
    dt_clf.fit(X_train, y_train)  # Trees are scale-invariant

    # Predict probabilities and class labels
    y_pred_lr = log_reg.predict(X_test_scaled)
    y_prob_lr = log_reg.predict_proba(X_test_scaled)[:, 1]

    y_pred_dt = dt_clf.predict(X_test)
    y_prob_dt = dt_clf.predict_proba(X_test)[:, 1]

    # ---------------------------------------------------------
    # Step 4: Metric Evaluation (Accuracy, Precision, Recall, ROC-AUC)
    # ---------------------------------------------------------
    acc_lr = accuracy_score(y_test, y_pred_lr)
    prec_lr = precision_score(y_test, y_pred_lr)
    rec_lr = recall_score(y_test, y_pred_lr)
    auc_lr = roc_auc_score(y_test, y_prob_lr)

    acc_dt = accuracy_score(y_test, y_pred_dt)
    prec_dt = precision_score(y_test, y_pred_dt)
    rec_dt = recall_score(y_test, y_pred_dt)
    auc_dt = roc_auc_score(y_test, y_prob_dt)

    print("\n=== Model Performance Benchmarking ===")
    print(f"Logistic Regression -> Accuracy: {acc_lr:.4f} | Precision: {prec_lr:.4f} | Recall: {rec_lr:.4f} | AUC: {auc_lr:.4f}")
    print(f"Decision Tree       -> Accuracy: {acc_dt:.4f} | Precision: {prec_dt:.4f} | Recall: {rec_dt:.4f} | AUC: {auc_dt:.4f}")

    print("\nDetailed Classification Report (Logistic Regression):")
    print(classification_report(y_test, y_pred_lr, target_names=['Healthy (0)', 'Disease (1)']))

    # ---------------------------------------------------------
    # Step 5: Visualizations (Confusion Matrix & ROC Curve)
    # ---------------------------------------------------------
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Subplot 1: Confusion Matrix (Logistic Regression)
    cm = confusion_matrix(y_test, y_pred_lr)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[0],
                xticklabels=['Healthy (0)', 'Disease (1)'],
                yticklabels=['Healthy (0)', 'Disease (1)'],
                cbar=False, annot_kws={"size": 14, "weight": "bold"})
    axes[0].set_title('Logistic Regression: Confusion Matrix', fontsize=12, fontweight='bold')
    axes[0].set_xlabel('Predicted Label', fontsize=10)
    axes[0].set_ylabel('True Label', fontsize=10)

    # Subplot 2: ROC Curves
    fpr_lr, tpr_lr, _ = roc_curve(y_test, y_prob_lr)
    fpr_dt, tpr_dt, _ = roc_curve(y_test, y_prob_dt)

    axes[1].plot(fpr_lr, tpr_lr, color='#1A365D', lw=2.5, label=f'Logistic Regression (AUC = {auc_lr:.3f})')
    axes[1].plot(fpr_dt, tpr_dt, color='#E53E3E', lw=2, linestyle='--', label=f'Decision Tree (AUC = {auc_dt:.3f})')
    axes[1].plot([0, 1], [0, 1], color='gray', linestyle=':')
    axes[1].set_title('Receiver Operating Characteristic (ROC) Curve', fontsize=12, fontweight='bold')
    axes[1].set_xlabel('False Positive Rate (1 - Specificity)', fontsize=10)
    axes[1].set_ylabel('True Positive Rate (Sensitivity / Recall)', fontsize=10)
    axes[1].legend(loc='lower right')
    axes[1].grid(True, linestyle='--', alpha=0.5)

    plt.tight_layout()
    chart_output = 'heart_disease_evaluation_metrics.png'
    plt.savefig(chart_output, dpi=300)
    # Also save to static folder for web serving
    static_chart = os.path.join('static', chart_output)
    plt.savefig(static_chart, dpi=300)
    plt.close()
    print(f"Saved diagnostic figures: {chart_output} and {static_chart}")

    # ---------------------------------------------------------
    # Step 6: Artifact Serialization
    # ---------------------------------------------------------
    model_file = 'heart_disease_logistic_model.joblib'
    scaler_file = 'heart_disease_scaler.joblib'
    
    # Save in root
    joblib.dump(log_reg, model_file)
    joblib.dump(scaler, scaler_file)
    
    # Also save in models/ directory
    joblib.dump(log_reg, os.path.join('models', model_file))
    joblib.dump(scaler, os.path.join('models', scaler_file))
    # Also save Decision Tree for comparison in UI
    joblib.dump(dt_clf, os.path.join('models', 'heart_disease_dt_model.joblib'))

    # Save benchmark metrics to json for web UI quick loading
    import json
    metrics_summary = {
        "dataset_rows": len(df),
        "logistic_regression": {
            "accuracy": round(float(acc_lr), 4),
            "precision": round(float(prec_lr), 4),
            "recall": round(float(rec_lr), 4),
            "auc": round(float(auc_lr), 4)
        },
        "decision_tree": {
            "accuracy": round(float(acc_dt), 4),
            "precision": round(float(prec_dt), 4),
            "recall": round(float(rec_dt), 4),
            "auc": round(float(auc_dt), 4)
        },
        "features": list(X.columns)
    }
    with open('models/metrics_summary.json', 'w') as f:
        json.dump(metrics_summary, f, indent=2)

    print("Model pipeline successfully serialized.")
    print("Clinical Safety Note: In healthcare ML systems, Recall (Sensitivity) is prioritized over overall Accuracy.")
    return metrics_summary

if __name__ == '__main__':
    run_pipeline()
