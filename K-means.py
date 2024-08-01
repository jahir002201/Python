from sklearn.cluster import KMeans

X = [[1, 2], [2, 3], [3, 4], [8, 9]]
kmeans = KMeans(n_clusters=2).fit(X)
print(kmeans.labels_)
