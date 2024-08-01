import numpy as np  # Use np as the alias

# Define the original array
joined = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Split the array into 3 parts
split = np.array_split(joined, 3)

# Print each part of the split array
for arr in split:
    print(arr)
