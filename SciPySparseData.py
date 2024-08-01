from scipy.sparse import csr_matrix

# Create a sparse matrix
A = csr_matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])

print("Sparse matrix:\n", A)
print("Dense matrix:\n", A.toarray())
