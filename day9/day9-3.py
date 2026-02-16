import pandas as pd

# Create the Series
usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])

# Remove leading/trailing whitespace
cleaned = usernames.str.strip()

# Convert all names to lowercase
lowercased = cleaned.str.lower()

# Check which names contain the letter 'a'
contains_a = lowercased.str.contains('a')

# Display results
print("Original:")
print(usernames)

print("\nCleaned (strip + lower):")
print(lowercased)

print("\nContains letter 'a':")
print(contains_a)
