from scipy.optimize import minimize
import numpy as np 

# Define the function to minimize
def f(x):
    return x**2 + 5*np.sin(x)

# Initial guess
x0 = 2.0

# Perform the optimization
result = minimize(f, x0)

print("Minimum value:", result.fun)
print("Location of minimum:", result.x)
