from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
import numpy as np

# Example data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 4, 9, 16, 25])

# Polynomial regression model
poly = PolynomialFeatures(degree=2)
model = make_pipeline(poly, LinearRegression())
model.fit(X, y)

# Make predictions
predictions = model.predict(np.array([[6]]))
print(predictions)
