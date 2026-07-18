import os
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Prediction History",
    page_icon="📜",
    layout="wide"
)

st.title("📜 Prediction History")

st.write(
    "View the latest prediction results and summary."
)

FILE_PATH = "history/latest_predictions.csv"

# =====================================================
# CHECK FILE
# =====================================================

if not os.path.exists(FILE_PATH):

    st.warning(
        "No prediction history found.\n\nRun Bulk Upload first."
    )

    st.stop()

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv(FILE_PATH)

# =====================================================
# SUMMARY
# =====================================================

total = len(df)

fake = (df["Prediction"] == "Fake Review").sum()

genuine = (df["Prediction"] == "Genuine Review").sum()

avg_confidence = round(
    df["Confidence (%)"].mean(),
    2
)

fake_percent = round(
    fake / total * 100,
    2
)

st.subheader("📊 Latest Prediction Summary")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Total Reviews",
    total
)

c2.metric(
    "Fake Reviews",
    fake
)

c3.metric(
    "Genuine Reviews",
    genuine
)

c4.metric(
    "Avg Confidence",
    f"{avg_confidence}%"
)

st.progress(fake_percent / 100)

if fake_percent >= 70:

    st.error(
        "High number of fake reviews detected."
    )

elif fake_percent >= 40:

    st.warning(
        "Moderate number of fake reviews detected."
    )

else:

    st.success(
        "Most reviews appear genuine."
    )

st.divider()

# =====================================================
# SEARCH
# =====================================================

st.subheader("🔎 Search Reviews")

search = st.text_input(
    "Search review text"
)

display_df = df.copy()

if search:

    review_col = None

    for col in df.columns:

        if col.lower() in [
            "review",
            "reviews",
            "text",
            "content"
        ]:

            review_col = col
            break

    if review_col:

        display_df = df[
            df[review_col]
            .astype(str)
            .str.contains(
                search,
                case=False,
                na=False
            )
        ]

# =====================================================
# DATASET
# =====================================================

st.subheader("📄 Prediction Dataset")

st.dataframe(
    display_df,
    use_container_width=True,
    height=450
)

st.divider()

# =====================================================
# PREDICTION COUNTS
# =====================================================

st.subheader("📈 Prediction Counts")

counts = display_df["Prediction"].value_counts()

st.bar_chart(counts)

st.divider()

# =====================================================
# DOWNLOAD
# =====================================================

csv = df.to_csv(
    index=False
).encode("utf-8")

st.download_button(

    "⬇ Download Latest Prediction",

    data=csv,

    file_name="latest_predictions.csv",

    mime="text/csv",

    use_container_width=True
)

st.divider()

# =====================================================
# FILE DETAILS
# =====================================================

st.subheader("📁 File Information")

size = round(
    os.path.getsize(FILE_PATH) / 1024,
    2
)

modified = os.path.getmtime(FILE_PATH)

from datetime import datetime

modified = datetime.fromtimestamp(
    modified
)

left, right = st.columns(2)

with left:

    st.info(f"""
**File**

latest_predictions.csv

**Rows**

{total}

**Size**

{size} KB
""")

with right:

    st.info(f"""
**Last Updated**

{modified.strftime("%d-%m-%Y %I:%M %p")}

**Status**

Available
""")

st.divider()

st.caption(
    "Prediction History • Fake Review Detection System"
)