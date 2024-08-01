from scipy.io import savemat, loadmat
import numpy as np

# Create a dictionary of arrays to save
mat_dict = {'array1': np.array([1, 2, 3]), 'array2': np.array([4, 5, 6])}

# Save to a MATLAB file
savemat('example.mat', mat_dict)

# Load the MATLAB file
data = loadmat('example.mat')
print(data)
