# Main import statement for numpy (every program)
import numpy as np

# Even numbers from 2 - 20
a = np.arange(2, 21, 2)
print(a)

# Given [5, 10, 15, 20, 25], find the number of elements
a =  np.array([5, 10, 15, 20, 25])
print(len(a))

# From [11, 22, 33, 44, 55], print: first and last element
a = np.array([11, 22, 33, 44, 55])
print(a[0])
print(a[-1])

# Add 10 to every element in [5, 10, 15, 20, 25]
a = np.array([5, 10, 15, 20, 25])
print(a + 10)

# Create [1, 2, 3] and print its data type
a = np.array([1, 2, 3])
print(a.dtype)

# Create a 2x2 array filled with ones
a = np.ones((2, 2))
print(a)

# Find the shape
# [[1, 2, 3],
# [4, 5, 6]]
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)

# From [3, 6, 9, 12, 15], create a boolean array showing values greater than 8
a = np.array([3, 6, 9, 12, 15])
print(a > 8)

# Find sum and average of [4, 8, 12, 16]
a = np.array([4, 8, 12, 16])
print(a.sum())
print(a.mean())
