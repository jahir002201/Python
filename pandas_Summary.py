import pandas as pd

# Read the JSON file into a DataFrame
df = pd.read_json('data.json')

# Print summary statistics for the DataFrame
print(df.describe())
