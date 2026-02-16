import pandas as pd
data = {
    "Price": ["$100.50", "$250.75", "$300.00", "$150.25"],
    "Date": ["2024-01-01", "2024-02-15", "2024-03-10", "2024-04-05"]
}
df = pd.DataFrame(data)
print(df.dtypes)
df["Price"] = df["Price"].str.replace("$", "", regex=False).astype(float)
df["Date"] = pd.to_datetime(df["Date"])
print(df.dtypes)
print(df)