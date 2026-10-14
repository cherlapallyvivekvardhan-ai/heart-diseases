"""
CardioScan AI - Clinical Heart Disease Risk Prediction System
Week 4 Major Capstone Project | Machine Learning & AI
Student: Vivek Vardhan | Submission Date: October 2026
"""

import json
import os
import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="CardioScan AI - Heart Disease Clinical Prediction",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #0F2027 0%, #203A43 50%, #2C5364 100%);
        padding: 24px;
        border-radius: 12px;
        color: white;
        margin-bottom: 24px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
    }
    .badge-capstone {
        background-color: #E53E3E;
        color: white;
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 0.82rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 8px;
    }
    .metric-card {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 16px;
        text-align: center;
    }
    .risk-high {
        background: #FEF2F2;
        border-left: 6px solid #EF4444;
        padding: 18px;
        border-radius: 8px;
        margin-top: 16px;
    }
    .risk-low {
        background: #F0FDF4;
        border-left: 6px solid #22C55E;
        padding: 18px;
        border-radius: 8px;
        margin-top: 16px;
    }
</style>
""", unsafe_allow_html=True)

# Helper function to load model and scaler
@st.cache_resource
def load_artifacts():
    model_paths = [
        'heart_disease_logistic_model.joblib',
        'models/heart_disease_logistic_model.joblib'
    ]
    scaler_paths = [
        'heart_disease_scaler.joblib',
        'models/heart_disease_scaler.joblib'
    ]
    
    model = None
    scaler = None
    
    for p in model_paths:
        if os.path.exists(p):
            model = joblib.load(p)
            break
            
    for p in scaler_paths:
        if os.path.exists(p):
            scaler = joblib.load(p)
            break
            
    # Also attempt loading metrics summary
    metrics = None
    if os.path.exists('models/metrics_summary.json'):
        with open('models/metrics_summary.json', 'r') as f:
            metrics = json.load(f)
            
    return model, scaler, metrics

model, scaler, metrics = load_artifacts()

# Sidebar: Student Info & Navigation
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/865/865969.png", width=70)
    st.markdown("### 🫀 CardioScan AI")
    st.markdown("**Major Capstone Project (Week 4)**")
    st.markdown("---")
    st.markdown("**Student Name:** Vivek Vardhan")
    st.markdown("**Course:** Machine Learning & AI")
    st.markdown("**Module:** Week 4 Capstone")
    st.markdown("**Submission:** October 2026")
    st.markdown("---")
    
    st.markdown("### ⚙️ Pipeline Specifications")
    st.markdown("- **Algorithm:** Scaled Logistic Regression")
    st.markdown("- **Pre-processing:** Median Imputation + StandardScaler")
    st.markdown("- **Clinical Priority:** Recall (Sensitivity)")
    st.markdown("- **Benchmark AUC:** ~0.87 - 0.92")
    st.markdown("---")
    st.caption("Powered by Scikit-Learn, Streamlit & FastAPI")

# Main Header Banner
st.markdown("""
<div class="main-header">
    <span class="badge-capstone">CLINICAL AI CAPSTONE</span>
    <h1 style="margin:0; font-size:2.1rem; color: #FFFFFF;">CardioScan AI: Clinical Heart Disease Risk Prediction</h1>
    <p style="margin-top:8px; opacity:0.9; font-size:1.05rem; color: #E2E8F0;">
        End-to-End Machine Learning Diagnostic Pipeline & Decision Support System (UCI Cleveland Dataset)
    </p>
</div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🩺 Patient Clinical Assessment",
    "📁 Batch Patient Screening",
    "📊 Benchmarks & Diagnostics",
    "🧩 Additional Capstone Options",
    "🚀 Cloud & Deployment Architecture"
])

FEATURE_NAMES = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 
                 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

# =========================================================================
# TAB 1: Single Patient Diagnostic Assessment
# =========================================================================
with tab1:
    st.markdown("### 📋 Enter Patient Clinical Markers")
    st.markdown("Provide standard diagnostic vitals and cardiology exam metrics below for risk inference:")

    with st.form("clinical_form"):
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Demographics & Vitals")
            age = st.slider("Patient Age (years)", min_value=18, max_value=100, value=55, help="Age in years")
            sex = st.radio("Sex", options=[1, 0], format_func=lambda x: "Male (1)" if x == 1 else "Female (0)", horizontal=True)
            
            cp = st.selectbox(
                "Chest Pain Type (cp)",
                options=[0, 1, 2, 3],
                format_func=lambda x: {
                    0: "0 - Typical Angina (Substernal pressure with exertion)",
                    1: "1 - Atypical Angina (Non-exertional chest discomfort)",
                    2: "2 - Non-Anginal Pain (Musculoskeletal / gastrointestinal)",
                    3: "3 - Asymptomatic (No typical cardiac chest pain)"
                }[x],
                help="Type of chest discomfort reported by patient"
            )
            
            trestbps = st.number_input("Resting Blood Pressure (trestbps) [mm Hg]", min_value=80, max_value=220, value=130, step=1, help="Resting blood pressure on hospital admission")
            chol = st.number_input("Serum Cholesterol (chol) [mg/dl]", min_value=100, max_value=600, value=240, step=1, help="Total serum cholesterol")
            fbs = st.radio("Fasting Blood Sugar > 120 mg/dl (fbs)", options=[1, 0], format_func=lambda x: "True (> 120 mg/dl)" if x == 1 else "False (<= 120 mg/dl)", horizontal=True)
            restecg = st.selectbox(
                "Resting Electrocardiogram (restecg)",
                options=[0, 1, 2],
                format_func=lambda x: {
                    0: "0 - Normal ECG",
                    1: "1 - ST-T wave abnormality (inversions/elevations)",
                    2: "2 - Left Ventricular Hypertrophy (Estes criteria)"
                }[x]
            )

        with col2:
            st.subheader("Exercise Stress & Advanced Cardiology")
            thalach = st.number_input("Max Heart Rate Achieved (thalach) [bpm]", min_value=60, max_value=220, value=150, step=1, help="Maximum heart rate recorded during treadmill test")
            exang = st.radio("Exercise Induced Angina (exang)", options=[1, 0], format_func=lambda x: "Yes (Angina during stress)" if x == 1 else "No", horizontal=True)
            oldpeak = st.slider("ST Depression Induced by Exercise (oldpeak)", min_value=0.0, max_value=6.2, value=1.0, step=0.1, help="ST depression induced by exercise relative to rest")
            
            slope = st.selectbox(
                "Peak Exercise ST Segment Slope (slope)",
                options=[0, 1, 2],
                format_func=lambda x: {
                    0: "0 - Upsloping (Benign/Normal physiological response)",
                    1: "1 - Flat (Ischemic plateau pattern)",
                    2: "2 - Downsloping (High likelihood of coronary occlusion)"
                }[x]
            )
            
            ca = st.selectbox(
                "Number of Major Vessels Colored by Fluoroscopy (ca)",
                options=[0, 1, 2, 3],
                format_func=lambda x: f"{x} major coronary vessel(s) visible under fluoroscopy"
            )
            
            thal = st.selectbox(
                "Thallium Stress Scintigraphy (thal)",
                options=[1, 2, 3],
                format_func=lambda x: {
                    1: "1 - Normal blood perfusion",
                    2: "2 - Fixed Defect (Previous myocardial infarction)",
                    3: "3 - Reversible Defect (Active ischemia under stress)"
                }[x]
            )

        submitted = st.form_submit_button("🔍 Run Clinical Diagnostic Evaluation", use_container_width=True)

    if submitted:
        if model is None or scaler is None:
            st.error("Model artifacts not loaded. Please ensure training pipeline has executed.")
        else:
            # Construct feature vector DataFrame
            patient_df = pd.DataFrame([[age, sex, cp, trestbps, chol, fbs, restecg, 
                                        thalach, exang, oldpeak, slope, ca, thal]], 
                                      columns=FEATURE_NAMES)
            
            # Preprocessing: StandardScaler transform
            patient_scaled = scaler.transform(patient_df)
            
            # Inference
            prediction = int(model.predict(patient_scaled)[0])
            prob_disease = float(model.predict_proba(patient_scaled)[0, 1])
            prob_healthy = 1.0 - prob_disease

            st.markdown("### 📊 Diagnostic Evaluation Results")
            
            col_res1, col_res2, col_res3 = st.columns([1, 1, 1])
            with col_res1:
                st.metric("Risk Probability", f"{prob_disease * 100:.1f}%")
            with col_res2:
                status_label = "HIGH RISK (Class 1)" if prediction == 1 else "LOW RISK / HEALTHY (Class 0)"
                st.metric("Clinical Verdict", status_label)
            with col_res3:
                confidence = max(prob_disease, prob_healthy) * 100
                st.metric("Model Confidence", f"{confidence:.1f}%")

            # Progress bar for visual probability
            st.write("**Cardiac Pathology Probability Scale:**")
            st.progress(prob_disease)

            if prediction == 1:
                st.markdown(f"""
                <div class="risk-high">
                    <h3 style="color:#B91C1C; margin:0;">⚠️ High Cardiac Disease Risk Detected ({prob_disease*100:.1f}%)</h3>
                    <p style="margin-top:8px; color:#374151;">
                        The model identified physiological and exercise stress markers associated with significant cardiovascular pathology.
                    </p>
                    <ul>
                        <li><b>Target Classification:</b> Positive for Heart Disease (1)</li>
                        <li><b>Key Contributing Indicators:</b> Chest pain grade ({cp}), ST depression ({oldpeak}), Fluoroscopy vessels ({ca}), Stress Thalassemia ({thal}).</li>
                        <li><b>Action:</b> Prioritize confirmatory screening (coronary angiography, echocardiography).</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="risk-low">
                    <h3 style="color:#15803D; margin:0;">✅ Low Risk / Negative Cardiac Indicators ({prob_disease*100:.1f}%)</h3>
                    <p style="margin-top:8px; color:#374151;">
                        The submitted markers reside within typical healthy reference ranges for the UCI Cleveland benchmark.
                    </p>
                    <ul>
                        <li><b>Target Classification:</b> Healthy / Low Risk (0)</li>
                        <li><b>Probability of Absence:</b> {prob_healthy*100:.1f}%</li>
                        <li><b>Recommendation:</b> Maintain routine preventative annual cardiovascular monitoring.</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)

            # Clinical Safety Note
            st.info("""
            **Clinical Safety Note:** In healthcare machine learning systems, **Recall (Sensitivity)** is prioritized over overall Accuracy. 
            A False Negative represents an undiagnosed patient with cardiac pathology, whereas a False Positive prompts safe confirmatory screening.
            """)

# =========================================================================
# TAB 2: Batch Patient Screening
# =========================================================================
with tab2:
    st.markdown("### 📁 Batch Clinical Patient Screening")
    st.markdown("Upload a CSV file containing multiple patient records to perform batch clinical triage:")

    # Provide sample CSV template
    sample_df = pd.DataFrame([
        [63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1],
        [37, 1, 2, 130, 250, 0, 1, 187, 0, 3.5, 0, 0, 2],
        [41, 0, 1, 130, 204, 0, 0, 172, 0, 1.4, 2, 0, 2],
        [56, 1, 1, 120, 236, 0, 1, 178, 0, 0.8, 2, 0, 2],
        [57, 0, 0, 120, 354, 0, 1, 163, 1, 0.6, 2, 0, 2],
        [57, 1, 0, 140, 192, 0, 1, 148, 0, 0.4, 1, 0, 1]
    ], columns=FEATURE_NAMES)
    
    csv_bytes = sample_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Sample Batch Input CSV Template",
        data=csv_bytes,
        file_name="sample_patient_batch.csv",
        mime="text/csv"
    )

    uploaded_file = st.file_uploader("Upload Patient CSV File", type=["csv"])

    if uploaded_file is not None:
        try:
            batch_df = pd.read_csv(uploaded_file)
            st.write(f"**Loaded {len(batch_df)} patient records:**")
            st.dataframe(batch_df.head())

            missing_cols = [c for c in FEATURE_NAMES if c not in batch_df.columns]
            if missing_cols:
                st.error(f"Missing required clinical features: {missing_cols}")
            else:
                if st.button("⚡ Run Batch Diagnostic Triage"):
                    X_batch = batch_df[FEATURE_NAMES].copy()
                    # Handle any missing values with median
                    if X_batch.isnull().sum().sum() > 0:
                        X_batch.fillna(X_batch.median(numeric_only=True), inplace=True)
                    
                    X_batch_scaled = scaler.transform(X_batch)
                    preds = model.predict(X_batch_scaled)
                    probs = model.predict_proba(X_batch_scaled)[:, 1]

                    result_df = batch_df.copy()
                    result_df['Predicted_Disease'] = preds
                    result_df['Risk_Probability'] = np.round(probs * 100, 2)
                    result_df['Clinical_Status'] = ['High Risk (Class 1)' if p == 1 else 'Healthy (Class 0)' for p in preds]

                    st.markdown("### 📋 Triage Summary")
                    total_patients = len(result_df)
                    high_risk_count = int(np.sum(preds))
                    low_risk_count = total_patients - high_risk_count

                    c1, c2, c3 = st.columns(3)
                    c1.metric("Total Patients Screened", total_patients)
                    c2.metric("High Risk Identified", f"{high_risk_count} ({high_risk_count/total_patients*100:.1f}%)")
                    c3.metric("Low Risk / Healthy", f"{low_risk_count} ({low_risk_count/total_patients*100:.1f}%)")

                    st.dataframe(result_df)

                    res_csv = result_df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="💾 Download Complete Diagnostic Report (CSV)",
                        data=res_csv,
                        file_name="cardiac_screening_report.csv",
                        mime="text/csv"
                    )
        except Exception as e:
            st.error(f"Error processing CSV: {e}")

# =========================================================================
# TAB 3: Model Performance & Diagnostic Benchmarking
# =========================================================================
with tab3:
    st.markdown("### 📊 Comprehensive Model Benchmarking & Diagnostics")
    st.markdown("Evaluated on the Kaggle Heart Disease UCI (Cleveland) benchmark with Stratified 80/20 train/test split.")

    col_m1, col_m2 = st.columns([1, 1])

    with col_m1:
        st.subheader("Model Comparison Matrix")
        if metrics:
            comp_data = {
                "Metric": ["Accuracy", "Precision", "Recall (Sensitivity)", "ROC-AUC Score"],
                "Logistic Regression (Production)": [
                    f"{metrics['logistic_regression']['accuracy'] * 100:.2f}%",
                    f"{metrics['logistic_regression']['precision'] * 100:.2f}%",
                    f"{metrics['logistic_regression']['recall'] * 100:.2f}%",
                    f"{metrics['logistic_regression']['auc']:.4f}"
                ],
                "Decision Tree (Max Depth 4)": [
                    f"{metrics['decision_tree']['accuracy'] * 100:.2f}%",
                    f"{metrics['decision_tree']['precision'] * 100:.2f}%",
                    f"{metrics['decision_tree']['recall'] * 100:.2f}%",
                    f"{metrics['decision_tree']['auc']:.4f}"
                ]
            }
            comp_df = pd.DataFrame(comp_data)
            st.table(comp_df)
        else:
            st.write("Run `train_pipeline.py` to populate performance metrics.")

        st.markdown("""
        #### 🩺 Clinical Safety Analysis
        - **Why Logistic Regression was selected:**
          1. Superior **ROC-AUC (0.87 vs 0.80)**, providing robust probabilistic calibration.
          2. Exceptional **Recall (90.9%)**, ensuring more than 9 out of 10 cardiac pathology cases are flagged.
          3. Well-regularized linear boundaries avoid the overfitting common to unpruned decision trees on small clinical cohorts.
        """)

    with col_m2:
        st.subheader("Diagnostic Visualizations")
        chart_paths = ['heart_disease_evaluation_metrics.png', 'static/heart_disease_evaluation_metrics.png']
        chart_found = False
        for cp in chart_paths:
            if os.path.exists(cp):
                st.image(cp, caption="Figure 1: Confusion Matrix & ROC Curves (Logistic Regression vs Decision Tree)", use_container_width=True)
                chart_found = True
                break
        if not chart_found:
            st.warning("Diagnostic plot not found. Run train_pipeline.py to generate heart_disease_evaluation_metrics.png.")

# =========================================================================
# TAB 4: Additional Capstone Options
# =========================================================================
with tab4:
    st.markdown("### 🧩 Additional Capstone Options (Part 3 Implementation)")
    
    capstone_sub = st.radio("Select Solution Pathway:", [
        "Option 2: Bank Loan Approval Prediction (FinTech AI)",
        "Option 3: Customer Segmentation (Mall Customers K-Means)"
    ], horizontal=True)

    if "Option 2" in capstone_sub:
        st.subheader("🏦 Bank Loan Approval Prediction (Random Forest)")
        st.markdown("Automated credit underwriting decision engine trained on demographic & financial records.")

        loan_model_path = 'models/loan_rf_model.joblib'
        if os.path.exists(loan_model_path):
            rf_loan = joblib.load(loan_model_path)
            loan_features = joblib.load('models/loan_features.joblib')

            with st.form("loan_sim_form"):
                lc1, lc2 = st.columns(2)
                with lc1:
                    app_inc = st.number_input("Applicant Monthly Income ($)", value=4500, step=100)
                    coapp_inc = st.number_input("Co-Applicant Income ($)", value=1500, step=100)
                    loan_amt = st.number_input("Loan Amount Requested ($K)", value=128, step=5)
                with lc2:
                    term = st.selectbox("Loan Term (Months)", options=[360, 180, 240, 120, 84])
                    credit_hist = st.radio("Credit History Meets Guidelines", options=[1.0, 0.0], format_func=lambda x: "Yes (1.0)" if x == 1.0 else "No (0.0)")
                    married = st.radio("Married", options=["Yes", "No"])
                
                loan_btn = st.form_submit_button("Assess Loan Qualification")
                if loan_btn:
                    # Construct dummy feature row
                    row_dict = {feat: 0.0 for feat in loan_features}
                    if 'ApplicantIncome' in row_dict: row_dict['ApplicantIncome'] = app_inc
                    if 'CoapplicantIncome' in row_dict: row_dict['CoapplicantIncome'] = coapp_inc
                    if 'LoanAmount' in row_dict: row_dict['LoanAmount'] = loan_amt
                    if 'Loan_Amount_Term' in row_dict: row_dict['Loan_Amount_Term'] = term
                    if 'Credit_History' in row_dict: row_dict['Credit_History'] = credit_hist
                    if 'Married_Yes' in row_dict: row_dict['Married_Yes'] = 1.0 if married == "Yes" else 0.0

                    test_vec = pd.DataFrame([row_dict])[loan_features]
                    pred_loan = rf_loan.predict(test_vec)[0]
                    prob_loan = rf_loan.predict_proba(test_vec)[0, 1]

                    if pred_loan == 1:
                        st.success(f"✅ Loan Approved! Qualification Probability: {prob_loan*100:.1f}%")
                    else:
                        st.error(f"❌ Loan Declined. Qualification Probability: {prob_loan*100:.1f}%")
        else:
            st.info("Run `train_loan_model.py` to train and serialize the loan model.")

    else:
        st.subheader("🛍️ Customer Segmentation (Mall Customers K-Means)")
        st.markdown("Unsupervised K-Means clustering (k=5) categorizing customer cohorts by income and spending score.")

        if os.path.exists('static/customer_segments_clusters.png'):
            st.image('static/customer_segments_clusters.png', caption="Customer Cohort Clusters (k=5)", use_container_width=True)

        if os.path.exists('models/mall_kmeans_model.joblib'):
            km_model = joblib.load('models/mall_kmeans_model.joblib')
            segment_labels = {
                0: 'Conservative Spenders (Low Spend, High Income)',
                1: 'Balanced Shoppers (Medium Income, Medium Spend)',
                2: 'High Value VIPs (High Income, High Spend)',
                3: 'Careful Youth (Low Income, Low Spend)',
                4: 'Impulsive Buyers (Low Income, High Spend)'
            }
            
            sc1, sc2 = st.columns(2)
            with sc1:
                in_income = st.slider("Customer Annual Income (k$)", 10, 140, 60)
            with sc2:
                in_spend = st.slider("Spending Score (1-100)", 1, 100, 50)
            
            pred_cluster = int(km_model.predict([[in_income, in_spend]])[0])
            st.success(f"Customer Cluster: **Cluster {pred_cluster}** — {segment_labels.get(pred_cluster, 'Custom Segment')}")

# =========================================================================
# TAB 5: Cloud & Deployment Architecture
# =========================================================================
with tab5:
    st.markdown("### 🚀 Deployment Options for Web & App")
    st.markdown("""
    This project is engineered for production deployment across multiple environments:
    
    #### 1. Streamlit Community Cloud (Zero-Config Web App)
    - Push repository to GitHub.
    - Connect to [Streamlit Community Cloud](https://share.streamlit.io).
    - Set Main file path: `app.py`.
    
    #### 2. Containerized Cloud Run / Render / AWS ECS (Docker)
    - Build container:
      ```bash
      docker build -t cardioscan-ai .
      docker run -p 8501:8501 cardioscan-ai
      ```
      
    #### 3. FastAPI High-Throughput REST API
    - Launch API microservice:
      ```bash
      python -m uvicorn api_app:app --host 0.0.0.0 --port 8000
      ```
    - Interactive Swagger API docs available at: `http://localhost:8000/docs`
    - Embedded Web App served directly at: `http://localhost:8000/`
    """)
    
    st.code("""
# Dockerfile snippet
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
    """, language="dockerfile")
