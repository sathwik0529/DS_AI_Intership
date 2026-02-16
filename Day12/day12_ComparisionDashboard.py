import matplotlib.pyplot as plt

categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.subplot(1, 2, 2)
plt.plot(categories, sales)
plt.title("Sales Trend Line")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.show()
