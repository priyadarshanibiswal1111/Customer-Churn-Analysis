import pandas as pd
import os

# Load cleaned data
df = pd.read_csv(
    "data/cleaned/Telco-Customer-Churn-Cleaned.csv"
)

# -----------------------------
# BUSINESS INSIGHTS
# -----------------------------

insights = {
    "Insight": [
        "New customers have significantly higher churn risk.",
        "Month-to-month contracts have the highest churn rate.",
        "Customers with higher monthly charges show higher churn.",
        "Electronic check customers have a high churn rate.",
        "Customers without Tech Support show higher churn.",
        "Customers without Online Security show higher churn.",
        "A high-risk segment of new, high-paying, month-to-month customers was identified."
    ],

    "Evidence": [
        "0-6 month customers: 53.33% churn",
        "Month-to-month customers: 42.71% churn",
        "$70-$100 monthly charge group: 37.85% churn",
        "Electronic check customers: 45.29% churn",
        "Customers without Tech Support: 41.65% churn",
        "Customers without Online Security: 41.78% churn",
        "856 customers with a 69.04% churn rate"
    ],

    "Recommendation": [
        "Strengthen onboarding and retention programs during the first 6 months.",
        "Provide incentives to move customers toward longer-term contracts.",
        "Offer personalized pricing plans and service bundles.",
        "Encourage automatic payment methods through targeted incentives.",
        "Promote Tech Support packages to customers at higher churn risk.",
        "Promote Online Security packages to vulnerable customers.",
        "Prioritize this segment for proactive retention campaigns."
    ]
}

business_insights = pd.DataFrame(insights)

# Save business insights
os.makedirs("outputs", exist_ok=True)

business_insights.to_csv(
    "outputs/business_insights.csv",
    index=False
)

print("\n--- BUSINESS INSIGHTS ---")
print(business_insights.to_string(index=False))

print("\n--- BUSINESS INSIGHTS COMPLETED ---")
print("Business insights saved successfully.")