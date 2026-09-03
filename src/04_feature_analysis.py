import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned dataset
df = pd.read_csv("data/cleaned/Telco-Customer-Churn-Cleaned.csv")

# Make sure outputs folder exists
os.makedirs("outputs", exist_ok=True)

# ---------------------------------
# 1. Tenure Group Analysis
# ---------------------------------

df["TenureGroup"] = pd.cut(
    df["tenure"],
    bins=[-1, 6, 12, 24, 48, 72],
    labels=["0-6 Months", "7-12 Months", "13-24 Months", "25-48 Months", "49-72 Months"]
)

tenure_churn = (
    df.groupby("TenureGroup", observed=True)["Churn"]
    .mean()
    .mul(100)
)

print("\n--- CHURN RATE BY TENURE GROUP ---")
print(tenure_churn)

plt.figure(figsize=(9, 5))
tenure_churn.plot(kind="bar")
plt.title("Churn Rate by Customer Tenure")
plt.xlabel("Tenure Group")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("outputs/churn_by_tenure_group.png")
plt.show()


# ---------------------------------
# 2. Monthly Charges Analysis
# ---------------------------------

df["MonthlyChargeGroup"] = pd.cut(
    df["MonthlyCharges"],
    bins=[0, 40, 70, 100, float("inf")],
    labels=["Low (<$40)", "Medium ($40-$70)", "High ($70-$100)", "Very High (>$100)"]
)

charge_churn = (
    df.groupby("MonthlyChargeGroup", observed=True)["Churn"]
    .mean()
    .mul(100)
)

print("\n--- CHURN RATE BY MONTHLY CHARGES ---")
print(charge_churn)

plt.figure(figsize=(9, 5))
charge_churn.plot(kind="bar")
plt.title("Churn Rate by Monthly Charges")
plt.xlabel("Monthly Charge Group")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("outputs/churn_by_monthly_charges.png")
plt.show()


# ---------------------------------
# 3. Tech Support Analysis
# ---------------------------------

techsupport_churn = (
    df.groupby("TechSupport")["Churn"]
    .mean()
    .mul(100)
    .sort_values(ascending=False)
)

print("\n--- CHURN RATE BY TECH SUPPORT ---")
print(techsupport_churn)

plt.figure(figsize=(8, 5))
techsupport_churn.plot(kind="bar")
plt.title("Churn Rate by Tech Support")
plt.xlabel("Tech Support")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("outputs/churn_by_tech_support.png")
plt.show()


# ---------------------------------
# 4. Online Security Analysis
# ---------------------------------

security_churn = (
    df.groupby("OnlineSecurity")["Churn"]
    .mean()
    .mul(100)
    .sort_values(ascending=False)
)

print("\n--- CHURN RATE BY ONLINE SECURITY ---")
print(security_churn)

plt.figure(figsize=(8, 5))
security_churn.plot(kind="bar")
plt.title("Churn Rate by Online Security")
plt.xlabel("Online Security")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("outputs/churn_by_online_security.png")
plt.show()


# ---------------------------------
# 5. Senior Citizen Analysis
# ---------------------------------

senior_churn = (
    df.groupby("SeniorCitizen")["Churn"]
    .mean()
    .mul(100)
)

print("\n--- CHURN RATE BY SENIOR CITIZEN STATUS ---")
print(senior_churn)

plt.figure(figsize=(7, 5))
senior_churn.plot(kind="bar")
plt.title("Churn Rate by Senior Citizen Status")
plt.xlabel("Senior Citizen (0 = No, 1 = Yes)")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("outputs/churn_by_senior_status.png")
plt.show()


# ---------------------------------
# 6. High-Risk Customer Segments
# ---------------------------------

high_risk = df[
    (df["Contract"] == "Month-to-month") &
    (df["MonthlyCharges"] > 70) &
    (df["tenure"] <= 12)
]

print("\n--- HIGH-RISK CUSTOMER SEGMENT ---")
print(f"High-risk customers: {len(high_risk)}")
print(f"High-risk churn rate: {high_risk['Churn'].mean() * 100:.2f}%")

print("\n--- FEATURE ANALYSIS COMPLETED ---")
print("All feature analysis charts saved in outputs folder.")