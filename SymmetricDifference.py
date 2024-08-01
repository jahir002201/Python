import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
symmetric_difference = np.setxor1d(arr1, arr2)
print(symmetric_difference)