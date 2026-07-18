import os
import shutil
import streamlit as st

st.set_page_config(
    page_title="Settings",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ Settings")

st.write("Customize the Fake Review Detection System.")

# ==========================================================
# Initialize Defaults
# ==========================================================

defaults = {
    "show_confidence": True,
    "show_cleaned": True,
    "show_original": True,
    "rows_per_page": 25,
    "confidence_threshold": 60,
    "wordcloud_words": 100,
    "histogram_bins": 10,
    "save_history": True,
    "download_format": "CSV"
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ==========================================================
# Prediction Settings
# ==========================================================

st.subheader("🔍 Prediction Settings")

col1, col2 = st.columns(2)

with col1:

    st.session_state.show_confidence = st.checkbox(
        "Show Confidence Score",
        value=st.session_state.show_confidence
    )

    st.session_state.show_cleaned = st.checkbox(
        "Show Cleaned Review",
        value=st.session_state.show_cleaned
    )

with col2:

    st.session_state.show_original = st.checkbox(
        "Show Original Review",
        value=st.session_state.show_original
    )

    st.session_state.confidence_threshold = st.slider(
        "Confidence Threshold (%)",
        50,
        100,
        st.session_state.confidence_threshold
    )

st.divider()

# ==========================================================
# Table Settings
# ==========================================================

st.subheader("📋 Table Settings")

st.session_state.rows_per_page = st.selectbox(
    "Rows to Display",
    [10, 25, 50, 100],
    index=[10,25,50,100].index(st.session_state.rows_per_page)
)

st.divider()

# ==========================================================
# Analytics Settings
# ==========================================================

st.subheader("📊 Analytics Settings")

col1, col2 = st.columns(2)

with col1:

    st.session_state.wordcloud_words = st.slider(
        "Maximum WordCloud Words",
        50,
        300,
        st.session_state.wordcloud_words
    )

with col2:

    st.session_state.histogram_bins = st.slider(
        "Histogram Bins",
        5,
        30,
        st.session_state.histogram_bins
    )

st.divider()

# ==========================================================
# History
# ==========================================================

st.subheader("📂 History")

st.session_state.save_history = st.checkbox(
    "Automatically Save Prediction History",
    value=st.session_state.save_history
)

col1, col2 = st.columns(2)

with col1:

    if st.button("🗑 Clear Prediction History"):

        history_file = "history/latest_predictions.csv"

        if os.path.exists(history_file):
            os.remove(history_file)
            st.success("Prediction history deleted.")
        else:
            st.info("No history found.")

with col2:

    if st.button("🧹 Clear __pycache__"):

        removed = 0

        for root, dirs, files in os.walk("."):

            if "__pycache__" in dirs:

                shutil.rmtree(
                    os.path.join(root, "__pycache__"),
                    ignore_errors=True
                )

                removed += 1

        st.success(f"Removed {removed} cache folders.")

st.divider()

# ==========================================================
# Download
# ==========================================================

st.subheader("⬇ Download Settings")

st.session_state.download_format = st.radio(
    "Default Export Format",
    ["CSV", "Excel"],
    horizontal=True
)

st.divider()

# ==========================================================
# Model Information
# ==========================================================

st.subheader("🧠 Current Model")

c1, c2, c3 = st.columns(3)

c1.metric("Algorithm", "Logistic Regression")
c2.metric("Vectorizer", "TF-IDF")
c3.metric("Dataset", "Amazon Reviews")

st.divider()

# ==========================================================
# Reset
# ==========================================================

st.subheader("♻ Reset")

if st.button("Reset All Settings"):

    for key, value in defaults.items():
        st.session_state[key] = value

    st.success("Settings restored to default.")

st.divider()

st.success("✔ Settings saved for the current session.")