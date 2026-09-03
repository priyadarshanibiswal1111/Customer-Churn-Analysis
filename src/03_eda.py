import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("data/cleaned/Telco-Customer-Churn-Cleaned.csv")

# Create outputs folder if needed
import os
os.makedirs("outputs", exist_ok=True)

# -----------------------------
# 1. Overall Churn Rate
# -----------------------------

churn_rate = df["Churn"].mean() * 100

print("\n--- OVERALL CHURN ANALYSIS ---")
print(f"Total Customers: {len(df)}")
print(f"Churned Customers: {df['Churn'].sum()}")
print(f"Churn Rate: {churn_rate:.2f}%")

# -----------------------------
# 2. Churn Distribution
# -----------------------------

plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="Churn")
plt.title("Customer Churn Distribution")
plt.xlabel("Churn (0 = No, 1 = Yes)")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("outputs/churn_distribution.png")
plt.show()

# -----------------------------
# 3. Churn by Contract
# -----------------------------

contract_churn = (
    df.groupby("Contract")["Churn"]
    .mean()
    .mul(100)
    .sort_values(ascending=False)
)

print("\n--- CHURN RATE BY CONTRACT ---")
print(contract_churn)

plt.figure(figsize=(8, 5))
contract_churn.plot(kind="bar")
plt.title("Churn Rate by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("outputs/churn_by_contract.png")
plt.show()

# -----------------------------
# 4. Churn by Internet Service
# -----------------------------

internet_churn = (
    df.groupby("InternetService")["Churn"]
    .mean()
    .mul(100)
    .sort_values(ascending=False)
)

print("\n--- CHURN RATE BY INTERNET SERVICE ---")
print(internet_churn)

plt.figure(figsize=(8, 5))
internet_churn.plot(kind="bar")
plt.title("Churn Rate by Internet Service")
plt.xlabel("Internet Service")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("outputs/churn_by_internet_service.png")
plt.show()

# -----------------------------
# 5. Churn by Payment Method
# -----------------------------

payment_churn = (
    df.groupby("PaymentMethod")["Churn"]
    .mean()
    .mul(100)
    .sort_values(ascending=False)
)

print("\n--- CHURN RATE BY PAYMENT METHOD ---")
print(payment_churn)

plt.figure(figsize=(10, 5))
payment_churn.plot(kind="bar")
plt.title("Churn Rate by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=25, ha="right")
plt.tight_layout()
plt.savefig("outputs/churn_by_payment_method.png")
plt.show()

# -----------------------------
# 6. Tenure vs Churn
# -----------------------------

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Churn", y="tenure")
plt.title("Customer Tenure vs Churn")
plt.xlabel("Churn (0 = No, 1 = Yes)")
plt.ylabel("Tenure (Months)")
plt.tight_layout()
plt.savefig("outputs/tenure_vs_churn.png")
plt.show()

# -----------------------------
# 7. Monthly Charges vs Churn
# -----------------------------

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Churn", y="MonthlyCharges")
plt.title("Monthly Charges vs Churn")
plt.xlabel("Churn (0 = No, 1 = Yes)")
plt.ylabel("Monthly Charges")
plt.tight_layout()
plt.savefig("outputs/monthly_charges_vs_churn.png")
plt.show()

print("\n--- EDA COMPLETED ---")
print("Charts saved in the outputs folder.")