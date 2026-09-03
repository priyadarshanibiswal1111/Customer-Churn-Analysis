import pandas as pd

# Load the raw dataset
df = pd.read_csv("data/raw/Telco-Customer-Churn.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Convert TotalCharges from text to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# Check missing values created after conversion
print("\n--- MISSING VALUES AFTER CONVERSION ---")
print(df.isnull().sum())

# Remove rows where TotalCharges is missing
df = df.dropna(subset=["TotalCharges"])

# Convert Churn into numeric format
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

# Save cleaned dataset
df.to_csv("data/cleaned/Telco-Customer-Churn-Cleaned.csv", index=False)

# Final information
print("\n--- CLEANED DATASET SHAPE ---")
print(df.shape)

print("\n--- CLEANED DATA TYPES ---")
print(df.dtypes)

print("\n--- CLEANING COMPLETED ---")
print("Cleaned dataset saved successfully.")