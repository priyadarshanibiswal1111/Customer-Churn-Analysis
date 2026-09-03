import pandas as pd
import matplotlib.pyplot as plt
import os

# Model performance results
results = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "Random Forest"
    ],
    "Accuracy": [
        0.8038,
        0.7477
    ],
    "Precision": [
        0.6476,
        0.5171
    ],
    "Recall": [
        0.5749,
        0.7701
    ],
    "F1 Score": [
        0.6091,
        0.6187
    ],
    "ROC-AUC": [
        0.8357,
        0.8346
    ]
})

print("\n--- MODEL COMPARISON ---")
print(results.to_string(index=False))

# Save comparison table
os.makedirs("outputs", exist_ok=True)

results.to_csv(
    "outputs/model_comparison.csv",
    index=False
)

# Create comparison chart
metrics = [
    "Accuracy",
    "Precision",
    "Recall",
    "F1 Score",
    "ROC-AUC"
]

x = range(len(metrics))
width = 0.35

plt.figure(figsize=(11, 6))

plt.bar(
    [i - width / 2 for i in x],
    results.loc[0, metrics],
    width=width,
    label="Logistic Regression"
)

plt.bar(
    [i + width / 2 for i in x],
    results.loc[1, metrics],
    width=width,
    label="Random Forest"
)

plt.xticks(x, metrics)
plt.ylabel("Score")
plt.title("Logistic Regression vs Random Forest")
plt.ylim(0, 1)
plt.legend()

plt.tight_layout()

plt.savefig(
    "outputs/model_comparison.png"
)

plt.show()

print("\n--- MODEL COMPARISON COMPLETED ---")
print("Comparison table saved successfully.")
print("Comparison chart saved successfully.")