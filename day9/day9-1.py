import pandas as pd

# Create the Series with custom labels
products = pd.Series(
    [700, 150, 300],
    index=['Laptop', 'Mouse', 'Keyboard']
)

# Access the price of 'Laptop' using label-based indexing
laptop_price = products['Laptop']

# Slice the first two products using positional indexing
first_two = products.iloc[:2]

# Output the results
print("Full Series:")
print(products)

print("\nPrice of Laptop:")
print(laptop_price)

print("\nFirst two products (positional slice):")
print(first_two)
