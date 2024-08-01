import numpy as np

# Define the original array
original = np.array([1, 2, 3, 4, 5])

# Create a view of the original array
view = original.view()

# Modify an element in the view
view[1] = 88

# Print the original array and the view
print("Original:", original)
print("View:", view)
