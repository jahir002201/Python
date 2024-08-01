import pandas as pd
from sklearn.preprocessing import StandardScaler

# Sample data
df = pd.DataFrame({'Feature1': [1, 2, 3], 'Feature2': [4, 5, 6]})

# Standardize features
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)
print(scaled_data)
