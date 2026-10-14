# CardioScan AI: Clinical Heart Disease Risk Prediction System

**Machine Learning & AI — Major Capstone Project (Week 4)**  
**Student Name:** Vivek Vardhan  
**Course:** Machine Learning & AI  
**Module:** Week 4 (Major Project / Capstone)  
**Submission Date:** October 2026  
**Capstone Pathway:** Option 1 — Heart Disease Prediction (Clinical AI)

---

## 🫀 1. Executive Summary & Clinical AI Context

Cardiovascular diseases are the leading cause of premature mortality globally. In clinical decision-support systems, algorithmic predictions carry direct medical consequences. 

### Clinical Safety Rationale: Recall (Sensitivity) Priority
In healthcare machine learning systems, **Recall (Sensitivity)** is strictly prioritized over overall Accuracy:
- **False Negative (FN):** An undiagnosed individual with cardiac pathology is classified as "healthy". The patient leaves without clinical intervention, risking acute myocardial infarction or cardiac death.
- **False Positive (FP):** A healthy patient is flagged as "at risk". This prompts safe, non-invasive confirmatory diagnostics (e.g., stress echocardiography or blood biomarker verification).

Hence, model selection and threshold calibration in this project emphasize maximizing **Recall** and **ROC-AUC** while maintaining high overall precision.

---

## 📊 2. Capstone Benchmark Performance & Evaluation

The models were evaluated on the benchmark **Kaggle Heart Disease UCI (Cleveland)** dataset with a **Stratified 80/20 Train/Test Split** (`random_state=42`):

| Model Architecture | Features & Preprocessing | Accuracy | Precision | Recall (Sensitivity) | ROC-AUC | Clinical Recommendation |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Logistic Regression (Selected)** | **StandardScaler (Fit on Train)** | **80.33%** | **76.92%** | **90.91%** | **0.8690** | **Production Champion (High Recall)** |
| **Decision Tree (Max Depth=4)** | Raw Features (Scale-Invariant) | 78.69% | 76.32% | 87.88% | 0.8009 | Baseline Benchmark |

### Diagnostic Verification Chart
The pipeline automatically generates and exports publication-quality diagnostic graphics to `heart_disease_evaluation_metrics.png`:
1. **Subplot 1 — Confusion Matrix (Logistic Regression):** Shows 30 true positives diagnosed, with only 3 false negatives out of 33 diseased cases in the test set.
2. **Subplot 2 — Receiver Operating Characteristic (ROC) Curves:** Demonstrates the clear AUC superiority of Logistic Regression ($0.869$) over Decision Trees ($0.801$).

---

## 🛠️ 3. End-to-End Pipeline Architecture

```
[ Kaggle UCI Heart Disease Dataset (heart.csv) ]
                        │
                        ▼
    [ Data Ingestion & Missing Value Audit ]
                        │
                        ▼
   [ Median Imputation (Numeric Robustness) ]
                        │
                        ▼
    [ Stratified 80/20 Train/Test Splitting ]
                        │
         ┌──────────────┴──────────────┐
         ▼                             ▼
[ StandardScaler ]             [ Raw Features ]
 (Fit on Train Only)                   │
         │                             ▼
         ▼                 [ Decision Tree (depth=4) ]
[ Logistic Regression ]                │
 (max_iter=1000)                       ▼
         │                 [ Benchmark AUC = 0.8009 ]
         ▼
[ Production Champion ] ──► Recall = 90.91% | AUC = 0.8690
         │
         ▼
[ Artifact Serialization: joblib.dump() ]
 - heart_disease_logistic_model.joblib
 - heart_disease_scaler.joblib
```

---

## 🌐 3. Web & App Deployment Options

### 🌍 Live Public Internet URL (Ultra-Fast, Instant Loading Worldwide)
> **Active Public HTTPS URL:**  
> **👉 [https://trainer-logical-blake-syndicate.trycloudflare.com](https://trainer-logical-blake-syndicate.trycloudflare.com)**  
> Anyone around the world can open this link in Google Chrome, on a mobile phone, tablet, or PC to test and interact with the live clinical system with sub-millisecond calculation speeds!

- **1-Click Public Launcher (Windows):** Double-click [`run_public_tunnel.bat`](file:///C:/Users/VIVEK%20VARDHAN/.gemini/antigravity/scratch/heart_disease_capstone/run_public_tunnel.bat) anytime to regenerate or maintain public access.

---

### Deployment Modality A: Interactive Streamlit Web Application
A clinical diagnostic interface featuring individual patient risk inference, batch CSV screening, visual probability meters, and capstone benchmark analytics.

**Local Launch (Windows 1-Click):**
Double-click `run_app.bat` or run:
```bash
streamlit run app.py
```
Access at: `http://localhost:8501`

**Features:**
- Real-time diagnostic sliders and clinical drop-downs.
- Batch patient CSV screening with one-click report export.
- Interactive benchmark comparison table & diagnostic figures.
- Direct simulator for Capstone Option 2 (Loan Approval) and Option 3 (Customer Clustering).

---

### Deployment Modality B: Production FastAPI REST Microservice & Responsive Web UI
A cloud-ready REST API that powers mobile apps (Flutter, React Native), Electronic Health Record (EHR) integrations, and includes a responsive Tailwind CSS web application served directly at `/`.

**Local Launch (Windows 1-Click):**
Double-click `run_api.bat` or run:
```bash
uvicorn api_app:app --host 0.0.0.0 --port 8000 --reload
```
- **Web Interface:** `http://localhost:8000/`
- **Interactive Swagger Documentation:** `http://localhost:8000/docs`
- **Alternative ReDoc UI:** `http://localhost:8000/redoc`

#### REST API Endpoints:
- `POST /api/predict`: Real-time cardiac risk assessment for an individual patient.
- `POST /api/predict/batch`: High-throughput triage for multiple patient profiles.
- `GET /api/metrics`: Programmatic retrieval of model benchmarks.
- `GET /api/health`: Health status endpoint for container orchestrators (Kubernetes/Cloud Run).

#### Sample API Request (`POST /api/predict`):
```bash
curl -X 'POST' \
  'http://localhost:8000/api/predict' \
  -H 'Content-Type: application/json' \
  -d '{
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
  }'
```

#### Sample Response:
```json
{
  "prediction": 1,
  "diagnosis": "Positive for Heart Disease (Class 1)",
  "probability_disease": 0.8452,
  "probability_healthy": 0.1548,
  "confidence": 0.8452,
  "risk_level": "Critical / Severe Risk",
  "recommendation": "Immediate cardiological consultation recommended. Prioritize secondary diagnostic screening (Stress Echo, Coronary Angiography)."
}
```

---

### Deployment Modality C: Docker & Containerized Cloud Deployment

This project includes a multi-stage `Dockerfile` and `docker-compose.yml`.

**Build & Run with Docker:**
```bash
docker build -t cardioscan-ai .
docker run -p 8501:8501 cardioscan-ai
```

**Run both Web UI (8501) & API Service (8000) together:**
```bash
docker compose up -d
```

---

### Deployment Modality D: 1-Click Free Cloud Hosting

1. **Streamlit Community Cloud (Free Web App):**
   - Fork/push this repository to GitHub.
   - Go to [share.streamlit.io](https://share.streamlit.io).
   - Select your repo and point the main file path to `app.py`.
   - Click **Deploy**!

2. **Render / Railway / Hugging Face Spaces (Free Cloud API / App):**
   - The repository includes a preconfigured `Procfile` and `render.yaml`.
   - Simply connect your repository on [render.com](https://render.com) or [huggingface.co/spaces](https://huggingface.co/spaces) as a Web Service.

---

## 🧩 5. Additional Capstone Options (Part 3)

In addition to the primary Heart Disease system, complete implementations for the remaining Capstone options are included:

### Option 2: Bank Loan Approval Prediction (FinTech AI)
- **Script:** `train_loan_model.py`
- **Dataset:** `loan_data.csv`
- **Methodology:** Imputation, One-Hot Encoding of demographics (`Gender`, `Married`, `Education`, `Property_Area`), Random Forest ensemble fitting (`n_estimators=100, max_depth=6`).
- **Engineered Artifacts:** `models/loan_rf_model.joblib`, `models/loan_features.joblib`.

### Option 3: Customer Segmentation (Business Analytics)
- **Script:** `cluster_customers.py`
- **Dataset:** `Mall_Customers.csv`
- **Methodology:** Unsupervised K-Means clustering ($k=5$, `init='k-means++'`) on Annual Income and Spending Score.
- **Engineered Segments:**
  1. *Conservative Spenders* (Low Spend, High Income)
  2. *Balanced Shoppers* (Medium Income, Medium Spend)
  3. *High Value VIPs* (High Income, High Spend)
  4. *Careful Youth* (Low Income, Low Spend)
  5. *Impulsive Buyers* (Low Income, High Spend)
- **Engineered Artifacts:** `models/mall_kmeans_model.joblib`, `static/customer_segments_clusters.png`.

---

## 🧪 6. Automated Testing & Verification

A test suite is included in `test_prediction.py`. It tests:
1. Production model & scaler artifact loading.
2. Feature scaling & logistic regression prediction integrity.
3. Probability calibration constraints ($\sum P = 1.0$).
4. FastAPI health and prediction endpoint responses.
5. HTML template rendering.

Run tests using:
```bash
python test_prediction.py
```
or double-click `run_tests.bat`.

---

## 📁 7. Project Directory Structure

```
heart_disease_capstone/
├── data/
│   ├── heart.csv                     # Kaggle Heart Disease UCI dataset
│   ├── loan_data.csv                 # FinTech Loan Prediction dataset
│   └── Mall_Customers.csv            # Retail Customer Clustering dataset
├── models/
│   ├── heart_disease_logistic_model.joblib
│   ├── heart_disease_scaler.joblib
│   ├── heart_disease_dt_model.joblib
│   ├── loan_rf_model.joblib
│   ├── loan_features.joblib
│   ├── mall_kmeans_model.joblib
│   └── metrics_summary.json
├── static/
│   ├── heart_disease_evaluation_metrics.png
│   └── customer_segments_clusters.png
├── templates/
│   └── index.html                    # Responsive Tailwind CSS Web App
├── train_pipeline.py                 # Primary Capstone Training Pipeline (Part 2)
├── train_loan_model.py               # Option 2 Loan Pipeline (Part 3)
├── cluster_customers.py              # Option 3 Clustering Pipeline (Part 3)
├── app.py                            # Streamlit Interactive Web Application
├── api_app.py                        # FastAPI Production Microservice & Web UI
├── test_prediction.py                # Automated Test & Validation Suite
├── requirements.txt                  # Production Dependency Specification
├── Dockerfile                        # Multi-Stage Docker Build
├── docker-compose.yml                # Dual-Service Local Orchestration
├── Procfile                          # Cloud PaaS Deployment Config
├── run_app.bat                       # 1-Click Streamlit Web App Launcher (Windows)
├── run_api.bat                       # 1-Click FastAPI Server Launcher (Windows)
├── run_tests.bat                     # 1-Click Test Suite Launcher (Windows)
└── README.md                         # Comprehensive Capstone Documentation
```

---

## 📜 8. Submission Verification

**Machine Learning & AI Coursework — Week 4 Major Capstone Submission**  
**Student Name:** Vivek Vardhan  
**Submission Date:** October 2026  
**Status:** Verified, Tested, Serialized & Deployable
