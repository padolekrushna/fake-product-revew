import os
import streamlit as st
import pandas as pd

from utils.predictor import predict_review

# =====================================================
# Page Title
# =====================================================

st.title("📂 Bulk Review Prediction")

st.write(
    "Upload a CSV file containing product reviews for batch prediction."
)

# =====================================================
# File Upload
# =====================================================

uploaded_file = st.file_uploader(
    "Choose a CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    # =====================================================
    # Read CSV
    # =====================================================

    try:
        df = pd.read_csv(uploaded_file)

    except Exception:
        st.error("❌ Unable to read CSV file.")
        st.stop()

    # =====================================================
    # Preview
    # =====================================================

    st.subheader("Dataset Preview")

    st.dataframe(
        df.head(),
        use_container_width=True
    )

    # =====================================================
    # Detect Review Column
    # =====================================================

    possible_columns = [
        "review",
        "Review",
        "reviews",
        "text",
        "Text",
        "content",
        "Content"
    ]

    review_column = None

    for col in possible_columns:

        if col in df.columns:
            review_column = col
            break

    if review_column is None:

        review_column = st.selectbox(
            "Select the Review Column",
            df.columns
        )

    st.success(f"Using review column: **{review_column}**")

    # =====================================================
    # Predict Button
    # =====================================================

    if st.button(
        "🔍 Analyze Reviews",
        use_container_width=True
    ):

        labels = []
        confidences = []
        cleaned_reviews = []

        progress = st.progress(0)

        total = len(df)

        for i, review in enumerate(df[review_column].fillna("")):

            result = predict_review(str(review))

            labels.append(result["label"])
            confidences.append(result["confidence"])
            cleaned_reviews.append(result["cleaned_review"])

            progress.progress((i + 1) / total)

        progress.empty()

        # =====================================================
        # Add Results
        # =====================================================

        df["Prediction"] = labels
        df["Confidence (%)"] = confidences
        df["Cleaned Review"] = cleaned_reviews

        # =====================================================
        # Save Latest Results
        # =====================================================

        os.makedirs("history", exist_ok=True)

        df.to_csv(
            "history/latest_predictions.csv",
            index=False
        )

        # =====================================================
        # Summary
        # =====================================================

        total_reviews = len(df)

        fake_reviews = (
            df["Prediction"] == "Fake Review"
        ).sum()

        genuine_reviews = total_reviews - fake_reviews

        fake_percent = (
            fake_reviews / total_reviews
        ) * 100

        st.divider()

        st.subheader("📊 Analysis Summary")

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric(
                "Total Reviews",
                total_reviews
            )

        with c2:
            st.metric(
                "Genuine Reviews",
                genuine_reviews
            )

        with c3:
            st.metric(
                "Fake Reviews",
                fake_reviews
            )

        with c4:
            st.metric(
                "Fake Rate",
                f"{fake_percent:.2f}%"
            )

        st.progress(fake_percent / 100)

        if fake_percent >= 70:

            st.error(
                "⚠️ A large number of reviews appear to be fake."
            )

        elif fake_percent >= 40:

            st.warning(
                "⚠️ Moderate number of fake reviews detected."
            )

        else:

            st.success(
                "✅ Majority of reviews appear to be genuine."
            )

        # =====================================================
        # Search
        # =====================================================

        st.divider()

        st.subheader("📋 Prediction Results")

        search = st.text_input(
            "Search Reviews",
            placeholder="Type a keyword..."
        )

        display_df = df.copy()

        if search:

            display_df = display_df[
                display_df[review_column]
                .astype(str)
                .str.contains(
                    search,
                    case=False,
                    na=False
                )
            ]

        # Show only useful columns
        st.dataframe(
            display_df[
                [
                    review_column,
                    "Prediction",
                    "Confidence (%)"
                ]
            ],
            use_container_width=True,
            height=450
        )

        # =====================================================
        # Cleaned Reviews
        # =====================================================

        with st.expander("🧹 View Preprocessed Reviews"):

            st.dataframe(
                display_df[
                    [
                        review_column,
                        "Cleaned Review"
                    ]
                ],
                use_container_width=True
            )

        # =====================================================
        # Download
        # =====================================================

        csv = df.to_csv(
            index=False
        ).encode("utf-8")

        st.divider()

        st.download_button(
            label="⬇ Download Results as CSV",
            data=csv,
            file_name="predicted_reviews.csv",
            mime="text/csv",
            use_container_width=True
        )

        st.success(
            "Results have been saved successfully. You can now view detailed insights on the Analytics page."
        )