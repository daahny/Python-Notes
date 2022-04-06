##### Lesson 7 #####
##### Array Oriented Programming with Numpy

import numpy as np

def creating_arrays():
    numbers = np.array([2, 3, 5, 7, 11])
    type(numbers)       # numpy.ndarray
    print(numbers)      # String representation: array([ 2,  3,  5,  7, 11])

    np.array([[1, 2, 3], [4, 5, 6]])


def array_attributes():
    # In a numpy array, nested arrays (each row) must have the same # of elements
    integers = np.array([[1, 2, 3], [4, 5, 6]])
    floats = np.array([0.0, 0.1, 0.2, 0.3, 0.4])

    # dtype is an attribute representing the underlying datatype
    print(integers.dtype)       # dtype('int64')
    print(floats.dtype)         # dtype('float64')

    # ndim represents the number of dimensions of an array
    print(integers.ndim)        # 2
    print(floats.ndim)          # 1

    # shape represents the shape of a 2D array, as a tuple: (rows, columns)
    # for a 1D array, shape holds a tuple of one element, simply being the # of elements
    print(integers.shape)       # (2, 3)
    print(floats.shape)         # (5,)

    # size represents the total number of elements
    print(integers.size)        # 6
    print(floats.size)          # 5

    # itemsize represents the number of bytes used for each element in the array
    print(integers.itemsize)    # 8
    print(floats.size)          # 8

    # flat attribute is used to 'flatten' a 2D array as if it didn't contain nested sequences
    for number in integers.flat:
        print(number, end=' ')  # prints 1 2 3 4 5 6