import pandas as pd

# Load dataset
df = pd.read_csv("dataset/fake_reviews.csv")

print("First 5 rows:\n")
print(df.head())

print("\n----------------------")
print("Dataset Shape:")
print(df.shape)

print("\n----------------------")
print("Column Names:")
print(df.columns)

print("\n----------------------")
print("Missing Values:")
print(df.isnull().sum())

print("\n----------------------")
print("Label Distribution:")
print(df['label'].value_counts())