# Customer Churn Analysis & Prediction

## 📌 Project Overview

This project analyzes customer churn behavior and builds machine learning models to predict customers who are likely to leave a telecom service.

The project uses Python and machine learning techniques to identify important churn patterns, customer risk factors, and high-risk customer segments.

---

## 🎯 Business Objective

The main objectives of this project are:

- Analyze customer churn patterns
- Identify factors associated with customer churn
- Build machine learning models for churn prediction
- Identify high-risk customer segments
- Evaluate model performance using classification metrics
- Provide actionable business recommendations

---

## 📊 Dataset

**Dataset:** IBM Telco Customer Churn Dataset

- Original customers: 7,043
- Customers after cleaning: 7,032
- Original columns: 21
- Target variable: Churn

During data cleaning, 11 records with blank or invalid `TotalCharges` values were removed.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Git & GitHub

---

## 🔄 Project Workflow

1. Data Understanding
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Analysis
5. Feature Engineering
6. Logistic Regression Model Training
7. Model Evaluation
8. Random Forest Model Training
9. Feature Importance Analysis
10. Model Comparison
11. Business Insights

---

## 📈 Key Business Insights

### 1. Customer Tenure

Customers with 0–6 months of tenure have a churn rate of **53.33%**.

**Recommendation:** Strengthen onboarding and early-stage customer retention programs.

### 2. Contract Type

Month-to-month customers have the highest churn rate at **42.71%**.

**Recommendation:** Provide incentives to encourage customers to move toward longer-term contracts.

### 3. Monthly Charges

Customers paying $70–$100 per month have a churn rate of **37.85%**.

**Recommendation:** Consider personalized pricing plans and service bundles for high-charge customers.

### 4. Payment Method

Electronic check customers have a churn rate of **45.29%**.

**Recommendation:** Encourage automatic payment methods through targeted incentives.

### 5. Tech Support

Customers without Tech Support have a churn rate of **41.65%**.

**Recommendation:** Promote Tech Support packages to customers at higher churn risk.

### 6. Online Security

Customers without Online Security have a churn rate of **41.78%**.

**Recommendation:** Promote Online Security services to vulnerable customer segments.

---

## ⚠️ High-Risk Customer Segment

A high-risk customer segment was identified using the following conditions:

- Month-to-month contract
- Monthly charges above $70
- Tenure of 12 months or less

### Result

- Customers in segment: **856**
- Churn rate: **69.04%**

This segment should be prioritized for proactive customer retention campaigns.

> Note: This is a descriptive customer segment based on observed churn patterns and does not imply causation.

---

## 🤖 Machine Learning Models

Two classification models were evaluated:

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 80.38% | 64.76% | 57.49% | 60.91% | 83.57% |
| Random Forest | 74.77% | 51.71% | 77.01% | 61.87% | 83.46% |

### Model Selection

Random Forest was selected as the **business-focused model** because it achieved:

- Higher Recall: **77.01%**
- Slightly higher F1 Score: **61.87%**
- ROC-AUC: **83.46%**

Higher recall is useful in churn retention scenarios because identifying more potential churners can help the business take proactive action.

However, Random Forest has lower precision and accuracy than Logistic Regression, so model selection depends on the business cost of false positives versus missed churners.

---

## 🔍 Top Churn Predictors

The most important predictive features identified using Random Forest included:

- Tenure
- Total Charges
- Monthly Charges
- Contract Type
- Internet Service
- Payment Method
- Online Security
- Tech Support

Feature importance represents predictive contribution and does not necessarily imply causation.

---

## 💼 Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Data Visualization
- Machine Learning
- Classification
- Model Evaluation
- Feature Importance Analysis
- Business Analysis
- Customer Retention Analytics
- Python Programming

---

## 📁 Project Structure

```text
Customer_Churn_Analysis/
│
├── data/
│   ├── raw/
│   │   └── Telco-Customer-Churn.csv
│   │
│   ├── cleaned/
│   │   └── Telco-Customer-Churn-Cleaned.csv
│   │
│   └── processed/
│       ├── Telco-Customer-Churn-Engineered.csv
│       ├── churn_predictions.csv
│       └── random_forest_predictions.csv
│
├── outputs/
│   ├── churn_distribution.png
│   ├── churn_by_contract.png
│   ├── churn_by_internet_service.png
│   ├── churn_by_payment_method.png
│   ├── churn_by_tenure_group.png
│   ├── churn_by_monthly_charges.png
│   ├── churn_by_tech_support.png
│   ├── churn_by_online_security.png
│   ├── churn_by_senior_status.png
│   ├── confusion_matrix_logistic_regression.png
│   ├── roc_curve_logistic_regression.png
│   ├── top_10_feature_importance.png
│   ├── feature_importance.csv
│   ├── model_comparison.csv
│   ├── model_comparison.png
│   └── business_insights.csv
│
├── src/
│   ├── 01_data_understanding.py
│   ├── 02_data_cleaning.py
│   ├── 03_eda.py
│   ├── 04_feature_analysis.py
│   ├── 05_feature_engineering.py
│   ├── 06_model_training.py
│   ├── 07_model_evaluation.py
│   ├── 08_random_forest.py
│   ├── 09_feature_importance.py
│   ├── 10_model_comparison.py
│   └── 11_business_insights.py
│
├── requirements.txt
└── README.md

---

## 👩‍💻 Author

**Priyadarshani Biswal**

Aspiring Data Analyst
