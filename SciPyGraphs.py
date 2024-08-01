from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix

# Adjacency matrix for a graph
graph = csr_matrix([
    [0, 1, 2],
    [1, 0, 4],
    [2, 4, 0]
])

# Compute shortest paths
dist_matrix, predecessors = dijkstra(graph, return_predecessors=True)

print("Shortest distance matrix:\n", dist_matrix)
print("Predecessors:\n", predecessors)
