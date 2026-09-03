import pandas as pd
import os

# Load cleaned dataset
df = pd.read_csv("data/cleaned/Telco-Customer-Churn-Cleaned.csv")

# Remove customer ID because it does not help predict churn
df = df.drop(columns=["customerID"])

# Convert categorical variables into numerical variables
df = pd.get_dummies(
    df,
    columns=[
        "gender",
        "Partner",
        "Dependents",
        "PhoneService",
        "MultipleLines",
        "InternetService",
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies",
        "Contract",
        "PaperlessBilling",
        "PaymentMethod"
    ],
    drop_first=True,
    dtype=int
)

# Save engineered dataset
os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/Telco-Customer-Churn-Engineered.csv",
    index=False
)

# Display results
print("\n--- FEATURE ENGINEERING COMPLETED ---")

print("\nDataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nData Types:")
print(df.dtypes)

print("\nEngineered dataset saved successfully.")