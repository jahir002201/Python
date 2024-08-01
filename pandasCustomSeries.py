import pandas as pd

# Define the data
data = [10, 20, 30, 40, 50]

# Create a Pandas Series with the data and custom indices
series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])

# Print the Series
print(series)
