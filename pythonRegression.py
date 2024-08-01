from sklearn.linear_model import LinearRegression
import numpy as np

# Define the input data (X) and target values (y)
X = np.array([[1], [2], [3]])
y = np.array([1, 2, 3])

# Create and fit the linear regression model
model = LinearRegression().fit(X, y)

# Predict the target value for a new input
print(model.predict([[4]]))
