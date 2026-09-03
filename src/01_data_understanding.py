# import pandas as pd

# # Load the raw dataset
# df = pd.read_csv("data/raw/Telco-Customer-Churn.csv")

# # Display first 5 rows
# print(df.head())

import pandas as pd

# Load the raw dataset
df = pd.read_csv("data/raw/Telco-Customer-Churn.csv")

# Display first 5 rows
print("\n--- FIRST 5 ROWS ---")
print(df.head())

# Dataset shape
print("\n--- DATASET SHAPE ---")
print(df.shape)

# Column names
print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

# Data types
print("\n--- DATA TYPES ---")
print(df.dtypes)

# Missing values
print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

# Duplicate rows
print("\n--- DUPLICATE ROWS ---")
print(df.duplicated().sum())

