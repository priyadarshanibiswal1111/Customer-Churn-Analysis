import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report,
    roc_curve
)

# Load predictions
df = pd.read_csv(
    "data/processed/churn_predictions.csv"
)

y_actual = df["Actual_Churn"]
y_pred = df["Predicted_Churn"]
y_probability = df["Churn_Probability"]

# -----------------------------
# MODEL PERFORMANCE
# -----------------------------

accuracy = accuracy_score(y_actual, y_pred)
precision = precision_score(y_actual, y_pred)
recall = recall_score(y_actual, y_pred)
f1 = f1_score(y_actual, y_pred)
roc_auc = roc_auc_score(y_actual, y_probability)

print("\n--- MODEL PERFORMANCE ---")
print(f"Accuracy  : {accuracy:.4f}")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")
print(f"F1 Score  : {f1:.4f}")
print(f"ROC-AUC   : {roc_auc:.4f}")

# -----------------------------
# CLASSIFICATION REPORT
# -----------------------------

print("\n--- CLASSIFICATION REPORT ---")
print(
    classification_report(
        y_actual,
        y_pred,
        target_names=["No Churn", "Churn"]
    )
)

# -----------------------------
# CONFUSION MATRIX
# -----------------------------

cm = confusion_matrix(y_actual, y_pred)

print("\n--- CONFUSION MATRIX ---")
print(cm)

plt.figure(figsize=(7, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    xticklabels=["No Churn", "Churn"],
    yticklabels=["No Churn", "Churn"]
)

plt.title("Confusion Matrix - Logistic Regression")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()

plt.savefig(
    "outputs/confusion_matrix_logistic_regression.png"
)

plt.show()

# -----------------------------
# ROC CURVE
# -----------------------------

fpr, tpr, thresholds = roc_curve(
    y_actual,
    y_probability
)

plt.figure(figsize=(8, 6))

plt.plot(
    fpr,
    tpr,
    label=f"Logistic Regression (AUC = {roc_auc:.3f})"
)

plt.plot(
    [0, 1],
    [0, 1],
    linestyle="--"
)

plt.title("ROC Curve - Logistic Regression")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()

plt.tight_layout()

plt.savefig(
    "outputs/roc_curve_logistic_regression.png"
)

plt.show()

print("\n--- MODEL EVALUATION COMPLETED ---")
print("Evaluation charts saved in outputs folder.")