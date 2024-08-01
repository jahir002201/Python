import matplotlib.pyplot as plt  

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a figure and a 1x2 grid of subplots
plt.figure(figsize=(10, 5))  

# First subplot: 1 row, 2 columns, 1st subplot
plt.subplot(1, 2, 1)  
plt.plot(x, y, 'r--') 
plt.title('Plot 1')  
plt.xlabel('X axis')  
plt.ylabel('Y axis') 

# Second subplot: 1 row, 2 columns, 2nd subplot
plt.subplot(1, 2, 2)  
plt.plot(y, x, 'b-')  
plt.title('Plot 2')  
plt.xlabel('Y axis') 
plt.ylabel('X axis')  

# Display the plots
plt.tight_layout() 
plt.show()
