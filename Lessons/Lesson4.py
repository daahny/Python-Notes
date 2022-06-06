##### Lesson 4 #####
### Functions
### Default Parameters
### Arbitrary Arguments List
### Local and Global Scope
### Passing Arguments

### Functions ###
def square(number):
    """Calculate the square of number.
    Python docs recommend you to include a docstring at the beginning of each function."""
    return number ** 2
    # if no return value is specified, a python function will return None



### Default Parameter Values ###
def rectangle_area(length=2, width=3):
    """Returns a rectangle's area."""
    return length * width

rectangle_area()    # returns 6
rectangle_area(10)  # returns 30
# Keyword arguments
rectangle_area(width=30, length=3)
rectangle_area(width=20)



### Arbitrary arguments list ###
# All arugments passed to this function will be packed up into the tuple args
def average(*args):
    return sum(*args) / len(*args)

average(5, 10) # 7.5
average(5, 10, 15) #10.0
grades = [88, 75, 55]
average(grades)



### Methods ###
# Methods are functions that are part of a class
s = 'Hello'
s.capitalize()



### Local and Global Scope ###
# Duplicate variable names are shadowed by the local instance during the duration of function call
x = 7
def print_x():
    print(x) # prints 7

def try_to_modify_x():
    x = 3.5
    print(x) # prints 3.5
print(x) # still prints 7
# The local instance of x shadowed the global instance of x during the function call

def modify_x():
    global x # Tells the interpreter to refer to the global instance of x
    x = 'hello'
    print(x) # prints hello
print(x) # prints hello



### Passing arguments ###
# Pass-by-value
# Arguments passed to a function are copies of the orginal. Any modifications to the copy
# do not effect the original
#------------------
# Pass-by-reference
# Arguments are passed by reference where the called function can modify the value (assuming its mutable)
# *Everything in Python is passed by reference
# Important to note, some objects are immutable. So, when a variable is modified, a new object is actually created.
# Examples of an immutable object are int, string, tuple
# When a mutable object such as a list
# https://www.geeksforgeeks.org/is-python-call-by-reference-or-call-by-value/
x = 7
print(f'id of x ({x}): ', id(x))

def cube(number):
    print('id of number: ', id(number))
    number **= 3
    print('id of number after cube: ', id(number))

cube(x)
print(f'id of x ({x}) after cube: ', id(x))
# x will remain the same even though it is pass by reference
# a new object will simply be created and number will point to another object