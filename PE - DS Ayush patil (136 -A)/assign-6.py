import numpy as np  




# Create arrays
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 4, 3, 2, 1])

c = np.add(a, b)
print(c)

print("Array A:", a)
print("Array B:", b)

# Perform multiple ufunc operations
print("\n Unary Operations")
print("Square Root of A:", np.sqrt(a))
print("Exponential of A:", np.exp(a))
print("Sine of A:", np.sin(a))

print("\n Binary Operations ")
print("Addition (A+B):", np.add(a, b))
print("Subtraction (A-B):", np.subtract(a, b))
print("Multiplication (A*B):", np.multiply(a, b))
print("Division (A/B):", np.divide(a, b))
print("Power (A^B):", np.power(a, 2))

print("\n Advanced Operations")
print("Maximum of A and B:", np.maximum(a, b))
print("Minimum of A and B:", np.minimum(a, b))
print("Modulus (A%B):", np.mod(a, b))

# Splitting fractional and integer parts
c = np.array([1.2, 2.5, 3.8])
frac, whole = np.modf(c)
print("\nFractional Parts:", frac)
print("Whole Parts:", whole)
