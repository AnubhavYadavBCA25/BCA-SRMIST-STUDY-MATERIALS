import numpy as np

# In 'array indexing' we will find the element in array with its position number. Indexing is start from "0" position. 

# -------For 1D array--------#

# Creating an array
arr = np.array([1,2,3,4,5,6,7,8])

# print array and fill position number in square bracket, as given below
print(arr[3])


# -------For 2D array-------#

arr1 = np.array([[1,2,3,4],[5,6,7,8]])

# If we want to get "3" number from arr1, but their are two array in main array.
# So, as given below:- "0" is used for first array in main array and "2" is for position of the number we want.
print(arr1[0,2])


# -------For 3D array--------#

arr2 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(arr2[1,0,1])
# Try to analyse the above 3D array code. 
# Output is 8.

# Note: To understand the numpy array indexing, learn the concept of 'python indexing' from w3schools Python Tutorial.