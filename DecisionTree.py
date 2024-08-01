from sklearn.tree import DecisionTreeClassifier

X = [[1, 2], [2, 3], [3, 4]]
y = [0, 1, 0]

clf = DecisionTreeClassifier().fit(X, y)
print(clf.predict([[2, 3]])) 
