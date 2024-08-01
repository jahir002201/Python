import pandas as pd

# Read the JSON file into a DataFrame
df = pd.read_json('data.json')

# Print the first 5 rows of the DataFrame
print("First 5 rows:")
print(df.head())

# Print the last 5 rows of the DataFrame
print("Last 5 rows:")
print(df.tail())
