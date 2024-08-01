from scipy.linalg import solve
import numpy as np

# Define the coefficients of the equations
A = np.array([[3, 2], [1, 2]])
# Define the constants
b = np.array([18, 14])

# Solve the equations
x = solve(A, b)
print(x) 
