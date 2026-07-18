import os
import pandas as pd
import streamlit as st

import plotly.express as px
import plotly.graph_objects as go

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# =====================================================
# PAGE
# =====================================================

st.set_page_config(layout="wide")

st.title("📊 Analytics Dashboard")

st.write(
    "Interactive insights generated from the latest bulk prediction."
)

FILE_PATH = "history/latest_predictions.csv"

if not os.path.exists(FILE_PATH):

    st.warning(
        "No prediction results found. Please analyze a CSV first."
    )
    st.stop()

df = pd.read_csv(FILE_PATH)

# =====================================================
# SUMMARY
# =====================================================

total = len(df)

fake = (
    df["Prediction"] == "Fake Review"
).sum()

genuine = (
    df["Prediction"] == "Genuine Review"
).sum()

avg_confidence = round(
    df["Confidence (%)"].mean(),
    2
)

st.divider()

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("📄 Total Reviews", total)

with c2:
    st.metric("🔴 Fake Reviews", fake)

with c3:
    st.metric("🟢 Genuine Reviews", genuine)

with c4:
    st.metric(
        "🎯 Avg Confidence",
        f"{avg_confidence}%"
    )

st.divider()

# =====================================================
# CHARTS
# =====================================================

left, right = st.columns(2)

# -----------------------------------------------------
# DONUT
# -----------------------------------------------------

with left:

    st.subheader("Prediction Distribution")

    fig = px.pie(

        values=[fake, genuine],

        names=[
            "Fake",
            "Genuine"
        ],

        hole=0.55,

        color=[
            "Fake",
            "Genuine"
        ],

        color_discrete_map={
            "Fake":"#EF4444",
            "Genuine":"#22C55E"
        }
    )

    fig.update_layout(

        height=420,

        legend_title="",

        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -----------------------------------------------------
# BAR
# -----------------------------------------------------

with right:

    st.subheader("Review Counts")

    bar = px.bar(

        x=[
            "Fake",
            "Genuine"
        ],

        y=[
            fake,
            genuine
        ],

        color=[
            "Fake",
            "Genuine"
        ],

        color_discrete_map={
            "Fake":"#EF4444",
            "Genuine":"#22C55E"
        }
    )

    bar.update_layout(

        showlegend=False,

        xaxis_title="",

        yaxis_title="Reviews",

        height=420
    )

    st.plotly_chart(
        bar,
        use_container_width=True
    )

st.divider()

# =====================================================
# CONFIDENCE ANALYSIS
# =====================================================

left, right = st.columns(2)

# -----------------------------------------------------
# HISTOGRAM
# -----------------------------------------------------

with left:

    st.subheader("Confidence Distribution")

    hist = px.histogram(

        df,

        x="Confidence (%)",

        nbins=20,

        color_discrete_sequence=[
            "#3B82F6"
        ]
    )

    hist.update_layout(

        xaxis_title="Confidence (%)",

        yaxis_title="Reviews",

        height=400
    )

    st.plotly_chart(
        hist,
        use_container_width=True
    )

# -----------------------------------------------------
# BOXPLOT
# -----------------------------------------------------

with right:

    st.subheader("Confidence Spread")

    box = px.box(

        df,

        y="Confidence (%)",

        color_discrete_sequence=[
            "#8B5CF6"
        ]
    )

    box.update_layout(

        height=400,

        showlegend=False
    )

    st.plotly_chart(
        box,
        use_container_width=True
    )

st.divider()

# =====================================================
# CONFIDENCE STATS
# =====================================================

st.subheader("Confidence Statistics")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Average",
        f'{df["Confidence (%)"].mean():.2f}%'
    )

with c2:
    st.metric(
        "Highest",
        f'{df["Confidence (%)"].max():.2f}%'
    )

with c3:
    st.metric(
        "Lowest",
        f'{df["Confidence (%)"].min():.2f}%'
    )

with c4:
    st.metric(
        "Std Dev",
        f'{df["Confidence (%)"].std():.2f}'
    )

st.divider()

# =====================================================
# WORD ANALYSIS
# =====================================================

st.subheader("☁️ Word Analysis")

text = " ".join(
    df["Cleaned Review"]
    .fillna("")
    .astype(str)
)

if text.strip() != "":

    left, right = st.columns([2, 1])

    # -------------------------------------------------
    # Word Cloud
    # -------------------------------------------------

    with left:

        wc = WordCloud(
            width=1200,
            height=500,
            background_color="white",
            colormap="viridis",
            max_words=150
        ).generate(text)

        fig, ax = plt.subplots(figsize=(12, 5))

        ax.imshow(wc)

        ax.axis("off")

        st.pyplot(fig, use_container_width=True)

    # -------------------------------------------------
    # Top Words
    # -------------------------------------------------

    with right:

        words = text.split()

        freq = (
            pd.Series(words)
            .value_counts()
            .head(15)
            .sort_values()
        )

        fig_words = px.bar(

            x=freq.values,

            y=freq.index,

            orientation="h",

            color=freq.values,

            color_continuous_scale="Viridis"
        )

        fig_words.update_layout(

            title="Top 15 Words",

            xaxis_title="Frequency",

            yaxis_title="",

            coloraxis_showscale=False,

            height=500
        )

        st.plotly_chart(
            fig_words,
            use_container_width=True
        )

else:

    st.info("No cleaned review text available.")

st.divider()

# =====================================================
# REVIEW LENGTH ANALYSIS
# =====================================================

st.subheader("📝 Review Length Analysis")

review_lengths = (
    df["Cleaned Review"]
    .fillna("")
    .astype(str)
    .apply(lambda x: len(x.split()))
)

length_fig = px.histogram(

    x=review_lengths,

    nbins=20,

    color_discrete_sequence=["#3B82F6"]
)

length_fig.update_layout(

    xaxis_title="Words per Review",

    yaxis_title="Number of Reviews",

    height=400
)

st.plotly_chart(
    length_fig,
    use_container_width=True
)

st.divider()

# =====================================================
# DATASET
# =====================================================

with st.expander(
    "📋 View Prediction Dataset",
    expanded=False
):

    st.dataframe(
        df,
        use_container_width=True,
        height=450
    )

st.divider()

# =====================================================
# DATA QUALITY
# =====================================================

st.subheader("📈 Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Average Review Length",
        f"{review_lengths.mean():.1f} words"
    )

with col2:

    st.metric(
        "Longest Review",
        f"{review_lengths.max()} words"
    )

with col3:

    st.metric(
        "Shortest Review",
        f"{review_lengths.min()} words"
    )

st.divider()

# =====================================================
# FOOTER
# =====================================================

st.caption(
    "Analytics generated from the latest bulk prediction results using the Fake Review Detection System."
)