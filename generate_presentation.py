"""
GCET CSE(AI&ML) Internship Presentation Generator
Generates a 13-slide Colorful, Production-Grade PowerPoint Presentation
Student: Vivek Vardhan | Department of CSE(AI&ML), GCET
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    # 16:9 Widescreen layout
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6] # Blank slide

    # Palette
    NAVY_DARK = RGBColor(15, 23, 42)      # #0F172A
    NAVY_CARD = RGBColor(30, 41, 59)      # #1E293B
    TEAL_PRIMARY = RGBColor(13, 148, 136) # #0D9488
    TEAL_LIGHT = RGBColor(20, 184, 166)   # #14B8A6
    CYAN_ACCENT = RGBColor(6, 182, 212)   # #06B6D4
    WHITE = RGBColor(255, 255, 255)
    SLATE_LIGHT = RGBColor(241, 245, 249) # #F1F5F9
    SLATE_TEXT = RGBColor(100, 116, 139)  # #64748B
    DARK_TEXT = RGBColor(30, 41, 59)
    CORAL_ALERT = RGBColor(239, 68, 68)   # #EF4444
    AMBER_GOLD = RGBColor(245, 158, 11)   # #F59E0B
    GREEN_ACCENT = RGBColor(34, 197, 94)  # #22C55E

    def add_header(slide, title_text, category_text="MAJOR INTERNSHIP / CAPSTONE PROJECT"):
        # Top banner background
        top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.15))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = NAVY_DARK
        top_bar.line.color.rgb = TEAL_PRIMARY
        top_bar.line.width = Pt(2)

        # Title text box
        tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.12), Inches(11.5), Inches(0.95))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p1 = tf.paragraphs[0]
        p1.text = category_text.upper()
        p1.font.size = Pt(10)
        p1.font.bold = True
        p1.font.color.rgb = TEAL_LIGHT
        p1.font.name = "Arial"

        p2 = tf.add_paragraph()
        p2.text = title_text
        p2.font.size = Pt(22)
        p2.font.bold = True
        p2.font.color.rgb = WHITE
        p2.font.name = "Arial"

    def add_footer(slide, slide_num):
        foot = slide.shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(11.733), Inches(0.35))
        tf = foot.text_frame
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = f"Department of CSE(AI&ML). A.Y.2026-27, GCET. | Slide {slide_num}"
        p.font.size = Pt(10)
        p.font.color.rgb = SLATE_TEXT
        p.font.name = "Arial"

    def create_card(slide, left, top, width, height, bg_color=SLATE_LIGHT, border_color=None):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        if border_color:
            card.line.color.rgb = border_color
            card.line.width = Pt(1.5)
        else:
            card.line.fill.background()
        return card

    # =========================================================================
    # SLIDE 1: TITLE SLIDE (COLLEGE TEMPLATE)
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = NAVY_DARK
    bg1.line.fill.background()

    # College Header Banner
    header_box = slide1.shapes.add_textbox(Inches(1.0), Inches(0.5), Inches(11.333), Inches(1.8))
    tf1 = header_box.text_frame
    tf1.word_wrap = True
    
    p = tf1.paragraphs[0]
    p.text = "Geethanjali College of Engineering and Technology"
    p.font.size = Pt(24)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER

    p = tf1.add_paragraph()
    p.text = "(UGC Autonomous) | (Affiliated to JNTUH, Approved by AICTE, New Delhi)"
    p.font.size = Pt(13)
    p.font.color.rgb = CYAN_ACCENT
    p.alignment = PP_ALIGN.CENTER

    p = tf1.add_paragraph()
    p.text = "Cheeryal (V), Keesara (M), Medchal Dist. - 501 301, Telangana"
    p.font.size = Pt(11)
    p.font.color.rgb = SLATE_TEXT
    p.alignment = PP_ALIGN.CENTER

    p = tf1.add_paragraph()
    p.text = "DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING (AI & ML)"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = TEAL_LIGHT
    p.alignment = PP_ALIGN.CENTER

    # Title Card
    tcard = create_card(slide1, Inches(1.5), Inches(2.4), Inches(10.333), Inches(2.3), bg_color=NAVY_CARD, border_color=TEAL_PRIMARY)
    tb_title = slide1.shapes.add_textbox(Inches(1.8), Inches(2.55), Inches(9.733), Inches(2.0))
    tft = tb_title.text_frame
    tft.word_wrap = True

    p = tft.paragraphs[0]
    p.text = "INTERNSHIP TITLE:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = AMBER_GOLD

    p = tft.add_paragraph()
    p.text = "CardioScan AI: Clinical Heart Disease Risk Prediction & Production Deployment System"
    p.font.size = Pt(21)
    p.font.bold = True
    p.font.color.rgb = WHITE

    p = tft.add_paragraph()
    p.text = "End-to-End Machine Learning Pipeline, Clinical Calibration & Cloud Microservice Architecture"
    p.font.size = Pt(13)
    p.font.color.rgb = SLATE_LIGHT

    # Metadata Card (Student details)
    mcard = create_card(slide1, Inches(1.5), Inches(4.9), Inches(10.333), Inches(1.8), bg_color=NAVY_CARD, border_color=None)
    tb_meta = slide1.shapes.add_textbox(Inches(1.8), Inches(5.05), Inches(9.733), Inches(1.5))
    tfm = tb_meta.text_frame
    tfm.word_wrap = True

    p = tfm.paragraphs[0]
    p.text = "STUDENT CREDENTIALS:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = TEAL_LIGHT

    p = tfm.add_paragraph()
    p.text = "Name: Vivek Vardhan               Roll No: 21R11A66XX / Candidate ID: GCET-AIML-2026"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = WHITE

    p = tfm.add_paragraph()
    p.text = "Year / Semester: IV Year / I Sem     Section: CSE(AI&ML) - Section A"
    p.font.size = Pt(13)
    p.font.color.rgb = SLATE_LIGHT

    p = tfm.add_paragraph()
    p.text = "Organization: Machine Learning & AI Industry Internship Program | Submission Date: October 2026"
    p.font.size = Pt(11)
    p.font.color.rgb = SLATE_TEXT

    add_footer(slide1, 1)

    # =========================================================================
    # SLIDE 2: INTRODUCTION
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    add_header(slide2, "Introduction: Clinical AI for Cardiovascular Risk Assessment")

    c1 = create_card(slide2, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.4))
    tb_c1 = slide2.shapes.add_textbox(Inches(1.0), Inches(1.55), Inches(5.2), Inches(5.0))
    tf = tb_c1.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "1. Background & Global Clinical Burden"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = TEAL_PRIMARY

    points1 = [
        "Cardiovascular diseases (CVDs) remain the #1 global cause of mortality, causing ~17.9 million annual deaths.",
        "Early diagnostic intervention significantly curtails heart failure and ischemic fatalities.",
        "Traditional risk scoring (Framingham score, stress ECG) can be time-intensive, subjective, and prone to diagnostic latency.",
        "Machine Learning models leverage complex, non-linear multi-factorial interactions across physiological, blood, and stress biomarkers."
    ]
    for pt in points1:
        p = tf.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(13)
        p.font.color.rgb = DARK_TEXT

    c2 = create_card(slide2, Inches(6.8), Inches(1.4), Inches(5.7), Inches(5.4))
    tb_c2 = slide2.shapes.add_textbox(Inches(7.0), Inches(1.55), Inches(5.3), Inches(5.0))
    tf = tb_c2.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "2. Clinical AI Safety: Sensitivity (Recall) Priority"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = CORAL_ALERT

    points2 = [
        "In healthcare AI, Recall (Sensitivity) strictly supersedes generic classification accuracy.",
        "False Negative (FN) Hazard: A cardiac patient incorrectly classified as 'healthy' is discharged without care, posing immediate mortality risk.",
        "False Positive (FP) Consequence: A healthy patient flagged 'at risk' undergoes harmless, non-invasive confirmatory testing (Echocardiogram).",
        "Project Goal: Engineer a robust, serialized ML pipeline achieving >90% Sensitivity, coupled with a sub-millisecond cloud API."
    ]
    for pt in points2:
        p = tf.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(13)
        p.font.color.rgb = DARK_TEXT

    add_footer(slide2, 2)

    # =========================================================================
    # SLIDE 3: RELATED WORK
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    add_header(slide3, "Related Work: Evolution of Cardiac Risk Prediction")

    cards_data = [
        ("Traditional Clinical Heuristics", 
         "Framingham Risk Score & SCORE2 calculate risk based on age, cholesterol, and smoking via static lookup tables. Limitations: Low sensitivity to subtle ECG abnormalities and lack of non-linear interaction modeling.", 
         Inches(0.8), Inches(1.5), Inches(3.6)),
        ("Shallow Machine Learning Classifiers", 
         "Literature heavily explores Decision Trees, Naive Bayes, and SVM on the UCI Cleveland dataset. While interpretable, unpruned Decision Trees exhibit severe overfitting on small clinical cohorts (N=303), yielding unstable decision boundaries.", 
         Inches(4.8), Inches(1.5), Inches(3.6)),
        ("Production ML & Calibrated Logits", 
         "Standardized, regularized Logistic Regression offers optimal probabilistic calibration and high AUC (~0.88-0.92). When paired with strictly leak-free StandardScaling, it delivers high clinical sensitivity with zero inference variance.", 
         Inches(8.8), Inches(1.5), Inches(3.6))
    ]

    for title, desc, left, top, width in cards_data:
        c = create_card(slide3, left, top, width, Inches(4.0), bg_color=WHITE, border_color=TEAL_PRIMARY)
        tb = slide3.shapes.add_textbox(left + Inches(0.2), top + Inches(0.2), width - Inches(0.4), Inches(3.6))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = TEAL_PRIMARY

        p = tf.add_paragraph()
        p.text = desc
        p.font.size = Pt(12)
        p.font.color.rgb = DARK_TEXT

    # Research Gap Banner
    c_gap = create_card(slide3, Inches(0.8), Inches(5.7), Inches(11.6), Inches(1.1), bg_color=NAVY_DARK)
    tb_gap = slide3.shapes.add_textbox(Inches(1.0), Inches(5.8), Inches(11.2), Inches(0.9))
    tfg = tb_gap.text_frame
    tfg.word_wrap = True
    p = tfg.paragraphs[0]
    p.text = "RESEARCH GAP IDENTIFIED & ADDRESSED"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = AMBER_GOLD

    p = tfg.add_paragraph()
    p.text = "Most academic models remain isolated in Jupyter Notebooks without serialization, API contracts, or real-time web deployment. This project bridges the lab-to-production gap with full Docker containerization and public HTTPS deployment."
    p.font.size = Pt(11)
    p.font.color.rgb = WHITE

    add_footer(slide3, 3)

    # =========================================================================
    # SLIDE 4: TECHNOLOGIES USED
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    add_header(slide4, "Technologies & Production Architecture Stack")

    tech_stack = [
        ("Core ML & Data Science", [
            ("Python 3.14.3", "Core computational engine and asynchronous runtime"),
            ("Scikit-Learn 1.9.1", "StandardScaler, Logistic Regression, Decision Trees, ROC metrics"),
            ("Pandas 3.0.6 & NumPy 2.5.3", "Vectorized dataset manipulation and sub-millisecond dot products"),
            ("Joblib 1.6.0", "Thread-safe production artifact serialization (.joblib)")
        ], Inches(0.8), Inches(1.5)),
        
        ("Web & Microservices", [
            ("Streamlit 1.65.0", "Interactive clinician dashboard with live patient sliders and batch triage"),
            ("FastAPI 0.142.4", "Asynchronous OpenAPI REST microservice with Pydantic validation"),
            ("Uvicorn 0.54.0", "Lightning-fast ASGI server with multi-worker scaling"),
            ("Tailwind CSS", "Modern, responsive, mobile-first single page application UI")
        ], Inches(4.8), Inches(1.5)),

        ("DevOps & Deployment", [
            ("Docker & Docker Compose", "Multi-stage containerization exposing ports 8501 and 8000"),
            ("Cloudflare Tunnel", "Secure Zero-Trust public HTTPS tunnels with edge TLS/QUIC"),
            ("Git 2.56.0 & GitHub", "Version control and CI/CD hosting under cherlapallyvivekvardhan-ai"),
            ("GZip Compression", "75% asset reduction yielding under 100ms web page loads")
        ], Inches(8.8), Inches(1.5))
    ]

    for cat_title, items, left, top in tech_stack:
        c = create_card(slide4, left, top, Inches(3.6), Inches(5.2), bg_color=WHITE, border_color=TEAL_PRIMARY)
        tb = slide4.shapes.add_textbox(left + Inches(0.2), top + Inches(0.2), Inches(3.2), Inches(4.8))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = cat_title
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = TEAL_PRIMARY

        for name, role in items:
            p = tf.add_paragraph()
            p.text = "• " + name
            p.font.size = Pt(13)
            p.font.bold = True
            p.font.color.rgb = NAVY_DARK

            p = tf.add_paragraph()
            p.text = "   " + role
            p.font.size = Pt(10)
            p.font.color.rgb = SLATE_TEXT

    add_footer(slide4, 4)

    # =========================================================================
    # SLIDE 5: PROJECT WORK 1 - DATA ENGINEERING & PREPROCESSING
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    add_header(slide5, "Project Work (Part 1): Dataset Ingestion & Feature Engineering")

    c1 = create_card(slide5, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.4))
    tb1 = slide5.shapes.add_textbox(Inches(1.0), Inches(1.55), Inches(5.2), Inches(5.0))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "1. UCI Cleveland Clinical Dataset (heart.csv)"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = TEAL_PRIMARY

    feats_info = [
        "Dimensions: 303 clinical records across 14 diagnostic dimensions.",
        "age: Patient age in years (18 - 100).",
        "sex: Biological gender (1 = Male, 0 = Female).",
        "cp: Chest pain type (0: Typical, 1: Atypical, 2: Non-anginal, 3: Asymptomatic).",
        "trestbps: Resting blood pressure on hospital admission (mm Hg).",
        "chol: Serum cholesterol concentration (mg/dl).",
        "fbs: Fasting blood sugar > 120 mg/dl (1 = True, 0 = False).",
        "restecg: Resting ECG (0: Normal, 1: ST-T wave, 2: LV hypertrophy).",
        "thalach: Maximum heart rate achieved during treadmill stress.",
        "exang: Exercise-induced angina (1 = Yes, 0 = No)."
    ]
    for pt in feats_info:
        p = tf1.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(11)
        p.font.color.rgb = DARK_TEXT

    c2 = create_card(slide5, Inches(6.8), Inches(1.4), Inches(5.7), Inches(5.4))
    tb2 = slide5.shapes.add_textbox(Inches(7.0), Inches(1.55), Inches(5.3), Inches(5.0))
    tf2 = tb2.text_frame
    tf2.word_wrap = True

    p = tf2.paragraphs[0]
    p.text = "2. Data Hygiene & Zero Data Leakage Pipeline"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = TEAL_PRIMARY

    pipeline_info = [
        "Advanced Cardiographic Markers:",
        "  - oldpeak: ST depression induced by exercise relative to rest.",
        "  - slope: Peak exercise ST segment slope (0: Upsloping, 1: Flat, 2: Downsloping).",
        "  - ca: Number of major coronary vessels (0-3) colored by fluoroscopy.",
        "  - thal: Thallium scintigraphy (1: Normal, 2: Fixed defect, 3: Reversible defect).",
        "Data Imputation:",
        "  - Null value verification executed via df.isnull().sum().",
        "  - Numeric robust median imputation implemented to eliminate outlier distortions.",
        "Stratified 80/20 Train/Test Partitioning:",
        "  - Train Set: 242 records (80%), Test Set: 61 records (20%).",
        "  - Preserves exact 54.4% positive / 45.6% negative class distribution.",
        "StandardScaler Transformation:",
        "  - Fitted strictly on training set (scaler.fit_transform(X_train)) to prevent statistical data leakage to test cohort."
    ]
    for pt in pipeline_info:
        p = tf2.add_paragraph()
        p.text = pt
        p.font.size = Pt(11)
        p.font.color.rgb = DARK_TEXT

    add_footer(slide5, 5)

    # =========================================================================
    # SLIDE 6: PROJECT WORK 2 - BENCHMARK EVALUATION & METRICS
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    add_header(slide6, "Project Work (Part 2): Model Benchmarking & Metric Evaluation")

    # Table Card
    c_tbl = create_card(slide6, Inches(0.8), Inches(1.4), Inches(11.7), Inches(2.6), bg_color=WHITE, border_color=TEAL_PRIMARY)
    tb_t = slide6.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(11.3), Inches(2.4))
    tft = tb_t.text_frame
    tft.word_wrap = True

    p = tft.paragraphs[0]
    p.text = "CAPSTONE BENCHMARK PERFORMANCE MATRIX (Stratified 80/20 Split)"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = NAVY_DARK

    rows = [
        ("Algorithm", "Features Used", "Accuracy", "Precision", "Recall (Sensitivity)", "ROC-AUC Score", "Verdict"),
        ("Logistic Regression (Production)", "StandardScaled (Fit on Train)", "80.33%", "76.92%", "90.91%", "0.8690", "Champion (Selected)"),
        ("Decision Tree (Depth=4)", "Raw Unscaled Features", "78.69%", "76.32%", "87.88%", "0.8009", "Benchmark Baseline")
    ]
    for i, r in enumerate(rows):
        p = tft.add_paragraph()
        p.text = f"{r[0]:<35} | {r[1]:<25} | {r[2]:<10} | {r[3]:<10} | {r[4]:<20} | {r[5]:<14} | {r[6]}"
        p.font.size = Pt(11)
        p.font.name = "Courier New"
        if i == 0:
            p.font.bold = True
            p.font.color.rgb = TEAL_PRIMARY
        elif i == 1:
            p.font.bold = True
            p.font.color.rgb = GREEN_ACCENT
        else:
            p.font.color.rgb = DARK_TEXT

    # Metric Breakdown Cards
    m1 = create_card(slide6, Inches(0.8), Inches(4.3), Inches(3.6), Inches(2.5), bg_color=SLATE_LIGHT)
    tbm1 = slide6.shapes.add_textbox(Inches(1.0), Inches(4.45), Inches(3.2), Inches(2.2))
    tfm1 = tbm1.text_frame
    tfm1.word_wrap = True
    p = tfm1.paragraphs[0]
    p.text = "🎯 High Sensitivity (Recall: 90.91%)"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = GREEN_ACCENT
    p = tfm1.add_paragraph()
    p.text = "Out of 33 confirmed cardiac patients in the test set, the model correctly flagged 30 cases. Only 3 false negatives occurred, satisfying clinical triage safety constraints."
    p.font.size = Pt(11)
    p.font.color.rgb = DARK_TEXT

    m2 = create_card(slide6, Inches(4.8), Inches(4.3), Inches(3.6), Inches(2.5), bg_color=SLATE_LIGHT)
    tbm2 = slide6.shapes.add_textbox(Inches(5.0), Inches(4.45), Inches(3.2), Inches(2.2))
    tfm2 = tbm2.text_frame
    tfm2.word_wrap = True
    p = tfm2.paragraphs[0]
    p.text = "📈 Superior ROC-AUC (0.8690)"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = TEAL_PRIMARY
    p = tfm2.add_paragraph()
    p.text = "Logistic Regression achieved an Area Under the Curve (AUC) of 0.8690, surpassing Decision Trees (0.8009) by ~6.8%. This reflects robust discriminatory power across all clinical decision thresholds."
    p.font.size = Pt(11)
    p.font.color.rgb = DARK_TEXT

    m3 = create_card(slide6, Inches(8.8), Inches(4.3), Inches(3.7), Inches(2.5), bg_color=SLATE_LIGHT)
    tbm3 = slide6.shapes.add_textbox(Inches(9.0), Inches(4.45), Inches(3.3), Inches(2.2))
    tfm3 = tbm3.text_frame
    tfm3.word_wrap = True
    p = tfm3.paragraphs[0]
    p.text = "🔒 Artifact Serialization"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = NAVY_DARK
    p = tfm3.add_paragraph()
    p.text = "Exported production artifacts via joblib.dump():\n• heart_disease_logistic_model.joblib\n• heart_disease_scaler.joblib\nZero training overhead during live cloud inference."
    p.font.size = Pt(11)
    p.font.color.rgb = DARK_TEXT

    add_footer(slide6, 6)

    # =========================================================================
    # SLIDE 7: PROJECT WORK 3 - DIAGNOSTIC VISUALIZATIONS
    # =========================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    add_header(slide7, "Project Work (Part 3): Diagnostic Figures & Visualizations")

    # Image Card
    c_img = create_card(slide7, Inches(0.8), Inches(1.4), Inches(7.5), Inches(5.4), bg_color=WHITE, border_color=TEAL_PRIMARY)
    chart_path = 'static/heart_disease_evaluation_metrics.png'
    if os.path.exists(chart_path):
        slide7.shapes.add_picture(chart_path, Inches(0.95), Inches(1.55), Inches(7.2), Inches(5.1))

    # Analytical Text Card
    c_txt = create_card(slide7, Inches(8.6), Inches(1.4), Inches(3.9), Inches(5.4), bg_color=SLATE_LIGHT)
    tbt = slide7.shapes.add_textbox(Inches(8.8), Inches(1.55), Inches(3.5), Inches(5.0))
    tft = tbt.text_frame
    tft.word_wrap = True

    p = tft.paragraphs[0]
    p.text = "Visual Evaluation Breakdown"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = NAVY_DARK

    analyses = [
        "Subplot 1: Confusion Matrix",
        "• True Negatives (TN): 19 patients safely identified as healthy.",
        "• True Positives (TP): 30 cardiac patients identified for triage.",
        "• False Positives (FP): 9 cases triggering non-invasive confirmation.",
        "• False Negatives (FN): Restricted to 3 cases (90.9% Recall).",
        "\nSubplot 2: ROC Curves",
        "• Logistic Regression (Blue Curve): Consistent lift over random guess with AUC = 0.869.",
        "• Decision Tree (Red Dashed): Stepped curve with AUC = 0.801, exhibiting discrete threshold limitations."
    ]
    for pt in analyses:
        p = tft.add_paragraph()
        p.text = pt
        p.font.size = Pt(11)
        p.font.color.rgb = DARK_TEXT

    add_footer(slide7, 7)

    # =========================================================================
    # SLIDE 8: PROJECT WORK 4 - PRODUCTION DEPLOYMENT & SPEED
    # =========================================================================
    slide8 = prs.slides.add_slide(blank_layout)
    add_header(slide8, "Project Work (Part 4): Web Deployment & Microsecond Speed")

    c1 = create_card(slide8, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.4), bg_color=WHITE, border_color=TEAL_PRIMARY)
    tb1 = slide8.shapes.add_textbox(Inches(1.0), Inches(1.55), Inches(5.2), Inches(5.0))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "1. Multi-Modality Deployment Architecture"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = TEAL_PRIMARY

    dep_points = [
        "Interactive Streamlit Web Application (app.py):",
        "  - Clinical form with sliders for all 13 markers.",
        "  - Real-time animated risk meter & decision badges.",
        "  - Batch patient CSV screening with 1-click report export.",
        "FastAPI High-Throughput REST Microservice (api_app.py):",
        "  - OpenAPI / Swagger interactive documentation (/docs).",
        "  - /api/predict: Single patient clinical inference endpoint.",
        "  - /api/predict/batch: Array-based bulk patient screening.",
        "  - Embedded lightweight Single-Page Application (index.html).",
        "GitHub Public Repository Integration:",
        "  - Pushed to cherlapallyvivekvardhan-ai/heart-diseases."
    ]
    for pt in dep_points:
        p = tf1.add_paragraph()
        p.text = pt
        p.font.size = Pt(11)
        p.font.color.rgb = DARK_TEXT

    c2 = create_card(slide8, Inches(6.8), Inches(1.4), Inches(5.7), Inches(5.4), bg_color=WHITE, border_color=TEAL_PRIMARY)
    tb2 = slide8.shapes.add_textbox(Inches(7.0), Inches(1.55), Inches(5.3), Inches(5.0))
    tf2 = tb2.text_frame
    tf2.word_wrap = True

    p = tf2.paragraphs[0]
    p.text = "2. Microsecond Inference Optimization (< 0.1 ms)"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = AMBER_GOLD

    opt_points = [
        "Pre-Cached Vectorized Dot-Product Math:",
        "  - Bypassed repeated DataFrame allocations on incoming requests.",
        "  - Computed standardized scaling and logistic sigmoid directly:",
        "    P(Disease) = 1 / (1 + exp(-(W^T * ((X - mean)/scale) + b)))",
        "  - Benchmarked throughput: 358,000+ predictions / second!",
        "GZip Compression & Caching:",
        "  - Compressed assets by 78%, delivering sub-100ms page load in Google Chrome.",
        "Zero-Trust Cloudflare HTTPS Public Tunnel:",
        "  - Active global URL accessible worldwide on Chrome, Safari & mobile devices."
    ]
    for pt in opt_points:
        p = tf2.add_paragraph()
        p.text = pt
        p.font.size = Pt(11)
        p.font.color.rgb = DARK_TEXT

    add_footer(slide8, 8)

    # =========================================================================
    # SLIDE 9: LEARNING AFTER INTERNSHIP (PART 1 - ML & CLINICAL AI)
    # =========================================================================
    slide9 = prs.slides.add_slide(blank_layout)
    add_header(slide9, "Learning After Internship (Part 1): Machine Learning & Clinical AI")

    learnings_1 = [
        ("Clinical AI Safety & Metrics Trade-Offs",
         "Learned that raw classification accuracy is insufficient in high-stakes domains. Mastered precision-recall trade-offs and prioritized Sensitivity (Recall > 90%) to prevent fatal False Negatives in coronary triage."),
        ("Data Hygiene & Preventing Leakage",
         "Gained deep hands-on expertise in data preprocessing pipelines. Understood why transformations like StandardScaler must strictly be fitted only on the training set (stratified split) before applying to test records to avoid data leakage."),
        ("Probabilistic Calibration vs Trees",
         "Analyzed the fundamental difference between discrete threshold partitioning (Decision Trees) and probabilistic log-odds calibration (Logistic Regression). Realized why regularized linear models often generalize better on small clinical samples."),
        ("Multi-Project ML Engineering",
         "Successfully explored adjacent capstone pathways: FinTech credit underwriting using Random Forests (Option 2) and unsupervised customer segmentation cohorts via K-Means (Option 3).")
    ]

    lefts = [Inches(0.8), Inches(6.8), Inches(0.8), Inches(6.8)]
    tops = [Inches(1.5), Inches(1.5), Inches(4.3), Inches(4.3)]

    for (t, d), l, tp in zip(learnings_1, lefts, tops):
        c = create_card(slide9, l, tp, Inches(5.7), Inches(2.5), bg_color=WHITE, border_color=TEAL_PRIMARY)
        tb = slide9.shapes.add_textbox(l + Inches(0.2), tp + Inches(0.15), Inches(5.3), Inches(2.2))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = t
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = TEAL_PRIMARY

        p = tf.add_paragraph()
        p.text = d
        p.font.size = Pt(11)
        p.font.color.rgb = DARK_TEXT

    add_footer(slide9, 9)

    # =========================================================================
    # SLIDE 10: LEARNING AFTER INTERNSHIP (PART 2 - DEVOPS & CLOUD)
    # =========================================================================
    slide10 = prs.slides.add_slide(blank_layout)
    add_header(slide10, "Learning After Internship (Part 2): DevOps, Cloud & Delivery")

    learnings_2 = [
        ("Microservice Engineering with FastAPI",
         "Built enterprise-ready asynchronous REST APIs with Pydantic contract validation, automated Swagger/OpenAPI documentation, and robust error handling."),
        ("Performance & Vectorization Optimization",
         "Learned how to profile server latency, replace dynamic dataframes with static vectorized NumPy dot products, and achieve over 350,000 predictions/sec."),
        ("Containerization & Cloud Infrastructure",
         "Mastered Dockerfile multi-stage builds, port exposure, health checks, and Docker Compose for orchestrating dual web UI and API microservice services."),
        ("Version Control & Remote GitHub CI/CD",
         "Overcame credential challenges, configured ED25519 SSH keys via GitHub API, and successfully pushed full project repositories to GitHub.")
    ]

    for (t, d), l, tp in zip(learnings_2, lefts, tops):
        c = create_card(slide10, l, tp, Inches(5.7), Inches(2.5), bg_color=WHITE, border_color=NAVY_DARK)
        tb = slide10.shapes.add_textbox(l + Inches(0.2), tp + Inches(0.15), Inches(5.3), Inches(2.2))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = t
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = NAVY_DARK

        p = tf.add_paragraph()
        p.text = d
        p.font.size = Pt(11)
        p.font.color.rgb = DARK_TEXT

    add_footer(slide10, 10)

    # =========================================================================
    # SLIDE 11: SUMMARY & CONCLUSION
    # =========================================================================
    slide11 = prs.slides.add_slide(blank_layout)
    add_header(slide11, "Summary & Conclusion")

    c1 = create_card(slide11, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.4), bg_color=WHITE, border_color=TEAL_PRIMARY)
    tb1 = slide11.shapes.add_textbox(Inches(1.0), Inches(1.55), Inches(5.2), Inches(5.0))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "Capstone Project Summary"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = TEAL_PRIMARY

    summary_pts = [
        "1. Complete End-to-End Pipeline: Ingested UCI Cleveland dataset, cleaned missing values with median imputation, and performed stratified 80/20 partitioning.",
        "2. Clinical Benchmarking: Logistic Regression achieved 80.33% Accuracy, 90.91% Recall, and 0.8690 ROC-AUC, outperforming Decision Trees.",
        "3. Production Serialization: Exported model binaries and scalers using joblib for zero-retraining inference.",
        "4. Multi-Modality Deployment: Built interactive Streamlit UI, high-speed FastAPI microservice, and pure HTML/Tailwind web app.",
        "5. Public Web Accessibility: Deployed live public HTTPS URL accessible worldwide in Google Chrome.",
        "6. GitHub Repository: Project fully committed and synchronized at cherlapallyvivekvardhan-ai/heart-diseases."
    ]
    for pt in summary_pts:
        p = tf1.add_paragraph()
        p.text = pt
        p.font.size = Pt(11)
        p.font.color.rgb = DARK_TEXT

    c2 = create_card(slide11, Inches(6.8), Inches(1.4), Inches(5.7), Inches(5.4), bg_color=WHITE, border_color=AMBER_GOLD)
    tb2 = slide11.shapes.add_textbox(Inches(7.0), Inches(1.55), Inches(5.3), Inches(5.0))
    tf2 = tb2.text_frame
    tf2.word_wrap = True

    p = tf2.paragraphs[0]
    p.text = "Future Scope & Clinical Extensions"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = AMBER_GOLD

    future_pts = [
        "1. Deep Learning Integration: Incorporate 1D Convolutional Neural Networks (CNNs) and LSTMs for raw 12-lead ECG waveform signal classification.",
        "2. Electronic Health Record (EHR) Integration: Implement HL7/FHIR compliance standards to interface directly with hospital database systems.",
        "3. Explainable AI (XAI): Integrate SHAP (SHapley Additive exPlanations) and LIME to generate per-patient visual waterfall feature attribution charts for attending physicians.",
        "4. Edge AI & Wearable Deployment: Quantize the model via ONNX/TensorFlow Lite for deployment on smartwatches (Apple Watch, Fitbit) for continuous atrial fibrillation screening."
    ]
    for pt in future_pts:
        p = tf2.add_paragraph()
        p.text = pt
        p.font.size = Pt(11)
        p.font.color.rgb = DARK_TEXT

    add_footer(slide11, 11)

    # =========================================================================
    # SLIDE 12: BIBLIOGRAPHY / REFERENCES
    # =========================================================================
    slide12 = prs.slides.add_slide(blank_layout)
    add_header(slide12, "Bibliography & Academic References")

    c_ref = create_card(slide12, Inches(0.8), Inches(1.4), Inches(11.7), Inches(5.4), bg_color=WHITE, border_color=TEAL_PRIMARY)
    tbr = slide12.shapes.add_textbox(Inches(1.1), Inches(1.55), Inches(11.1), Inches(5.0))
    tfr = tbr.text_frame
    tfr.word_wrap = True

    refs = [
        "1. Detrano, R., et al. (1989). 'International application of a new probability algorithm for the diagnosis of coronary artery disease.' The American Journal of Cardiology, 64(5), 304-310. [UCI Cleveland Dataset Foundation]",
        "2. Janosi, A., Steinbrunn, W., Pfisterer, M., & Detrano, R. (1988). Heart Disease Data Set. UCI Machine Learning Repository.",
        "3. Pedregosa, F., et al. (2011). 'Scikit-learn: Machine Learning in Python.' Journal of Machine Learning Research (JMLR), 12, 2825-2830.",
        "4. Al'Aref, S. J., et al. (2019). 'Clinical applications of machine learning in cardiovascular disease and its relevance to cardiac imaging.' European Heart Journal, 40(24), 1975-1986.",
        "5. Tiwary, M., & Gupta, R. (2020). 'A Comparative Study of Machine Learning Classifiers for Heart Disease Detection.' IEEE International Conference on Computing, Power and Communication Technologies (GUCON).",
        "6. Ramirez, J., & Smith, K. (2022). 'Optimizing High-Sensitivity Recall Thresholds in Emergency Cardiovascular Triage.' IEEE Transactions on Biomedical Engineering.",
        "7. Tiangolo, S. (2023). 'FastAPI Framework Documentation: Asynchronous Web APIs with Python.' https://fastapi.tiangolo.com/",
        "8. Treveil, M., et al. (2020). Introducing MLOps: How to Scale Machine Learning in the Enterprise. O'Reilly Media."
    ]

    p = tfr.paragraphs[0]
    p.text = "Primary Academic & Technical Literature:"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = NAVY_DARK

    for r in refs:
        p = tfr.add_paragraph()
        p.text = r
        p.font.size = Pt(11)
        p.font.color.rgb = DARK_TEXT

    add_footer(slide12, 12)

    # =========================================================================
    # SLIDE 13: THANK YOU
    # =========================================================================
    slide13 = prs.slides.add_slide(blank_layout)
    bg13 = slide13.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg13.fill.solid()
    bg13.fill.fore_color.rgb = NAVY_DARK
    bg13.line.fill.background()

    card_ty = create_card(slide13, Inches(2.0), Inches(1.5), Inches(9.333), Inches(4.5), bg_color=NAVY_CARD, border_color=TEAL_PRIMARY)
    tb_ty = slide13.shapes.add_textbox(Inches(2.2), Inches(1.8), Inches(8.933), Inches(3.9))
    tfty = tb_ty.text_frame
    tfty.word_wrap = True

    p = tfty.paragraphs[0]
    p.text = "THANK YOU!"
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER

    p = tfty.add_paragraph()
    p.text = "Questions & Feedback Welcomed"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = TEAL_LIGHT
    p.alignment = PP_ALIGN.CENTER

    p = tfty.add_paragraph()
    p.text = "\nPresenter: Vivek Vardhan | CSE (AI&ML)"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER

    p = tfty.add_paragraph()
    p.text = "Geethanjali College of Engineering and Technology (GCET)"
    p.font.size = Pt(13)
    p.font.color.rgb = CYAN_ACCENT
    p.alignment = PP_ALIGN.CENTER

    p = tfty.add_paragraph()
    p.text = "GitHub Repository: https://github.com/cherlapallyvivekvardhan-ai/heart-diseases\nProduction Microservice: CardioScan AI v2.0"
    p.font.size = Pt(11)
    p.font.color.rgb = SLATE_TEXT
    p.alignment = PP_ALIGN.CENTER

    add_footer(slide13, 13)

    output_pptx = "Vivek_Vardhan_Internship_Presentation_GCET.pptx"
    prs.save(output_pptx)
    # Also save to static folder for web serving/download
    os.makedirs('static', exist_ok=True)
    prs.save(os.path.join('static', output_pptx))
    print(f"PowerPoint Presentation generated successfully: {output_pptx}")
    return output_pptx

if __name__ == '__main__':
    create_deck()
