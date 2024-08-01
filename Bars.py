import matplotlib.pyplot as plt  

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a bar chart
plt.bar(x, y, color='skyblue')  

# Add labels and title (optional)
plt.xlabel('X axis')  
plt.ylabel('Y axis')  
plt.title('Bar Chart')  

# Display the chart
plt.show()
