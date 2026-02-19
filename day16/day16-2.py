import numpy as np
import pandas as pd

# Set seed for reproducibility
np.random.seed(42)

# 1️⃣ Create sample dataset (normal distribution)
data = np.random.normal(loc=100, scale=15, size=1000)

# Add a few extreme outliers
data = np.append(data, [30, 250, 300])

# Create DataFrame
df = pd.DataFrame({"value": data})

# 2️⃣ Calculate mean (μ) and standard deviation (σ)
mu = df["value"].mean()
sigma = df["value"].std()

print(f"Mean (μ): {mu}")
print(f"Standard Deviation (σ): {sigma}")

# 3️⃣ Calculate Z-scores
df["z_score"] = (df["value"] - mu) / sigma

# 4️⃣ Identify statistical outliers (|Z| > 3)
outliers = df[np.abs(df["z_score"]) > 3]

print("\nOutliers (|Z| > 3):")
print(outliers)
