import numpy as np

def perceptron(x):
    weights = np.array([0.5, 0.5])
    bias = -0.5
    activation = np.dot(weights, x) + bias
    return 1 if activation >= 0 else 0

# Example input
x = np.array([1, 1])
print(perceptron(x))  
