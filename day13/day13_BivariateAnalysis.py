import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = 'housing_prices.csv'
df = pd.read_csv(file_path)

# Scatter plot: SquareFeet vs Price
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='SquareFeet', y='Price')
plt.title('Scatter Plot: SquareFeet vs Price')
plt.xlabel('Square Feet')
plt.ylabel('Price')
plt.tight_layout()
plt.savefig('scatter_squarefeet_price.png')
plt.show()
plt.close()

# Boxplot: Location vs Price
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Location', y='Price')
plt.title('Boxplot: Location vs Price')
plt.xlabel('Location')
plt.ylabel('Price')
plt.tight_layout()
plt.savefig('boxplot_location_price.png')
plt.show()
plt.close()
