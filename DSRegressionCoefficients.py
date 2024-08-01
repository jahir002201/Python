from sklearn.linear_model import LinearRegression

# Example data
X = [[1], [2], [3], [4], [5]]  
y = [2, 4, 6, 8, 10]            

# Initialize and fit the model
model = LinearRegression()
model.fit(X, y)

# Print the coefficients and intercept
print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)
