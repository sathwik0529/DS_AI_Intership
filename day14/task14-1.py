import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Example data
data = {
	'Age': [22, 25, 47, 52, 46, 56, 55, 60, 62, 61],
	'Salary': [20000, 25000, 47000, 52000, 46000, 56000, 55000, 60000, 62000, 61000]
}
df = pd.DataFrame(data)

# Standardization (mean=0, std=1)
scaler_standard = StandardScaler()
df_standardized = pd.DataFrame(scaler_standard.fit_transform(df), columns=df.columns)

# Normalization (range 0 to 1)
scaler_minmax = MinMaxScaler()
df_normalized = pd.DataFrame(scaler_minmax.fit_transform(df), columns=df.columns)

# Plot histogram of Salary before and after scaling
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.hist(df['Salary'], bins=5, color='blue', alpha=0.7)
plt.title('Original Salary')
plt.xlabel('Salary')
plt.ylabel('Count')

plt.subplot(1, 3, 2)
plt.hist(df_standardized['Salary'], bins=5, color='green', alpha=0.7)
plt.title('Standardized Salary')
plt.xlabel('Standardized Value')

plt.subplot(1, 3, 3)
plt.hist(df_normalized['Salary'], bins=5, color='red', alpha=0.7)
plt.title('Normalized Salary')
plt.xlabel('Normalized Value')

plt.tight_layout()
plt.show()