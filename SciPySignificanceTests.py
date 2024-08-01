from scipy.stats import ttest_ind
import numpy as np 

# Two independent samples
sample1 = np.array([1.1, 2.3, 3.1, 4.0])
sample2 = np.array([2.0, 3.1, 4.5, 5.3])

# Perform t-test
t_stat, p_val = ttest_ind(sample1, sample2)

print("t-statistic:", t_stat)
print("p-value:", p_val)
