import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
difference = np.setdiff1d(arr1, arr2)
print(difference)