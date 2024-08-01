import numpy as np
multinomial_dist = np.random.multinomial(n=100, pvals=[0.2, 0.3, 0.5], size=1000)
print(multinomial_dist)
