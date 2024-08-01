import pandas as pd

# Read the JSON file into a DataFrame
df = pd.read_json('data.json')

# Print the data types of each column
print(df.dtypes)
