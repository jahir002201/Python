import numpy as np
original = np.array([1, 2, 3])
copy = original.copy()
copy[0] = 99
print("Original:", original)
print("Copy:", copy)
