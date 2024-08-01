from scipy.spatial import KDTree
import numpy as np 

points = np.array([(1, 2), (3, 4), (5, 6), (7, 8)])
tree = KDTree(points)

# Query for the nearest neighbor to the point (2,3)
dist, idx = tree.query([2, 3])

print("Nearest neighbor index:", idx)
print("Distance to nearest neighbor:", dist)
