import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("housing_prices.csv")

sns.histplot(df['Price'], kde=True)
plt.show()

print(df['Price'].skew())
print(df['Price'].kurt())

sns.countplot(x='City', data=df)
plt.show()
