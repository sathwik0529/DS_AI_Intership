import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# 1️⃣ Create a heavily skewed population (exponential distribution)
population = np.random.exponential(scale=50000, size=100000)

# Plot the original skewed population
plt.figure()
plt.hist(population, bins=50)
plt.title("Original Population Distribution (Skewed)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 2️⃣ Take 1,000 samples of size 30 and compute their means
sample_means = []

for _ in range(1000):
    sample = np.random.choice(population, size=30)
    sample_means.append(np.mean(sample))

# 3️⃣ Plot the distribution of sample means
plt.figure()
plt.hist(sample)
