import streamlit as st

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Fake Product Review Detection",
    page_icon="🛒",
    layout="wide"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

/* Hero */

.title{
    font-size:44px;
    font-weight:700;
    color:#1F2937;
}

.subtitle{
    font-size:24px;
    font-weight:600;
    color:#2563EB;
}

.description{
    font-size:17px;
    color:#4B5563;
}

/* Card */

.card{
    background:white;
    border:1px solid #E5E7EB;
    border-radius:15px;
    padding:22px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.08);
    margin-bottom:20px;
}

.card-title{
    font-size:16px;
    color:#6B7280;
}

.card-value{
    font-size:28px;
    font-weight:bold;
    color:#111827;
    margin-top:8px;
}

.section-title{
    font-size:30px;
    font-weight:700;
    color:#1F2937;
    text-align:center;
    margin:20px 0px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# HERO SECTION
# ==========================================

st.markdown(
"""
<div class="title">
🛒 Fake Product Review Detection System
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class="subtitle">
Detect Fake Product Reviews using Machine Learning
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class="description">
Identify whether online product reviews are Genuine or Fake using Natural Language Processing (NLP)
and Machine Learning. The system supports both individual review prediction and bulk CSV analysis,
along with interactive analytics and downloadable reports.
</div>
""",
unsafe_allow_html=True
)

st.write("")
st.divider()

# ==========================================
# MODEL SUMMARY
# ==========================================

st.markdown(
"""
<div class="section-title">
📈 Model Summary
</div>
""",
unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-title">Accuracy</div>
        <div class="card-value">73.48%</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-title">Algorithm</div>
        <div class="card-value">Logistic Regression</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <div class="card-title">Vectorizer</div>
        <div class="card-value">TF-IDF</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card">
        <div class="card-title">Dataset</div>
        <div class="card-value">Amazon Reviews</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ==========================================
# APPLICATION MODULES
# ==========================================

st.markdown(
"""
<div class="section-title">
🚀 Application Modules
</div>
""",
unsafe_allow_html=True
)

row1_col1, row1_col2 = st.columns(2, gap="large")

with row1_col1:

    st.markdown("""
    <div class="card">

<h3>✍️ Single Review Prediction</h3>

Predict whether a single product review is
<b>Genuine</b> or <b>Fake</b> instantly.

<hr>

✅ Instant Prediction<br>
✅ Confidence Score<br>
✅ Cleaned Review Text

</div>
""", unsafe_allow_html=True)


with row1_col2:

    st.markdown("""
    <div class="card">

<h3>📂 Bulk CSV Prediction</h3>

Upload a CSV file containing multiple
product reviews for batch analysis.

<hr>

✅ Batch Prediction<br>
✅ Download Results<br>
✅ Progress Indicator

</div>
""", unsafe_allow_html=True)


# ==========================================

row2_col1, row2_col2 = st.columns(2, gap="large")

with row2_col1:

    st.markdown("""
    <div class="card">

<h3>📊 Analytics Dashboard</h3>

Visualize prediction results using
interactive charts and statistics.

<hr>

✅ Pie Charts<br>
✅ Word Cloud<br>
✅ Confidence Analysis

</div>
""", unsafe_allow_html=True)


with row2_col2:

    st.markdown("""
    <div class="card">

<h3>🕘 Prediction History</h3>

View previously generated prediction
results and download reports.

<hr>

✅ Prediction Logs<br>
✅ Download CSV<br>
✅ Summary Statistics

</div>
""", unsafe_allow_html=True)

st.divider()


# ==========================================
# WORKFLOW & SYSTEM STATUS
# ==========================================

st.markdown(
"""
<div class="section-title">
⚙️ System Workflow
</div>
""",
unsafe_allow_html=True
)

left, right = st.columns([2, 1], gap="large")

# ---------------- Workflow ----------------

with left:

    st.markdown("""
    <div class="card">

<h3>🔄 Prediction Workflow</h3>

📝 User enters Review

⬇️

🧹 Text Preprocessing

⬇️

📚 TF-IDF Vectorization

⬇️

🤖 Machine Learning Model

⬇️

✅ Genuine / Fake Prediction

    </div>
    """, unsafe_allow_html=True)

# ---------------- Status ----------------

with right:

    st.markdown("""
    <div class="card">

<h3>🟢 System Status</h3>

✅ Model Loaded

✅ Application Ready

✅ Analytics Ready

✅ History Enabled

    </div>
    """, unsafe_allow_html=True)

st.divider()

# ==========================================
# PROJECT INFORMATION
# ==========================================

st.markdown(
"""
<div class="section-title">
📋 Project Information
</div>
""",
unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
**Version**

1.0
""")

with col2:
    st.info("""
**Technology**

Python • Streamlit
""")

with col3:
    st.info("""
**Machine Learning**

TF-IDF + Logistic Regression
""")

st.divider()

# ==========================================
# FOOTER
# ==========================================

st.markdown(
"""
<div style="text-align:center;color:#6B7280;font-size:15px;padding-top:10px;">

🛒 <b>Fake Product Review Detection System</b><br>

Developed using Python, Streamlit, Scikit-learn, NLP and Machine Learning.

</div>
""",
unsafe_allow_html=True
)