import numpy as np
def my_func(x):
    return x + 1
my_ufunc = np.frompyfunc(my_func, 1, 1)
result = my_ufunc(np.array([1, 2, 3]))
print(result)
