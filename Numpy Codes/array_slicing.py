import numpy as np

# ---------------------------- For 1D Array -------------------------------#

# Step1: Create an array.
# Slicing: Slicing in python means taking elements from one given index to another given index.

arr = np.array([1,2,3,4,5,6,7,8,9])

# Slicing with [start:end]
# For slicing, print arr with square bracket and "2" is starting position and "7" is ending position (7th position element is not included).
print(arr[2:7])

# Slicing with [start:end:step]
# For slicing, print arr with square bracket and as same as above but, "2" is step. Like given below
print(arr[1:8:2])


# --------------------------- For 2D Array -------------------------------#

arr1 = np.array([[1,2,3,4],[5,6,7,8]])

print(arr1[1,1:3])

# --------------------------- For 3D Array -------------------------------#

arr2 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(arr2[1,0,0:2])

# Note: To understand the concept of numpy array slicing, learn the concept python slicing from w3schools Python Tutorial.