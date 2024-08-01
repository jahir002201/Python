from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Load data
iris = load_iris()
X = iris.data
y = iris.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Train model
model = SVC()
model.fit(X_train, y_train)

# Test model
score = model.score(X_test, y_test)
print(score)
