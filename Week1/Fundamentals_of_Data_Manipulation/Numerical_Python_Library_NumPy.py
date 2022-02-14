# You will recall that we import a library using the "import" keyword
# as numpy common abbreviation is np

import numpy as np
import math
from PIL import Image
# from IPython.display import display


# Array Creation
# Arrays are displayed as a list...

a = np.array([1, 2, 3])
# print(a)

# We can print the number of dimensions of a list using the ndim attribute
# print(a.ndim)

# If we pass in a list of lists in numpy array, we create a multidimensional array, for instance, a matrix
b = np.array([[1, 2, 3], [4, 5, 6]])
# print(b)

# We can print out the length of each dimension by calling the shape attribute, which returns a tuple
# print(b.shape)

# We can also check the type of items in the array
# print(b.dtype)

# Besides integers, floats are also accepted in numpy arrays
c = np.array([2.2, 5, 1.1])
# print(c)
# print(c.dtype)

# Note that numpy automatically converts integers, like 5, up to floats, since there is no loss of precision.
# ...

# Numpy offers several functions to create arrays with placeholders, such as zero's or one's.
# Let's create two arrays, both the same shape but with different filter values.
d = np.zeros((2, 3))
e = np.ones((2, 3))
# print(d, '\n\n', e)

# >>
# [[0. 0. 0.]
#  [0. 0. 0.]]
#
#  [[1. 1. 1.]
#  [1. 1. 1.]]

# We can also generate an array with random numbers
random_array = np.random.rand(2, 3)
# print(random_array)

# >>
# [[0.10798286 0.94457366 0.5881763 ]
#  [0.68485572 0.04026548 0.92116046]]

# We can also create a sequence of numbers in an array with the arange() function.
f = np.arange(10, 30, 2)
# print(f)

# >>
# [10 12 14 16 18 20 22 24 26 28]

# If we want to generate a sequence of floats, we can use the linspace() function.
# In this function, the third argument is the total number of items you want to generate
linspace_array = np.linspace(0, 2, 5)
# print(linspace_array)

# >>
# [0.  0.5 1.  1.5 2. ]


# Array Operations
# We can also do matrix manipulation such as product, transpose, inverse and so on.

a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

# a minus b
c = a - b
# print(c)
# >> [ 9 18 27 36]

# a times b
d = a * b
# print(d)
# >> [ 10  40  90 160]

farenheit = np.array([0, -10, -5, -15, 0])

celcius = (farenheit - 32) * (5/9)
# print(celcius)
# print(celcius > -20)
# print(celcius % 2 == 0)

# >>
# [-17.77777778 -23.33333333 -20.55555556 -26.11111111 -17.77777778]
# [ True False False False  True]
# [False False False False False]


A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])

# 元素对应乘积 Elementwise product
# print(A * B)

# print('\n')
# 矩阵的乘法 Matrix product
# print(A @ B)

# >>
# [[2 0]
#  [0 4]]
#
# [[5 4]
#  [3 4]]

# Upcasting 上移
array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[7.1, 8.2, 9.3], [10.4, 11.2, 12.3]])
array3 = array1 + array2

# print(array1.dtype, array2.dtype, array3.dtype)
# >>
# int64 float64 float64

# Interesting Aggregation functions, such as sum(), max(), min(), and mean()
# print(array3.max())
# print(array3.min())
# print(array3.sum())
# print(array3.mean())

b = np.arange(1, 16, 1).reshape(3, 5)
# print(b)

# >>
# [[ 1  2  3  4  5]
# [ 6  7  8  9 10]
# [11 12 13 14 15]]

# image = Image.open('python.png')
# image.show()

# array = np.array(image)

a = np.array([1, 3, 5, 7])
# print(a[2])

# >>
# 5

# For multidimensional array, we need to use integer array indexing, let's create a  new multidimensional array
a = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])
# print(a, '\n')
# print(a[1, 1])

# >>
# [[1 2]
#  [3 4]
#  [5 6]]

# 4

a = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

b = np.array([a[0, 0], a[1, 1], a[2, 1]])
# print(b)

# >> [1 4 6]

a = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

c = a[
    [0, 1, 2],
    [0, 1, 1]
]
# print(c)

# >> [1 4 6]

a = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])
print(a>5)

# [[False False]
#  [False False]
#  [False  True]]
