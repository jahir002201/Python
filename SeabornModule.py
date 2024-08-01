import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generate 1000 samples from a normal distribution
normal_dist = np.random.normal(loc=0, scale=1, size=1000)

# Create the histogram with KDE
sns.histplot(normal_dist, kde=True)

# Display the plot
plt.show()
