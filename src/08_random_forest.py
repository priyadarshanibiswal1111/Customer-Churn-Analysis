import pandas as pd
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

# Load engineered dataset
df = pd.read_csv(
    "data/processed/Telco-Customer-Churn-Engineered.csv"
)

# Separate features and target
X = df.drop(columns=["Churn"])
y = df["Churn"]

print("\n--- DATA PREPARATION ---")
print(f"Features: {X.shape[1]}")
print("Target: Churn")

# Train-test split
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

# Train Random Forest
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)

print("\n--- RANDOM FOREST TRAINING ---")
print("Random Forest trained successfully.")

# Predictions
y_pred = model.predict(X_test)
y_probability = model.predict_proba(X_test)[:, 1]

print("\n--- PREDICTIONS ---")
print("Predictions generated successfully.")

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_probability)

print("\n--- RANDOM FOREST PERFORMANCE ---")
print(f"Accuracy  : {accuracy:.4f}")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")
print(f"F1 Score  : {f1:.4f}")
print(f"ROC-AUC   : {roc_auc:.4f}")

# Save predictions
os.makedirs("data/processed", exist_ok=True)

results = X_test.copy()
results["Actual_Churn"] = y_test.values
results["Predicted_Churn"] = y_pred
results["Churn_Probability"] = y_probability

results.to_csv(
    "data/processed/random_forest_predictions.csv",
    index=False
)

print("\n--- PREDICTIONS SAVED ---")
print("data/processed/random_forest_predictions.csv")

print("\n--- RANDOM FOREST COMPLETED ---")