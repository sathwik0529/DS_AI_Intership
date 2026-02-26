# plots.py
# This file will contain experimental visualization code for the project.

import matplotlib.pyplot as plt
import numpy as np

# Example plot
def example_plot():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.title('Example Sine Wave')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.show()

if __name__ == "__main__":
    example_plot()  
