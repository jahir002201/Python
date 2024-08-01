import matplotlib.pyplot as plt  

# Sample data
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Create a histogram
plt.hist(data, bins=4, edgecolor='black', color='skyblue')

# Add labels and title (optional)
plt.xlabel('Value')  
plt.ylabel('Frequency')  
plt.title('Histogram with 4 Bins')  

# Display the histogram
plt.show()
