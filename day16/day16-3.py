import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Reproducibility
np.random.seed(42)

# 1️⃣ Generate datasets

# Normal Distribution (Human Heights)
heights = np.random.normal(loc=170, scale=10, size=1000)

# Right-Skewed Distribution (Household Incomes)
incomes = np.random.exponential(scale=50000, size=1000)

# Left-Skewed Distribution (Easy Exam Scores)
test_scores = 100 - np.random.exponential(scale=10, size=1000)
test_scores = np.clip(test_scores, 0, 100)

datasets = {
    "Human Heights (Normal)": heights,
    "Household Incomes (Right-Skewed)": incomes,
    "Easy Exam Scores (Left-Skewed)": test_scores
}

# 2️⃣ Plot histograms with KDE and compare mean vs median
for title, data in datasets.items():
    df = pd.DataFrame({"value": data})
    
    mean = df["value"].mean()
    median = df["value"].median()
    
    print(f"\n{title}")
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    
    # Plot histogram
    plt.figure()
    plt.hist(df["value"], bins=30, density=True)
    
    # KDE overlay
    kde = gaussian_kde(df["value"])
    x_vals = np.linspace(df["value"].min(), df["value"].max(), 500)
    plt.plot(x_vals, kde(x_vals))
    
    plt.title(title)
    plt.xlabel("Value")
    plt.ylabel("Density")
    plt.show()
