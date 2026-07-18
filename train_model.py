import pandas as pd

from utils.preprocessing import clean_text

# Load dataset
df = pd.read_csv("dataset/fake_reviews.csv")

print("Original Shape:", df.shape)

# Remove missing values
df = df.dropna(subset=["title", "text"])

print("After removing missing values:", df.shape)

# Combine title and review text
df["review"] = df["title"] + " " + df["text"]

# Clean the review text
print("\nCleaning reviews...")

df["clean_review"] = df["review"].apply(clean_text)

print("\nSample Cleaned Reviews:\n")

for i in range(5):
    print("=" * 70)
    print("Original:")
    print(df["review"].iloc[i])
    print("\nCleaned:")
    print(df["clean_review"].iloc[i])

# Save processed dataset
df.to_csv("dataset/processed_reviews.csv", index=False)

print("\nProcessed dataset saved successfully!")