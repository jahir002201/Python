from scipy.stats import pearsonr

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]
correlation, _ = pearsonr(x, y)
print(correlation)
