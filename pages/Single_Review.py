import streamlit as st

from utils.predictor import predict_review
from utils.preprocessing import clean_text

# -------------------------------------------------------
# Page Title
# -------------------------------------------------------

st.title("📝 Single Review Prediction")

st.write(
    "Enter a product review below to check whether it is likely **genuine** or **fake**."
)

# -------------------------------------------------------
# Review Input
# -------------------------------------------------------

review = st.text_area(
    "Enter Product Review",
    height=200,
    placeholder="Example: This product exceeded my expectations..."
)

# -------------------------------------------------------
# Prediction
# -------------------------------------------------------

if st.button("🔍 Predict", use_container_width=True):

    if review.strip() == "":

        st.warning("⚠ Please enter a review.")

    else:

        label, confidence = predict_review(review)

        st.divider()

        st.subheader("Prediction Result")

        # -----------------------------------------------
        # Result + Confidence in two columns
        # -----------------------------------------------

        col1, col2 = st.columns(2)

        with col1:

            if label == "Fake Review":
                st.error("🔴 Fake Review Detected")
            else:
                st.success("🟢 Genuine Review")

        with col2:

            st.metric(
                "Confidence",
                f"{confidence:.2f}%"
            )

        # -----------------------------------------------
        # Confidence Progress Bar
        # -----------------------------------------------

        st.progress(confidence / 100)

        # -----------------------------------------------
        # Confidence Level
        # -----------------------------------------------

        if confidence >= 90:
            st.success("Confidence Level: Very High")

        elif confidence >= 75:
            st.info("Confidence Level: High")

        elif confidence >= 60:
            st.warning("Confidence Level: Moderate")

        else:
            st.error("Confidence Level: Low")

        # -----------------------------------------------
        # Original Review
        # -----------------------------------------------

        with st.expander("📄 Original Review"):

            st.write(review)

        # -----------------------------------------------
        # Cleaned Review
        # -----------------------------------------------

        with st.expander("🧹 Cleaned Review (After Preprocessing)"):

            st.code(clean_text(review))

        # -----------------------------------------------
        # Model Information
        # -----------------------------------------------

        st.caption(
            "Model: Logistic Regression | TF-IDF Vectorizer | Dataset: Amazon Fake Reviews"
        )