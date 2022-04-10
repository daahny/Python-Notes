##### Lesson 7 #####
### Creating Numpy Arrays
### Array Attributes
### Creating arrays with specific values
### List vs Array Performance
### Array Operators
### NumPy Calculation Methods
### Universal Functions
### Indexing and Slicing
### Shallow Copies and Deep Copies for NumPy Arrays
### Reshaping and Transposing



from timeit import timeit
import numpy as np



### Creating Numpy Arrays ###
def creating_arrays():
    numbers = np.array([2, 3, 5, 7, 11])
    type(numbers)       # numpy.ndarray
    print(numbers)      # String representation: array([ 2,  3,  5,  7, 11])

    np.array([[1, 2, 3], [4, 5, 6]])



### Array Attributes ###
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



### Creating arrays with specific values ###
def fill_arr():
    np.zeros(5)                 # returns an array with zeros -- array([0., 0., 0., 0., 0.,])

    np.ones((2, 4), dtype=int)  # returns an array with shape of 2 rows, 4 columns, filled with ones
                                # array([[1, 1, 1, 1],
                                #        [1, 1, 1, 1]])

    np.full((3, 5), 13)         # returns an array with shape of 3 rows, 5 columns, filled with 13

    np.arange(5)                # array([0, 1, 2, 3, 4])
    np.arange(5, 10)            # array([5, 6, 7, 8, 9])
    np.arange(10, 1, -2)        # array([10, 8, 6, 4, 2])

    np.arange(1, 21).reshape(4, 5)
    # [[ 1  2  3  4  5]
    #  [ 6  7  8  9 10]
    #  [11 12 13 14 15]
    #  [16 17 18 19 20]]



### List vs Array Performance ###
import random
import time
def perf():
    start = time.time()
    rolls_list = [random.randrange(1, 7) for i in range(6_000_000)]
    end = time.time()
    print(f"{'List time:':<20} {end - start:.2} seconds")

    start = time.time()
    rolls_array = np.random.randint(1, 7, 6_000_000)        # In the range of 1 - 6 inclusive, generate 6 million values
    end = time.time()
    print(f"{'Numpy array time:':<20} {end - start:.2} seconds")



### Array Operators ###
def arr_op():
    numbers = np.arange(1, 6)       # array([1, 2, 3, 4, 5])
    numbers *= 2                    # array([2, 4, 6, 8, 10])

    numbers = np.arange(1, 6)
    numbers += 10                   # array([11, 12, 13, 14, 15])

    numbers1 = np.arange(1, 6)      # array([1, 2, 3, 4, 5])
    numbers2 = np.arange(11, 16)    # array([11, 12, 13, 14, 15])
    numbers3 = numbers1 + numbers2  # array([12, 14, 16, 18, 20])

    numbers1 < numbers2             # array([True, True, True, True, True])



### NumPy Calculation Methods ###
def calc_meth():
    grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])

    grades.sum()        # 1054
    grades.min()        # 70
    grades.max()        # 100
    grades.mean()       # 87.8333
    grades.std()        # std. dev: 8.792...
    grades.var()        # variance: 77.305...

    grades.mean(axis=0)     # array of mean values of columns -- total of 3 elements
    grades.mean(axis=1)     # array of mean values of rows -- total of 4 elements



### Universal Functions ###
def univ_func():
    numbers = np.array(1, 4, 9, 16, 24, 36)

    np.sqrt(numbers)    # Array of square root of each element, in floating point type

    np.mulitply(numbers, 3)



### Indexing and Slicing ###
def ind_sli():
    grades = np.array([[87, 96, 70], [100, 87, 90], 
                        [94, 77, 90], [100, 81, 82]])
    
    grades[0, 1]        # Nested element 96
    grades[1]           # Row 1 [100, 87, 90]
    grades[0:2]         # Rows 0 and 1
    grades[[1, 3]]      # Just row 1 and row 3
    grades[:, 0]        # The 0th element from each row [87, 100, 94, 100]
    grades[:, 1:3]      # The 1st and 3rd element from all rows



### Shallow Copies and Deep Copies for NumPy Arrays ###
def sha_dee():
    ## Shallow Copies
    # For NumPy arrays, slicing also creates shallow copies.
    # However, unlike lists, changes to shallow copies for NumPy arrays
    # are reflected in the original array and vice versa
    numsa = np.arange(1, 6)
    numsb = numsa[0:3]

    # lista and listb have separate IDs

    numsa[1] = 9
    print(numsb)    # [1, 9, 2, 3, 4, 5]

    ## Deep Copies
    numbers = np.arange(1, 6)
    numbers2 = numbers.copy()   # Creates a deep copy

    # Changes aren't reflected in each other
    numbers[3] = 10000
    print(numbers2) # [1, 2, 3, 4, 5]



### Reshaping and Transposing ###
def resh():
    grades = np.array([[87, 96, 70], [100, 87, 90], 
                        [94, 77, 90], [100, 81, 82]])

    grades.reshape(2, 3)            # 2 rows 3 columns
    grades.resize(1, 6)             # 1 row 6 columns (still going to be a nested array tho)

    flattened = grades.flatten      # 1 dimensional array (deep copy)
    raveled = grades.ravel()        # 1 dimensional array (shallow copy)

    # Transpose: Cause 2 things to change place with eachother
    new_grades = np.array([[100, 95, 80], [70, 60, 50]])
    new_grades.T                        # rows swap with columns
    # [[100  95  80]                        [[100  70]
    # [ 70  60  50]]            to           [ 95  60]
    #                                        [ 80  50]]

    ## Horizontal and Vertical Stacking
    z = np.zeros(6).reshape(2, 3)           # [[0. 0. 0.]
                                            #  [0. 0. 0.]]
    o = np.ones(6).reshape(2, 3)            # [[1. 1. 1.]
                                            #  [1. 1. 1.]]

    print(np.hstack((z, o)))                # Must accept a tuple of arrays
                                            # [[0. 0. 0. 1. 1. 1.]
                                            #  [0. 0. 0. 1. 1. 1.]]

    print(np.vstack((z, o)))                # [[0. 0. 0.]
                                            #  [0. 0. 0.]
                                            #  [1. 1. 1.]
                                            #  [1. 1. 1.]]
