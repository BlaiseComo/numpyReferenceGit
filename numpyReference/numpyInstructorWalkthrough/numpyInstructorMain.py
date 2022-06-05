import numpy as np
import sys

# Initialize an Array
# You could specify the type of the values with dtype as the second argument 
a = np.array([1,2,3])

# Two dimensional Array
b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])

# Returns the dimensions of the array, this would return 1, but b.ndim would return 2
a.ndim

# Gets the shape of an array, this would return (3,), but b.shape would return (2, 3)
a.shape

# Gets the type 
a.dtype

# Gets the size (in bytes) of the array
a.itemsize

# Gets the total size (in bytes) of the array
a.nbytes

a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])

# Gets a specific element [row, column] rows and columns start at index 0
a[1,5] # would return 13

# Get a specific row
a[0, :]

# Get a specific column
a[:, 2]

# Trikcy [startindex:endindex:stepsize]
a[0, 1:6:2] # returns [2, 4, 6]

a[0, 1:-1:2] # returns [2, 4, 6]

# Changing a value of an array
a[1, 5] = 20 # changes 13 in a to 20

# Changing a whole column
a[:, 2] = 5 # changes 3 and 10 in a to 5

# 3D Array
b = np.array( [ [ [1,2], [3,4] ], [ [5,6], [7,8] ] ] )

# Get Specific Element In b
b[0, 1, 1] # this will return 4

# Replacing an element in b
b[:, 1, :] = [[9,9], [8,8]] # will change [3,4] and [7,8] to [9,9] and [8,8] respectively

# All 0s matrix
np.zeros((2,3)) # creates a 2 by 3 matrix of 0s

# All 1s matrix
np.ones((4,2,2), dtype='int32') # creates a matrix of 4 arrays, each with a 2 by 2 matrix, all filled with 1s

# Any other number
np.full((2,2), 99) # creates a 2 by 2 array of 99

# Any other number (Another method)
np.full(a.shape, 4) # creates an array the same shape as a, filled with 4

# Random decimal numbers
np.random.rand(4,2) # this returns a 4 by 2 array of random numbers between 0 and 1

np.random.random_sample(a.shape) # returns an array the same shape as a filled with random numbers between 0 and 1

# Random Integer values
huh = np.random.randint(2, 7, size=(3,3)) # returns a 3 by 3 array of random numbers between 2 and 7

# The identity matrix
np.identity(5) # returns a 5 by 5 array 

# Repeating array values
arr = np.array([1,2,3])
arr2 = np.array([[1,2,3]])
r1 = np.repeat(arr, 3, axis=0) # r1 returns [1,1,1,2,2,2,3,3,3]
r2 = np.repeat(arr2, 3, axis=0) # r2 returns [[1,2,3], [1,2,3], [1,2,3]]

# Arithmetic with Arrays

a = np.array([1,2,3,4])

a + 2 # returns a but with every value += 2

a - 2

a * 2

a / 2

a ** 2

np.sin(a)
np.cos(a)

# You can also add arrays if their the same shape

# Linear Algebra

np.matmul(a, b) # multiplies matrices a and b and returns the product array

# Find the determinant 
c = np.identity(3)
np.linalg.det(c) # returns determinannt of c

# Statistics

stats = np.array([[1,2,3],[4,5,6]])

# Minimum Value of Array
np.min(stats, axis=1) # returns min of first row and min of second row

# Maximum Value of Array
np.max(stats, axis=0) # returns second row of stats as it has the max's

# Sum of Arrays
np.sum(stats, axis=0) # returns sum of all columns of stats

# Loading data from file
filedata = np.genfromtxt('data.txt', delimiter=',') # returns an array from the data in data.txt with delimiter as a comma, data will be floats
filedata = filedata.astype('int32') # changes all data types to ints
