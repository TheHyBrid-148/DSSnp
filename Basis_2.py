# Main import statment for numpy (Every program)
import numpy as np

# Array Reshaping (1-12 arry into 3x4 matrix)
a = np.arange(1, 13).reshape(3, 4)
print(a)

# Flatten matrix (Converting matrix into 1D)
# [[1, 2],
# [3, 4]]
a = np.array([[1, 2], [3, 4]])
print(a.flatten())
