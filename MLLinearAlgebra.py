import numpy as np

# Define matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix addition
C = A + B

# Matrix multiplication
D = np.dot(A, B)

print("Matrix Addition:\n", C)
print("Matrix Multiplication:\n", D)
