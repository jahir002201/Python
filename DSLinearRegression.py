from sklearn.linear_model import LinearRegression
import numpy as np

# Example data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 4, 5])

# Fit the model
model = LinearRegression()
model.fit(X, y)

# Make predictions
predictions = model.predict(X)
print(predictions)
