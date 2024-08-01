from sklearn.linear_model import LinearRegression

# Example data
X = [[1], [2], [3], [4], [5]]  
y = [2, 4, 6, 8, 10]           

# Initialize and fit the model
model = LinearRegression()
model.fit(X, y)

# Calculate and print the R-squared value
r_squared = model.score(X, y)
print("R-squared:", r_squared)
