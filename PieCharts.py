import matplotlib.pyplot as plt  

# Data for the pie chart
sizes = [10, 20, 30]  
labels = ['A', 'B', 'C']  

# Create the pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['skyblue', 'lightgreen', 'salmon'])

# Add a title (optional)
plt.title('Pie Chart Example')  

# Display the pie chart
plt.show()
