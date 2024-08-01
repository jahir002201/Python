from sklearn.cluster import KMeans
import numpy as np

# Sample data
data = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])

# Fit KMeans model
kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

# Print cluster centers
print(kmeans.cluster_centers_)
print(kmeans.labels_)
