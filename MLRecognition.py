from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load data
digits = load_digits()
X = digits.data
y = digits.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

# Train model
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Test model
accuracy = clf.score(X_test, y_test)
print(accuracy)
