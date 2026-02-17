import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

# Select only numeric columns for correlation
numeric_df = df.select_dtypes(include="number")

corr = numeric_df.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# Show highly correlated features (above 0.8 and below 1.0)
high_corr = corr[(corr > 0.8) & (corr < 1.0)]
print(high_corr.dropna(how="all").dropna(axis=1, how="all"))

# Boxplot for Salary (since 'Price' does not exist in this dataset)
plt.figure(figsize=(6, 4))
sns.boxplot(x=df['Salary'])
plt.title("Boxplot of Salary")
plt.tight_layout()
plt.show()
