import pandas as pd
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# ---------------------------------
# 1. Load engineered dataset
# ---------------------------------

df = pd.read_csv(
    "data/processed/Telco-Customer-Churn-Engineered.csv"
)

# ---------------------------------
# 2. Separate features and target
# ---------------------------------

X = df.drop(columns=["Churn"])
y = df["Churn"]

print("\n--- DATA PREPARATION ---")
print(f"Features: {X.shape[1]}")
print(f"Target: Churn")

# ---------------------------------
# 3. Train-Test Split
# ---------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\n--- TRAIN TEST SPLIT ---")
print(f"Training records: {X_train.shape[0]}")
print(f"Testing records: {X_test.shape[0]}")

# ---------------------------------
# 4. Feature Scaling
# ---------------------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\n--- FEATURE SCALING ---")
print("StandardScaler applied successfully.")

# ---------------------------------
# 5. Train Logistic Regression
# ---------------------------------

model = LogisticRegression(
    max_iter=1000,
    random_state=42
)

model.fit(X_train_scaled, y_train)

print("\n--- MODEL TRAINING ---")
print("Logistic Regression trained successfully.")

# ---------------------------------
# 6. Generate Predictions
# ---------------------------------

y_pred = model.predict(X_test_scaled)
y_probability = model.predict_proba(X_test_scaled)[:, 1]

print("\n--- PREDICTIONS ---")
print("Predictions generated successfully.")

# ---------------------------------
# 7. Save Predictions
# ---------------------------------

os.makedirs("data/processed", exist_ok=True)

results = X_test.copy()
results["Actual_Churn"] = y_test.values
results["Predicted_Churn"] = y_pred
results["Churn_Probability"] = y_probability

results.to_csv(
    "data/processed/churn_predictions.csv",
    index=False
)

print("\n--- PREDICTIONS SAVED ---")
print("data/processed/churn_predictions.csv")

print("\n--- MODEL TRAINING COMPLETED ---")