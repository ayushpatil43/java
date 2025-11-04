
import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]


data = np.random.randn(1000)

plt.figure(figsize=(8, 5))
plt.hist(data, bins=30, color='green')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
