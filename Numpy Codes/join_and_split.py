import numpy as np 

#-------------------------------Array Join----------------------------------#
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])

new_arr = np.concatenate((arr1,arr2))
print(new_arr)

arr_1 = np.array([[1,2,3],[4,5,6]])
arr_2 = np.array([[7,8,9],[10,11,12]])

new_array = np.concatenate((arr_1,arr_2))
print(new_array)

# Note:- In numpy their is lots of function which work same as concetenate function like- stack,hstack,vstackand dstack.

#-----------------------------Array Split---------------------------------#

# Splitting 1D array
array_1 = np.array([1,2,3,4,5,6,7,8,9])
new_array1 = np.array_split(array_1,3)
print(new_array1)

#Splitting 2D array
array_2 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
new_array2 = np.array_split(array_2,2)
print(new_array2)

#Splitting 3D array
array_3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]],[[9,10],[11,12]]])
new_array3 = np.array_split(array_3,2)
print(new_array3)


# Practice more programs for better understanding of array join and split.