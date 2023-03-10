import numpy as np

# Shape in numpy is define the shape or structure of the array

arr = np.array([1,2,3,4,5]) # Output:- (5,) here 5 is the element

arr1 = np.array([[1,2,3],[4,5,6]]) # Output:- (2,3) here 2 is 2D array and 3 is the element in an array.

arr2 = np.array([[[1,2],[3,4],[11,12]],[[5,6],[7,8],[9,10]]]) # Output:- (2,3,2) here 2 is main arrays of 3D array , 3 is the arrays in 2D or (sub-array) array and 2 is the element in 1D array.

print(arr.shape)
print(arr1.shape)
print(arr2.shape)

#--------------------------------------Reshape--------------------------------------#

# Reshape in numpy is used to change the shape or structure of the array.

new_arr = np.array([1,2,3,4,5,6,7,8,9,10])

print(new_arr.reshape(2,5))
# converting 1D array into 2D array.

new_arr1 = np.array([[1,2,3,4],[5,6,7,8]])
print(new_arr1.reshape(8,))
#converting 2D array into 1D array.

# Practice more programs to learn the concept of reshape in numpy.