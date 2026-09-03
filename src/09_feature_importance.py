import pandas as pd
import matplotlib.pyplot as plt
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


# -----------------------------
# LOAD DATA
# -----------------------------

df = pd.read_csv(
    "data/processed/Telco-Customer-Churn-Engineered.csv"
)

X = df.drop(columns=["Churn"])
y = df["Churn"]


# -----------------------------
# TRAIN TEST SPLIT
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# -----------------------------
# TRAIN RANDOM FOREST
# -----------------------------

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)


# -----------------------------
# FEATURE IMPORTANCE
# -----------------------------

feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

print("\n--- TOP 15 FEATURE IMPORTANCE ---")
print(feature_importance.head(15))


# -----------------------------
# TOP 10 FEATURES
# -----------------------------

top_features = feature_importance.head(10)

print("\n--- TOP 10 CHURN PREDICTORS ---")
print(top_features)


# -----------------------------
# SAVE FEATURE IMPORTANCE
# -----------------------------

os.makedirs("outputs", exist_ok=True)

feature_importance.to_csv(
    "outputs/feature_importance.csv",
    index=False
)


# -----------------------------
# CREATE CHART
# -----------------------------

plt.figure(figsize=(10, 6))

plt.barh(
    top_features["Feature"][::-1],
    top_features["Importance"][::-1]
)

plt.title("Top 10 Features for Customer Churn Prediction")
plt.xlabel("Feature Importance")
plt.ylabel("Feature")

plt.tight_layout()

plt.savefig(
    "outputs/top_10_feature_importance.png"
)

plt.show()


print("\n--- FEATURE IMPORTANCE COMPLETED ---")
print("Feature importance data saved successfully.")
print("Feature importance chart saved successfully.")