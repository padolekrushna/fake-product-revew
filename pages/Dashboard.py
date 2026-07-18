import os
from datetime import datetime

import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Fake Review Detection",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Fake Review Detection System")

st.markdown(
    """
Detect **Fake Product Reviews** using **Machine Learning** and
**Natural Language Processing (NLP)**.
"""
)

st.divider()

# ======================================================
# LOAD LATEST HISTORY
# ======================================================

FILE_PATH = "history/latest_predictions.csv"

if os.path.exists(FILE_PATH):

    df = pd.read_csv(FILE_PATH)

    total = len(df)
    fake = (df["Prediction"] == "Fake Review").sum()
    genuine = (df["Prediction"] == "Genuine Review").sum()
    avg_confidence = round(df["Confidence (%)"].mean(), 2)

else:

    df = None
    total = 0
    fake = 0
    genuine = 0
    avg_confidence = 0

# ======================================================
# METRICS
# ======================================================

st.subheader("📊 Overview")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Reviews", total)
c2.metric("Fake Reviews", fake)
c3.metric("Genuine Reviews", genuine)
c4.metric("Avg Confidence", f"{avg_confidence}%")

st.divider()

# ======================================================
# CHART + FILE INFO
# ======================================================

left, right = st.columns([2,1])

with left:

    st.subheader("Prediction Distribution")

    if df is not None:

        fig = px.pie(
            values=[fake, genuine],
            names=["Fake", "Genuine"],
            hole=0.5,
        )

        fig.update_layout(height=400)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:

        st.info("No prediction history available.")

with right:

    st.subheader("Latest Prediction")

    if os.path.exists(FILE_PATH):

        modified = datetime.fromtimestamp(
            os.path.getmtime(FILE_PATH)
        )

        st.success("History Available")

        st.write("**Dataset**")
        st.write("latest_predictions.csv")

        st.write("**Last Updated**")
        st.write(modified.strftime("%d-%m-%Y"))

        st.write("**Time**")
        st.write(modified.strftime("%I:%M %p"))

        st.write("**Reviews Processed**")
        st.write(total)

    else:

        st.warning("No history found.")

st.divider()

# ======================================================
# QUICK ACTIONS
# ======================================================

st.subheader("🚀 Quick Actions")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
### 📝 Single Review

Analyze one product review instantly.

**Use when:**
- Testing one review
- Quick verification
- Instant prediction
""")

with col2:
    st.info("""
### 📂 Bulk Upload

Upload a CSV file to analyze multiple reviews.

**Use when:**
- Large datasets
- Batch prediction
- Export results
""")

with col3:
    st.info("""
### 📊 Analytics

Visualize prediction results.

**Includes:**
- Charts
- Word Cloud
- Confidence Analysis
- Statistics
""")

st.divider()

# ======================================================
# MODEL INFORMATION
# ======================================================

st.subheader("🧠 Model Information")

m1, m2, m3, m4 = st.columns(4)

m1.metric("Algorithm", "Logistic Regression")
m2.metric("Vectorizer", "TF-IDF")
m3.metric("Dataset", "Amazon Reviews")
m4.metric("Accuracy", "73.48%")

st.divider()

# ======================================================
# PROJECT WORKFLOW
# ======================================================

st.subheader("⚙️ System Workflow")

st.code("""
Review Input
      │
      ▼
Text Cleaning
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Machine Learning Model
      │
      ▼
Prediction
      │
      ▼
Analytics & Reports
""")

st.divider()

# ======================================================
# PROJECT FEATURES
# ======================================================

st.subheader("✨ Features")

left, right = st.columns(2)

with left:
    st.markdown("""
- ✅ Single Review Prediction
- ✅ Bulk CSV Analysis
- ✅ Confidence Score
- ✅ Review Preprocessing
""")

with right:
    st.markdown("""
- ✅ Interactive Analytics
- ✅ Word Cloud
- ✅ Prediction History
- ✅ Download Results
""")

st.divider()

# ======================================================
# SYSTEM STATUS
# ======================================================

st.subheader("📌 System Status")

if os.path.exists(FILE_PATH):
    st.success("🟢 System Ready - Model Loaded Successfully")
else:
    st.warning("🟡 Waiting for prediction history. Run Bulk Upload to generate analytics.")

st.caption(
    "Fake Review Detection System • Version 1.0"
)