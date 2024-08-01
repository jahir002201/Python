import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the DataFrame from a CSV file
df = pd.read_csv('data.csv')

# Print column names to verify
print("Columns in the DataFrame:")
print(df.columns)

# 7. Handling Missing Data

# Drop rows with missing values
df.dropna(inplace=True)

# Fill missing values with a specific value
# Let's assume you want to fill missing values in the 'age' column
df['age'].fillna(0, inplace=True)

# 8. Cleaning Empty Cells
# Fill empty cells in the 'city' column with 'Unknown'
df['city'].fillna('Unknown', inplace=True)

# 9. Cleaning Wrong Format
# If there are columns that need to be converted to datetime, use pd.to_datetime
# df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# 10. Cleaning Wrong Data
# Replace negative ages with the mean age
df.loc[df['age'] < 0, 'age'] = df['age'].mean()

# 11. Removing Duplicates
# Drop duplicate rows
df.drop_duplicates(inplace=True)

# 12. Calculating Correlations
# Compute correlation only for numeric columns
numeric_df = df.select_dtypes(include=[np.number])
correlation = numeric_df.corr()
print("Correlation Matrix:")
print(correlation)

# 13. Plotting with Pandas

# Line plot (adjust x and y as needed)
# df.plot(kind='line', x='Date', y='Value', title='Line Plot of Value Over Time')
# plt.show()

# Bar plot
df.plot(kind='bar', x='name', y='age', title='Bar Plot of Age by Name')
plt.show()

# Scatter plot (adjust x and y as needed)
# df.plot(kind='scatter', x='age', y='Salary', title='Scatter Plot of Age vs. Salary')
# plt.show()

# Histogram
df['age'].plot(kind='hist', bins=10, title='Histogram of Age')
plt.show()
