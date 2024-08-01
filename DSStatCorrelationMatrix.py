import pandas as pd
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [2, 2, 3, 3, 5]
})
correlation_matrix = df.corr()
print(correlation_matrix)
