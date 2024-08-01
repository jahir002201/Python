from scipy.interpolate import interp1d
import numpy as np 

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 1, 4, 9, 16, 25])

# Create a linear interpolator
f = interp1d(x, y)

# Interpolate
x_new = np.array([1.5, 2.5, 3.5])
y_new = f(x_new)
print(y_new)  
