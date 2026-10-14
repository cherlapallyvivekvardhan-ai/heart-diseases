"""
Bank Loan Approval Prediction Pipeline (Capstone Option 2)
Student Name: Vivek Vardhan | Machine Learning & AI
"""

import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

def train_loan_pipeline():
    data_path = 'loan_data.csv' if os.path.exists('loan_data.csv') else os.path.join('data', 'loan_data.csv')
    df_loan = pd.read_csv(data_path)
    print(f"Loan Dataset Ingested. Dimensions: {df_loan.shape}")

    # Impute and encode categorical variables
    cat_cols = ['Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area']
    existing_cat = [c for c in cat_cols if c in df_loan.columns]
    df_loan = pd.get_dummies(df_loan, columns=existing_cat, drop_first=True)
    df_loan.fillna(df_loan.median(numeric_only=True), inplace=True)

    X_loan = df_loan.drop(columns=['Loan_ID', 'Loan_Status'], errors='ignore')
    # Handle Loan_Status encoding ('Y' -> 1, 'N' -> 0)
    if 'Loan_Status' in df_loan.columns:
        y_loan = df_loan['Loan_Status'].apply(lambda x: 1 if str(x).strip().upper() in ['Y', '1'] else 0)
    else:
        raise ValueError("Loan_Status column not found")

    X_tr, X_te, y_tr, y_te = train_test_split(X_loan, y_loan, test_size=0.2, random_state=42)

    # Train Random Forest Classifier
    rf_model = RandomForestClassifier(n_estimators=100, max_depth=6, random_state=42)
    rf_model.fit(X_tr, y_tr)

    # Evaluation
    y_pred_rf = rf_model.predict(X_te)
    print("Loan Approval Confusion Matrix:\n", confusion_matrix(y_te, y_pred_rf))
    print("\nClassification Report:\n", classification_report(y_te, y_pred_rf))

    os.makedirs('models', exist_ok=True)
    joblib.dump(rf_model, os.path.join('models', 'loan_rf_model.joblib'))
    joblib.dump(list(X_loan.columns), os.path.join('models', 'loan_features.joblib'))
    print("Loan approval model saved successfully.")

if __name__ == '__main__':
    train_loan_pipeline()
