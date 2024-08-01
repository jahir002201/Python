import matplotlib.pyplot as plt  

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a scatter plot
plt.scatter(x, y, color='b', marker='o')  

# Add labels and title (optional)
plt.xlabel('X axis')  
plt.ylabel('Y axis')  
plt.title('Scatter Plot')  

# Display the plot
plt.show()
