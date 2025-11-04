import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 1. LINE CHART
plt.figure(figsize=(8, 5))
plt.plot(x, y, marker='o')
plt.title('Line Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()

# 2. BAR CHART
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]

plt.figure(figsize=(8, 5))
plt.bar(categories, values, color='skyblue')
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# 3. HORIZONTAL BAR CHART
plt.figure(figsize=(8, 5))
plt.barh(categories, values, color='coral')
plt.title('Horizontal Bar Chart')
plt.xlabel('Values')
plt.ylabel('Categories')
plt.show()

# 4. PIE CHART
sizes = [25, 30, 20, 15, 10]
labels = ['Apple', 'Banana', 'Orange', 'Grape', 'Mango']

plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart')
plt.show()

# 5. SCATTER PLOT
x_scatter = np.random.rand(50) * 100
y_scatter = np.random.rand(50) * 100

plt.figure(figsize=(8, 5))
plt.scatter(x_scatter, y_scatter, c='purple', alpha=0.5)
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()



# 7. MULTIPLE LINES
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.title('Multiple Line Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()




#  AREA CHART
x = [1, 2, 3, 4, 5]
y = [1, 4, 6, 8, 4]

plt.figure(figsize=(8, 5))
plt.fill_between(x, y, color='lightblue', alpha=0.5)
plt.plot(x, y, color='blue')
plt.title('Area Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()