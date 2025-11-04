import numpy as np

# Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.arange(10)
arr3 = np.linspace(0, 1, 5)

# Operations
sum_arr = arr1 + 5
product = arr1 * arr2[:5]
matrix = np.array([[1, 2], [3, 4]])
transpose = matrix.T

print("Array 1:", arr1)
print("Array 2:", arr2)
print("Sum Array:", sum_arr)
print("Matrix Transpose:\n", transpose)
print(product)

