import numpy as np
import matplotlib.pyplot as plt

# Define function
def linear_function(x):
    return 2 * x + 1

# Generate data
x = np.linspace(-10, 10, 100)
y = linear_function(x)

# Plot
plt.plot(x, y)
plt.title('Linear Function: y = 2x + 1')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
