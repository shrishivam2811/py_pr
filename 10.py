# Using a numpy module create an array and check the following: 1. Type of array 2. Axes of array 3. Shape of array 4. Type of elements in array

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(f'Type of array: {type(arr)}')
print(f'Axes of array: {arr.ndim}')
print(f'Shape of array: {arr.shape}')
print(f'Type of elements in array: {arr.dtype}')
