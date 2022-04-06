##### Lessons 1-3 #####
### Variables and Types
### Strings and String Methods
### Getting Input
### Basic Control Flow
### Looping
### Built-in Functions
### Exceptions
### Modules and Import
### Random and Time Modules
### Casting
### Printf
### Compound Interest Example

### Variables ###
# Basic primitives types: 
# int
# float
# string
# bool
print(type(True))



### Strings ###
def strings():
    name = "ada lovelace"
    print(name.title()) # Ada Lovelace
    print(name.upper()) # ADA LOVELACE
    print(name.lower()) # ada lovelace

    cuisine = " greek "
    print(cuisine.rstrip()) # " greek"
    print(cuisine.lstrip()) # "greek "
    print(cuisine.strip()) # "greek"

    print("a7ii " * 3) # a7ii a7ii a7ii 
    print("a7ii", end="") # omit the new line after printing a string

    print(1, 2, 3, sep=", ")

    sentence = "This sentence has an apsotrophe and is still a complete string."
    sentence2 = 'This sentence is delimited with a single quote and not a double quote "'

    multi_line_string = """
    One
    Two
    Three
    """



### Integer operations ###
# + Addition
# - Subtraction
# * Multiplication
# / Division (results in float)
# // Integer Division (results in int)
# ** Exponentiation
# % Remainder or Modulo



### I/O ###
def io():
    user_input = input('This is the prompt message: ')
    print('hello ' + user_input)



### Control flow ###
def control_flow():
    if bool:
        print("bool is true")
    bool_expression = (not 1 == 2)       # This equates to True
    if bool_expression:
        print("True")
    elif not bool_expression == True:
        print("Not true")
    else:
        print("Error")

    x = 5
    if 1 <= x <= 5:
        print("chained comparison!")

    if True and True:
        print('voila')
    if False or False:
        print('impossible!')
    if True and not False:
        print('voila')

    # The paranthesis are tuples, not ranges/sequences
    if 1 in (1, 2, 3):
        print("true")
    if "no" in (7, 11):
        print('non')
    


### Looping ###
def looping():
    for i in range(5): # 5 is not inclusive
        print("i is ", i)
    for j in range(1, 10, 2): # 10 is not inclusive
        print("j is ", j)
    
    for char in 'abcde':
        print(char, end=' ') # a b c d e

    for num in [8, 0, 1, -9, 10]: # list defined by square brackets
        print(num)

    count = 0
    while count < 5:
        print(count)
    


### Built-in functions ###
# Python includes several built-in functions
def built_in():
    abs(-4.3) # absolute value of a number
    max(3, 4, 5) # larger of 2 or moreintegers
    min(3, 4) # smaller of 2 or more integers
    round(3.467, 2) # round 3.467 to 2 decimal places
    len(list) # get the length of an iterable
    sorted(list) # returns a sorted list
    sum(list) # accepts parameters or a sequnce and returns the sum



### Common errors ###
# SyntaxError - Error caused by python syntax (structure) violations
# NameError   - Error caused when the interpreter detects a variable that is unknown
# TypeError   - Error caused when an operation is applied to an inappropriate object
# Function signature - The name of a function along with the number of parameters it requires
# Calling a function with the incorrect number of arguments/'actual parameters' will produce a TypeError



### Modules and Import ###
# Module - A unit of python library functionality
# Import - Request to access a python module/class? in your code
# You can import classes from a library module:
from decimal import Decimal     # Decimal class from decimal library module
import math                     # entire math module
from math import ceil, floor    # just ceil, and floor functions

# important: when importing something from a library module using the 'from' keyword, those things
# will be brought into the global namespace. This means functions such as ceil do not need module reference.
# i.e.: instead of math.floor() you can use floor()

# wildcard imports can be dangerous (poor programming practice)
e = 'hello'
from math import *
print(e)    # prints euler's number (2.7182....)

# aliasing module names
import statistics as stats
stats.mean([15, 10, 7])



### Random module ###
import random
# random.choice() - randomly choose an element in a list/sequence
def randomize():
    r1 = random.randrange(1, 100, 2) # random integer in the range of [1,100) with a step of 2
    r2 = random.randint(1, 10) # random integer between 1 and 9
    random.seed(1042) # set the initial number for the random number generator. By default, the system time is used



### Time module ###
import time
def timeize():
    time.sleep(.1) # sleep for 100 milliseconds
    time.time() # current time in seconds since the epoch



### Casting ###
def casting():
    name = str(input("What is your name?"))
    age = int(input("What is your age?")) # ValueError will be thrown if input is not an int
    float("3.4")



### Print fstring ###
def printf():
    model = 'a7ii'
    print(f"My camera model is a sony {model}")

    flapa = 4.9 / 3.2
    print(f"Flapa is {flapa:.2f}") # Include 2 decimal points

    print(f"{flapa:>2.2f}") # Right align with a field width of 2, use 2 decimal points



### Compound interest example ###
# Decimal is an object used to store exact decimal values, avoids rounding errors with floats
from decimal import Decimal
def compound_interest():
    # amount = prinicipal * (1 + rate) ** year
    principal = Decimal('1000.00')
    rate = Decimal('0.05')
    for year in range(1, 11):
        amount = principal * (1 + rate) ** year
        print(f'{year:>2}{amount:>10.2f}')
# Output:
#  1   1050.00
#  2   1102.50
#  3   1157.62
#  4   1215.51
#  5   1276.28
#  6   1340.10
#  7   1407.10
#  8   1477.46
#  9   1551.33
# 10   1628.89



