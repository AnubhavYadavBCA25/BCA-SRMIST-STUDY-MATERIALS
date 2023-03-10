# Step1: Download 'numpy' module for use in your program.
# command in cmd: pip install numpy
# or command in cmd: py -m pip install numpy

# Step2: Import numpy in your file.
# Assign numpy a short name like 'np'.
import numpy as np

# Create an array.

# 0-D array
arr = np.array(78) 
print(arr)

# 1-D array
arr1 = np.array([1,2,3,4,5])
print(arr1)

# 2-D array
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)

# 3-D array
arr3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(arr3)

# Check the dimensions of the arrays.
print(arr.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)