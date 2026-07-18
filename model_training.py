import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import LinearSVC

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)

from tabulate import tabulate

# =====================================================
# Load Dataset
# =====================================================

print("=" * 60)
print("Loading processed dataset...")
print("=" * 60)

df = pd.read_csv("dataset/processed_reviews.csv")

# Remove NaN
df = df.dropna(subset=["clean_review"])

# Remove empty reviews
df = df[df["clean_review"].str.strip() != ""]

print(f"Dataset Shape : {df.shape}")

X = df["clean_review"]
y = df["label"]

# =====================================================
# TF-IDF Vectorizer
# =====================================================

print("\nCreating TF-IDF features...")

vectorizer = TfidfVectorizer(
    max_features=20000,
    ngram_range=(1, 2),
    min_df=2,
    max_df=0.95,
    sublinear_tf=True,
)

X = vectorizer.fit_transform(X)

print("Feature Matrix Shape:", X.shape)

# =====================================================
# Train Test Split
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y,
)

print("\nTraining Samples :", X_train.shape[0])
print("Testing Samples  :", X_test.shape[0])

# =====================================================
# Models
# =====================================================

models = {
    "Naive Bayes": MultinomialNB(),

    "Logistic Regression":
        LogisticRegression(
            max_iter=1000,
            random_state=42,
        ),

    "Linear SVM":
        LinearSVC(
            random_state=42,
        ),

    "SGD Classifier":
        SGDClassifier(
            loss="hinge",
            random_state=42,
        ),
}

results = []

best_f1 = 0
best_accuracy = 0
best_model = None
best_model_name = ""

# =====================================================
# Train Models
# =====================================================

print("\nStarting Model Training...\n")

for name, model in models.items():

    print("=" * 60)
    print(name)
    print("=" * 60)

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions)
    recall = recall_score(y_test, predictions)
    f1 = f1_score(y_test, predictions)

    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")

    print("\nConfusion Matrix")

    print(confusion_matrix(y_test, predictions))

    results.append(
        [
            name,
            round(accuracy, 4),
            round(precision, 4),
            round(recall, 4),
            round(f1, 4),
        ]
    )

    if f1 > best_f1:
        best_f1 = f1
        best_accuracy = accuracy
        best_model = model
        best_model_name = name

# =====================================================
# Results Table
# =====================================================

print("\n")
print("=" * 60)
print("MODEL COMPARISON")
print("=" * 60)

headers = [
    "Model",
    "Accuracy",
    "Precision",
    "Recall",
    "F1 Score",
]

print(tabulate(results, headers=headers, tablefmt="grid"))

# =====================================================
# Save Results
# =====================================================

os.makedirs("models", exist_ok=True)

best_model = models["Logistic Regression"]
best_model_name = "Logistic Regression"

joblib.dump(best_model, "models/fake_review_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

results_df = pd.DataFrame(
    results,
    columns=headers,
)

results_df.to_csv(
    "models/model_results.csv",
    index=False,
)

print("\n")
print("=" * 60)
print("BEST MODEL")
print("=" * 60)

print(f"Model    : {best_model_name}")
print(f"Accuracy : {best_accuracy:.4f}")
print(f"F1 Score : {best_f1:.4f}")

print("\nModel saved to:")
print("models/fake_review_model.pkl")

print("Vectorizer saved to:")
print("models/vectorizer.pkl")

print("Results saved to:")
print("models/model_results.csv")

print("\nTraining Completed Successfully!")