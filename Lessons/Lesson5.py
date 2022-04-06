##### Lesson 5 #####
### Lists
### Tuples
### Unpacking Sequences
### Sequence Slicing
### Relating references, copying, and immutabilty
### del
### Sorting
### Searching
### any() and all()
### List Methods
### List Comprehensions
### Generator Expressions
### Map, Filter, Reduce, and Lambda
### Sequence Processing Functions
### Iterators and Sequences
### Two-Dimensional Lists


### Sequences, Lists, and Tuples ###
### Lists ###
def lists():
    # Can be homogenous or heterogenous (same or different data types in one list)
    c = [-45, 6, 0, 72, 1543]
    print(c[2])     # prints 0
    print(c[-1])    # prints 1543, reverse indexing starts at -1
    print(len(c))   # prints 5

    # Lists are mutable
    c[4] = 17

    # Strings are immutable
    # The square bracket notation can be used to access an element of any sequence
    s = 'hello'
    s[0]        # prints h
    s[0] = 'H'  # Throws a TypeError: 'str' object does not support item assignment

    # Index out of range
    c[100]      # Throws IndexError: list index out of range

    # Lists are not one set length
    # When adding to a list, the added element must be an iterable
    list = []
    for value in range(1, 6):
        list += [value]     # This is okay
        list += value       # Throws a TypeErrpr: 'int' object is not iterable


### Tuples ###
### Tuples ###
# Tuples are an immutable set of elements, defined by commas, typically placed in paranthesis
def roll_dice():
    """Roll two dice and return their face values as a tuple."""
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2) # This packs the two values into a tuple and returns the tuple

def display_dice(die_rolls):
    """Display one roll of the two dice."""
    die1, die2 = die_rolls  # The die_rolls tuple is unpacked into die1 and die2.
                            # This works because the number of elements being unpacked into matches
                            # the number of elements in the die_rolls tuple

def tuples():
    # Paranthesis aren't required but always recommended
    student_tuple = ('Mary', 'John', 3.3)
    singleton_tuple = ('red',)
    singleton_tuple[0]

    # Tuples are immutable
    tuple1 = (10, 20, 30)
    tuple2 = tuple1
    tuple1 += (40, 50)
    # tuple1 will refer to an entirely new tuple object
    # tuple2 will refer to the original (10, 20, 30) tuple



### Unpacking Sequences ###
def unpacking_sequences():
    student_tuple = ('Jared', [84, 90, 66, 100])
    name, grades = student_tuple    # unpacking the student_tuple

    first, second = 'hi'            # first = h, second = i

    num1, num2, num3 = range(10, 40, 10)    # num1 = 10, num2 = 20, num3 = 30 because this range function
                                            # only produces 3 values: 10, 20, 30

    # Using unpacking to swap values:
    number1 = 10
    number2 = 20
    # Create a tuple with these 2 values and unpack them one the same line
    number1, number2 = (number2, number1)   # swaps number1 and number2

    # list() and enumerate()
    # list() is a built-in function that takes a sequence and returns that sequence as a list
    # enumerate() is a built-in function that returns a sequence of tuples in which each tuple contains
    # the index number and the corresponding value in the sequence
    colors = ['red', 'orange', 'yellow']
    print(list(enumerate(colors)))      # [(0, 'red'), (1, 'orange'), (2, 'yellow')]

    # tuple() is a built-in function that takes a sequence and returns that sequence as a tuple
    print(tuple(enumerate(colors)))     # ((0, 'red'), (1, 'orange'), (2, 'yellow'))

    # Using enumerate() in tuple unpacking in a for loop, very common use of enumerate()
    for index, value in enumerate(colors):
        print(f'{index>2}:{value>10}')
        # 0:    red
        # 1: orange
        # 2: yellow



### Primitive bar chart ###
def prim_bar():
    nums = [19, 3, 5, 7, 11]
    printf('Index{Value:>8}    Bar')

    for index, value in enumerate(nums):
        print(f'{index:>5}{value:>8}    {"*" * value}')

    #Output
    # Index   Value    Bar
    #     0      19    *******************
    #     1       3    ***
    #     2       5    *****
    #     3       7    *******
    #     4      11    ***********



### Sequence Slicing ###
def seq_slice():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7]
    numbers[:6]         # Represents a new list of values from index 0 to index 6 not including index 6  
                        # -- [0, 1, 2, 3, 4, 5]
    numbers[2:6]        # Represents a new list starting from index 2 and not include index 6 
                        # -- [2, 3, 4, 5]
    numbers[6:]         # Represents a new list starting from and including index 6 
                        # -- [6, 7]
    numbers[::2]        # Represents a new list starting from the beginning with a step of 2
                        # -- [0, 2, 4, 6]
    numbers[::-1]       # Reverse list
                        # -- [7, 6, 5, 4, 3, 2, 1, 0]

    numbers[0:3] = ['zero', 'one', 'two']   # Replace
    numbers[0:3] = []                       # Remove

    
    # Note: list slicing like this creates a new list. So, when a variable is re-assigned to a slice
    # of a list, it is assigned a new list. The original list is not modified.
    # We call slicing a *Shallow Copy*. A splice of the original list.



### Fundamental concept: Reference and Copying ###
# When you declare a variable and assign it a copy of an existing variable using =,
# you are not creating a new object.
# Instead, you are creating a new variable that references an object that already exists
def ref_and_copy():
    x = [1, 2, 3]   # This is a new object
    y = x           # This is creating another variable that references the original object
    # x and y will share the same id. (x is y) equates to True

    ## Shallow copies
    # A shallow copy creates a new object that stores references of the original elements.
    # So, in effect, a shallow copy doesn't create copies of the original nested elements,
    # it creates copies of the references to the original nested elements.
    import copy
    x = [[1, 2, 3], [4, 5, 6]]
    y = copy.copy(x)            # Creates a shallow copy
    # When creating a shallow copy, the 2 lists have separate IDs.  This is not like using the = operator.
    # Adding to the old list or the new list will not impact each other
    # Only when changing the nested objects in either x or y, a change to the other list will be seen.

    # When the lists do not have nested elements, changes to the lists are unique and not shared (for shallow copies)
    x = [1, 2, 3]
    y = copy.copy(x)
    # Here, any change to x or y in any way will be independent. Again, they have different IDs.
    # Lists will only share the same ID when one is copied using the = operator.
    # This is unlike immutable objects like strings.
    a = "first"
    b = "first"
    # Here, a and b will share the same ID. Modifying a or b will change the reference entirely

    ## Deep copies
    # Like shallow copies, deep copies are new objects.
    # Unlike shallow copies, deep copies do not store references to the original nested objects.
    # Instead, deep copies store copies of nested objects, not copies of the references of the nested objects.
    x = [[1, 2, 3], [4, 5, 6]]
    y = copy.deepcopy(x)
    # Any changes to either list in any way will be independent of each other.
    


### del statement ###
def deldel():
    numbers = list(range(10))
    del numbers[-1]     # removes the last element from a list
    del numbers[0:2]    # removes up to (not including) index 2, so index 0 and 1
    del numbers         # only works on mutable types



### Sorting Sequences ###
def sorto():
    numbers = [10, 3, 7, 9, 1, 6, 1, 5, 8]
    numbers.sort()
    numbers.sort(reverse=True)

    # For not modifying the original list or when working with an immutable sequence
    # Use the built-in function sorted()
    # sorted() accepts an iterable and returns that iterable as a sorted list
    ascending_nums = sorted(numbers)

    letters = 'jhabsofyguq'
    ascending_letters = sorted(letters) # a list of sorted letters based on unicode values
    ascending_letters = sorted(letters, reverse=True)

 

### Searching Sequences ###
def searcho():
    nums = [3, 7, 1, 5, 2, 0, 8]
    nums.index(7)
    nums.index('a')             # Throws an exception since no such element exists

    nums *= 2                   # Will double the list size, with repeated values... will become 
                                # [3, 7, 1, 5, 2, 0, 8, 3, 7, 1, 5, 2, 0, 8]
    
    nums.index(7, 10)           # Search for the element 7 starting at index 10

    print((1000 in nums))       # Prints False
    print((1000 not in nums))   # Prints True


def any_and_all():
    l1 = [1, 0, 2]
    l2 = [1, 2, 3]
    l3 = ["a", "", "c"]
    l4 = ["a", "b", "c",]
    # Built-in function any() checks if there are any non-False elements in a list
    any(l1)     # True
    any(l2)     # True
    any(l3)     # True
    any(l4)     # True

    # Built-in function all() checks if all indexes are occupied by a non-False element
    all(l1)     # False
    all(l2)     # True
    all(l3)     # False
    all(l4)     # True

    # A non-false element is one that is passed to the built-in bool() function and has a return value of True
    # 0, empty strings, and empty lists return False when passed into bool()
    # non-zero, non-empty strings, and non-empty lists return True when passed into bool()


### List methods ###
def list_methods():
    l = ['red', 'orange', 'blue']
    
    l.insert(0, 'grey')             # l becomes ['grey', 'red', 'orange', 'blue'
    l.append('green')

    # extend() takes a sequence and adds each element of the sequence into the list one at a time
    l.extend(['violet', 'indigo']) 

    l.remove('blue')

    l.clear()

    l.count('red')                  # how many times the 'red' element appears in a list

    l.reverse()

    l.pop()                         # returns the last element and removes it.
                                    # if no elements exist, an exception is thrown



### List Comprehensions ###
def l_comp():
    list1 = []
    for item in range(1, 6):
        list1.append(item)

    # The same thing, different syntax
    # Basically saying "For item in 1 through 5, add item to the list"
    list2 = [item for item in range(1, 6)]

    # The item added does not have to be the iterator value in the for loop
    rolls = [random.randrange(1, 7) for i in range(600)]

    # Mapping
    # Just like JavaScript map function
    # This example cubes each element before adding it
    list3 = [item ** 3 for item in range(1, 6)]

    # Mapping a list
    colors = ['red', 'green', 'blue']
    colors = [color.upper() for color in colors]
    # ['RED', 'GREEN', 'BLUE']
    
    # Filtering
    # Just like JavaScript filter function
    # This example filters out odd numbers
    list4 = [item for item in range(1, 11) if item % 2 == 0]

    

### Generator Expressions ### 
# - List comprehensions are greedy --- They immediately evaluate produce the list
# - Generator expressions are lazy --- They produce values on demand, only as needed or when requested
# - Therefore, generator expressions improve performacne and memory consumption
def gen_ex():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # The critical thing to understand is the parenthesis.
    # List comprehensions and generator expressions share the same syntax,
    # but a generator expression has paranthesis rather than square brackets.
    # Therefore, it is evaluated to produce one value for each loop cycle
    for i in (item * 2 for item in numbers if x % 2 == 0):
        print(i, end=' ')

    # You can't create a list using a generator expression
    not_a_list = (item for item in range(1, 5) if item % 2 == 0)
    print(not_a_list)     # Prints <generator object <genexpr> at 0x192389>



### More on Filtering, Mapping, and Reducing ###
# Filtering and mapping can be done using a list comprehension or a generator expresison
# However, part of Python's functional programming offers includes built-in functions.

# filter() and map() are higher-order functions. They are functions that receive other functions as arguments.
# - filter() accepts a sequence and a function that is used to determine a condition that must be satisfied for the filtering.
# - map() accepts a sequence and a function that is used to perform an operation on each element

# Remember that functions are objects
# They can be assigned to variables, passed to functions, and returned from functions
# You can pass named functions or use a lambda expression

## filter()
numbos = [1, 2, 3, 4, 5, 1, 2, 25, 1, 6, 0]
def is_odd(x):
    """Returns true if x is odd"""
    return x % 2 != 0

# filter() returns a sequence
list(filter(is_odd, numbos))


# The same thing can be accomplished using lambda expression
# The lambda expression is used to define a function in-line
# The function parameters follow the lambda keyword, followed by a colon, followed by one expression
list(filter(lambda x: x % 2 != 0, numbos))


## map()
list(map(lambda x: x ** 2, numbos))


## reduce()
# reduce() is used to apply an operation to elements in a sequence and reduce the elements to a single value
# the functools module provides the reduce() function to add this capability
from functools import reduce
numbas = [2, 4, 6]
reduce(lambda x, y: x + y, numbas, initial=1)
sum(numbas) # does the same thing



### Other Sequence Processing Functions ###
def seq_proc():
    print('Red' < 'orange')     # prints True because the numeric value of R comes before the numeric value of o
    ord('R')                    # prints the ordinal number of 'R' -- 82
    ord('o')                    # prints the ordinal number of 'o' -- 111

    # Providing a key argument for min() and max()
    colors = ['Red', 'orange', 'Yellow', 'green', 'Blue']
    min(colors, key=lambda str: str.lower())    # The key specifies a function that is used to assist in finding the min
                                                # Here, all the strings are lowercased before compared

    # Reversing a sequence
    numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
    numbers.reverse()
    # or
    reversed(numbers)
    # or
    reversed_numbers = [item for item in reversed([10, 3, 7, 1, 9, 4, 2, 8, 5, 6])]

    # zip() is a built-in fucntion that accepts multiple sequences of values, and pairs elements in each sequence into tuples
    # zip() doesn't return a sequence, it returns an iterator which may be used to iterate over
    names = ['Bob', 'Sue', 'Amanda']
    grade_point_averages = [3.5, 4.0, 3.75]
    for name, gpa in zip(names, grade_point_averages):
        print(f'Name={name}; GPA={gpa}')
        # Name=Bob; GPA=3.5
        # Name=Sue; GPA=4.0
        # Name=Amanda; GPA=3.75

    

### Fundamental Concept: Iterators and Sequences ###
# An iterable is antything that can be looped over with a for loop in Python
    # for item in some_iterable:
        # print(item)

# Sequences are a common type of iterable. Lists, tuples, ands strings are all sequences
# Sequences have a specific set of features: 
# - They can be indexed starting from 0 and ending at length - 1
# - They have a length
# - They can be sliced

# Examples of iterables that are not sequences are sets, dictionaries, files, and generators

# For loops in Python do not use indexes. They use iterators.
# An iterator is what's used to power iterables.
# An iterator can be obtained from any iterator.
# And the iterator can be used to manually loop over the iterable it came from.

# Example: 3 iterators... a set, a tuples, and a string
numbers = {1, 2, 3, 5, 7}
coordinates = (4, 5, 7)
words = "hello there"
# Using the built-in iter() function, an iterator can be obtained for each iterable
iter(numbers)       # <set_iterator object at 0x7f2b9271c860>
iter(coordinates)   # <tuple_iterator object at 0x7f2b9271ce80>
iter(words)         # <str_iterator object at 0x7f2b9271c860>

# Using the returned iterator, you can use the built-in next() function to obtained the next element in the iterable
next(numbers)       # 1
next(numbers)       # 2



### Two-Dimensional Lists ###
def two_d_lists():
    l = [[77, 68, 86, 73], [96, 87, 89, 81], [70, 90, 86, 81]]
    l[1][2] # prints 89