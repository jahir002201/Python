from sklearn.linear_model import LinearRegression
import numpy as np

# Example data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 3, 5, 7, 9])

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Make predictions
predictions = model.predict(np.array([[6]]))
print(predictions)  
