import pandas as pd

df = pd.read_csv("customer_orders.csv")

print("Shape before cleaning:", df.shape)
print("Missing values:\n", df.isna().sum())

numeric_cols = df.select_dtypes(include="number").columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

df = df.drop_duplicates()

print("Shape after cleaning:", df.shape)