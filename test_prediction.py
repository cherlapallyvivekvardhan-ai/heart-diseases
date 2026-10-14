"""
Automated Test Suite for CardioScan AI Heart Disease Prediction System
Validates model loading, scaling, predictions, and FastAPI endpoints
"""

import os
import joblib
import numpy as np
from fastapi.testclient import TestClient
from api_app import app

client = TestClient(app)

def test_artifacts_exist():
    """Verify serialized model and scaler exist."""
    assert os.path.exists("heart_disease_logistic_model.joblib") or os.path.exists("models/heart_disease_logistic_model.joblib"), "Model file missing"
    assert os.path.exists("heart_disease_scaler.joblib") or os.path.exists("models/heart_disease_scaler.joblib"), "Scaler file missing"
    assert os.path.exists("heart_disease_evaluation_metrics.png") or os.path.exists("static/heart_disease_evaluation_metrics.png"), "Diagnostic image missing"

def test_model_inference():
    """Verify inference pipeline produces valid output and probabilities."""
    model_path = "heart_disease_logistic_model.joblib" if os.path.exists("heart_disease_logistic_model.joblib") else "models/heart_disease_logistic_model.joblib"
    scaler_path = "heart_disease_scaler.joblib" if os.path.exists("heart_disease_scaler.joblib") else "models/heart_disease_scaler.joblib"
    
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)

    import pandas as pd
    feature_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 
                     'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
    sample_df = pd.DataFrame([[63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1]], columns=feature_names)
    scaled = scaler.transform(sample_df)
    
    pred = model.predict(scaled)
    probs = model.predict_proba(scaled)

    assert pred[0] in [0, 1], "Prediction must be 0 or 1"
    assert 0.0 <= probs[0, 1] <= 1.0, "Probability must be between 0 and 1"
    assert np.isclose(np.sum(probs[0]), 1.0), "Probabilities must sum to 1"

def test_api_health():
    """Test health check endpoint."""
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["model_loaded"] is True
    assert data["scaler_loaded"] is True

def test_api_predict():
    """Test single patient prediction endpoint."""
    payload = {
        "age": 63,
        "sex": 1,
        "cp": 3,
        "trestbps": 145,
        "chol": 233,
        "fbs": 1,
        "restecg": 0,
        "thalach": 150,
        "exang": 0,
        "oldpeak": 2.3,
        "slope": 0,
        "ca": 0,
        "thal": 1
    }
    response = client.post("/api/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["prediction"] in [0, 1]
    assert "probability_disease" in data
    assert "risk_level" in data
    assert "recommendation" in data

def test_api_homepage():
    """Test that homepage serves HTML correctly."""
    response = client.get("/")
    assert response.status_code == 200
    assert "CardioScan AI" in response.text
    assert "Vivek Vardhan" in response.text

if __name__ == "__main__":
    print("Running automated tests...")
    test_artifacts_exist()
    print("Artifact existence test: PASSED")
    test_model_inference()
    print("Model inference test: PASSED")
    test_api_health()
    print("API health endpoint test: PASSED")
    test_api_predict()
    print("API predict endpoint test: PASSED")
    test_api_homepage()
    print("API homepage test: PASSED")
    print("\nAll unit and integration tests passed successfully!")
