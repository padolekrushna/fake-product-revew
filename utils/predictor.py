import joblib
import numpy as np

from utils.preprocessing import clean_text

# Load model once
model = joblib.load("models/fake_review_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")


def predict_review(review):
    """
    Predict whether a review is Fake or Genuine.

    Returns:
    {
        "label": str,
        "confidence": float,
        "cleaned_review": str
    }
    """

    cleaned = clean_text(review)

    vector = vectorizer.transform([cleaned])

    prediction = model.predict(vector)[0]

    # -----------------------------
    # Confidence
    # -----------------------------
    if hasattr(model, "predict_proba"):

        confidence = float(model.predict_proba(vector).max() * 100)

    elif hasattr(model, "decision_function"):

        score = model.decision_function(vector)[0]

        confidence = float((1 / (1 + np.exp(-abs(score)))) * 100)

    else:

        confidence = 80.0

    label = "Fake Review" if prediction == 1 else "Genuine Review"

    return {
        "label": label,
        "confidence": round(confidence, 2),
        "cleaned_review": cleaned,
    }