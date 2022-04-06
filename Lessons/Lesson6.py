##### LESSON 6 ######
### Dictionaries
### Word Counter
### Sets     




### Dictionaries ###
# Key types must be immutable -- int or string, for example
# Value types can be mutable or immutable

def dict_fun():
    country_codes = {'Finland': 'fi', 'South Africa': 'za', 'Nepal': 'np'}
    len(country_codes)          # prints 3 (3 key/value pairs)

    if country_codes:
        print('country codes is not empty')


    
def iter_dict():
    days_per_month = {'January': 31, 'February': 28, 'March': 31}

    # The item() method of a dictionary returns a key/value pair as a tuple
    for month, days in days_per_month.items():
        print(f'{month} has {days} days')


    # The keys() methods actually reuturns a 'view' into the dictionary
    # The view is kind of like a pointer at the original dictionary's data
    # If you iterate over the view, modify the dictionary, and iterate over the same view, 
    # the modified data will be reflected by the original view
    for month_name in days_per_month.keys():
        print(month_name, end=' ')

    days_per_month['October'] = 31

    # This will show the October key/value pair
    for month_name in days_per_month.keys():
        print(month_name, end=' ')

    #values() method
    for day in days_per_month.values():
        print(day)



def dict_operations():
    roman_numerals = {'I': 1, 'II': 2, 'III': 4}
    print(roman_numerals['II']) # Access a key's value

    # Changing a value
    roman_numerals['III'] = 3

    # Adding a key/value pair
    roman_numerals['IV'] = 4

    # Removing a key/value pair
    del roman_numerals['III']

    # pop() method -- Returns the value of a provided key, and removes that key/value pair from the dictionary
    roman_numerals.pop('I')
    
    # Referencing an non-existent key/value pair
    roman_numerals['X'] # Throws a KeyError exception
    # Instead of referencing it this way, use the get() method
    # The dictionary get() method does not throw an exception if there is no key/value pair that was requested.
    # Instead, it returns None
    roman_numerals.get('X')
    roman_numerals.get('X', 'X not in dictionary') # Returns the 'X not in dictionary' message if not found, instead of returning None

    print('III' in roman_numerals) # prints True because the key is in the dictionary

    # Update method
    country_codes = {}
    country_codes.update({'South Africa': 'za'})
    # or
    country_codes.update(Australia='au')
    # You can also pass tuples or a list of tuples, which will be unpacked into key/value pairs
    country_codes.update([('United States', 'us'), ('Russia', 'ru')])


def dict_comparisons():
    home_locations1 = {'Bob': 'New York', 'Mary': 'Los Angeles'}
    home_locations2 = {'Mary': 'Los Angeles', 'Bob': 'New York'}
    home_locations1 == 2    # Prints True. As long as dictionaries have the exact same key/value pairs, they are equal
                            # regardless of the order of key/value pairs

### Word count example using a dictionary
def word_count():
    text = ('this is sample text with several words '
             'this is more sample text')
    word_counts = {}

    # The string method split() is used to tokenize string and return each word in a list
    for word in text.split():
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    for word, count in sorted(word_count.items()):
        print(f'{word:<12}{count}')

    print('Number of unique words:', len(word_counts))



### Line Wrapping ###
# String can be wrapped to new lines several ways

# Using parenthesis, the 2 strings are molded into one by the Python interpreter
text1 = ('this is sample text with several words '
        'this is more sample text')

# You can also use a backslash instead of parenthesis
text2 = 'this is sample text with several words ' \
        'this is more sample text'

# Using a multi-ling string will include the provided text, verbatim (includes new lines and all white space)
text3="""this is sample text with several words
this is more sample text"""



### Collections Module ###
# The collections module provuides specialized container datatypes that are alternatives
# to Python's general purpose built-in containers: list, dict, set, and tuple

# The Counter type is a dict subclass for counting hashable objects
# Hashable objects are objects that can be used as keys in a dictionary or as elements in a set - typically
# strings or immutable types
from collections import Counter
text = ('this is sample text with several words '
        'this is more sample text')

# Creates a Counter object which is still a dictionary
counts = Counter(text.split())

for word, count in sorted(counts.items()):
    print(f'{word:<12}{count}')



### Dictionary Comprehensions ###
def dict_comp():
    months = {'January': 1, 'February': 2, 'March': 3}
    
    # In months2, the key is now the month number, and the value is the month name
    months2 = {number: name for name, number in months.items()}
    # An important note, when reversing a dictionary, you must check
    # that the keys are unique (which is guaranteed in any dictionary)
    # and that the values are unique. Otherwise, when a value turns into a key and is referenced twice,
    # some data will be erased when updating the new key

    # Another use for dictionary comprehensions is updating a dictonary's values
    grades = {'Sue': [98, 87, 94], 'Bob': [84, 95, 91]}
    grades2 = {k: sum(v) / len(v) for k, v in grades.items()}



### Sets ###
# Unordered collection of unique values
# Sets are mutable, elements in a set are immutable because they need to be hashable
# mainly used to determine membership of a value
# NEVER RELY ON ORDER OF ELEMENTS IN A SET
def set_fun():
    colors = {'red', 'orange', 'yellow', 'green', 'red', 'blue'}
    
    # Notice colors is not in order and only has unique values
    print(colors) # {'blue', 'green', 'orange', 'red', 'yellow'}

    # You cannot create an empty set with empty curly braces
    # Empty curly braces are used for creating dictionaries
    # Use the set() method to create an empty set
    set()
    # An empty set is literally represented as the string 'set()'

    # Frozen sets can be used to create a constant, immutable set

def compare_sets():
    {1, 3, 5} == {5, 1, 3} # True

    # subset comparison: the left set is a 'proper subset'
    {1, 3, 5} < {7, 3, 5, 1} # True

    # subset comparison: the left set is an 'improper subset'
    {1, 3, 5} <= {3, 5, 1} # True
    {1, 3, 5}.issubset({3, 5, 1}) # True
    
    # superset comparison: the left set is a 'proper superset'
    {7, 5, 1, 3} > {3, 5, 1} # True

    # superset comparison: the left set is an 'improper superset'
    {3, 5, 1} >= {3, 1, 5} # True
    {3, 5, 1}.issuperset({1, 5, 3}) # True


def set_operations():
    # the union() method is more flexible as it doesn't need a set as the argument
    {1, 3, 5}.union([20, 20, 3, 50, 50])
    # or
    {1, 3, 5} | {2, 3, 4}

    {1, 3, 5} & {2, 3, 4}
    # or
    {1, 3, 5}.intersection([1, 2, 2, 3, 3, 4, 4])

    # Removes elements from the set on the left that are in the set on the right
    {1, 3, 5} - {2, 3, 4} # {1, 5}
    {1, 3, 5}.difference({2, 3, 4}) # {1, 5}

    # Symmetric difference: keeps unique values
    {1, 3, 5} ^ {2, 3, 4} # {1, 2, 4, 5}
    {1, 3, 5}.symmetric_difference({2, 3, 4}) # {1, 2, 4, 5}

    # Disjoint: True if they have no elements in common, False if they do
    {1, 3, 5}.isdisjoint({7, 8, 9}) # True
    {1, 3, 5}.isdisjoint([2, 3, 4]) # False


def mutable_set_operators_and_methods():
    # |=    Union                   update
    # &=    Intersection            intersection_update
    # -=    Difference              difference_update
    # ^=    Symmetric difference    symmetric_difference_update

    numbers = {1, 3, 5}

    numbers |= {2, 3, 4}
    numbers.update([2, 3, 4])

    numbers &= {2, 3, 4}
    numbers.intersection_update([2, 3, 4])

    numbers -= {2, 3, 4}
    numbers.difference_update([2, 3, 4])
    
    numbers ^= {2, 3, 4}
    numbers.symmetric_difference_update([2, 3, 4])

    # Removing an item from a set
    numbers.remove(3)   # KeyError if item is not there
    numbers.discard(3)  # Doesn't throw an exception even if item isn't there

    numbers.pop()

    numbers.clear()
    
    
### Set Comprehensions ###
def set_comp():
    numbers = [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10]
    evens = {num for num in numbers if num % 2 == 0}
