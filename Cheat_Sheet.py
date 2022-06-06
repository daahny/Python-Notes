# Built-in Functions
# Common Errors
# Lists and List Operations
# Comprehensions and Generator Expressions
# Dictionaries
# String Formatting
# Substrings
# Strings
# Regular Expressions
# File Processing


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



### Lists and list operations
def lis_opr():
    l = [0, 1, 2]
    l[100]                  # Throws IndexError: list index out of range
    l += [3]                # Added element must be an iterable

    l = ['red', 'orange', 'blue']
    l.insert(0, 'grey')
    l.append('green')
    l.extend(['violet', 'indigo']) 
    l.remove('blue')
    l.clear()
    l.count('red')
    l.reverse()
    l.pop()
    any(l)                  # Any non-False elements
    all(l)                  # All non-False elements



### Sequence operations
def seq_opr():
    letters = 'jhabsofyguq'
    letters.index('h')
    letters.count('f')
    letters.sort()
    sorted(letters)
    letters.reverse()



### Comprehensions and generator expressions
def com_gen():
    list_a = [item for item in range(11)]
    for i in (item for item in range(11) if item % 2 == 0):
        print(i)
    dict_a = {'US': 1, 'CH': 2}
    dict_b = {number: name for name,number in dict_a.items()}
    


### Filtering and Mapping
def fil_map():
    mapped_list = [char + '!' for char in 'ABCDEFG']
    list(map(lambda char: char + '!', 'ABCDEFG'))
    filtered_list = [char for char in 'ABCDEFG' if ord(char) % 2 == 0]
    list(filter(lambda char: ord(char) % 2 == 0, 'ABCDEFG'))



### Dictionaries
def dic():
    roman_numerals = {'I': 1, 'II': 2, 'III': 4}
    roman_numerals.items()
    roman_numerals.keys()
    roman_numerals.values()
    roman_numerals['III'] = 3               # Changing a value
    roman_numerals['IV'] = 4                # Adding a key/value pair
    del roman_numerals['III']
    roman_numerals.pop('I')
    roman_numerals.get('X')
    roman_numerals.update({'V': 5})
    roman_numerals.update({'VI': 6, 'VII': 7})



### String formatting
def str_for():
    f'{17.489:.2f}'
    f'{65:c}'                   # 'A'
    f'{"hello":s}'
    f'{254:b}'                  # base 2
    f'{254:o}'                  # base 8
    f'{254:d}'                  # base 10
    f'{254:x}'                  # base 16
     
    f'[{"hello":<10}]'          # [hello     ]
     
    '{0} {0} {1}'.format('Happy', 'Birthday')
    '{firs} {las}'.format(firs='Cyan', las='Amanda')



### Substrings
def sub_str():
    sentence = 'to be or not to be that is the question'
    sentence.count('to')        
    sentence.count('to', 12)    
    sentence.index('be')        
    sentence.rindex('be')       

    sentence.find('be')         # returns -1 instead of ValueError like index()
    sentence.rfind('be')        
    'that' in sentence          
    'THAT' in sentence          
    sentence.startswith('to')   
    sentence.endswith('be')



### Strings
def str_str():
    letters = 'A, B, C, D'
    letters.split(', ')                 # List of strings delineated by a comma and a space

    lines = """Line1
    Line2
    Line3"""
    lines.splitlines()                  # ['Line1', 'Line2', 'Line3']

    ",".join(letters)                   # 'A,B,C,D'
    ",".join([str(i) for i in range(10)])

    values = '1\t2\t3\t4'
    values.replace('\t', ',')   # 1,2,3,4



### Regular Expressions
### Regular Expression Metacharacters
## Quantifiers
# {n}   match the preceeding element n times
# {3,}  match the preceeding element 3 or more times
# {3,6} match the preceeding element 3, 4, 5, or 6 times
# *     match the preceeding element any number of times
# +     match the preceeding element one or more times
# ?     match the preceeding element zero or one time

## Metacharacters
# \d    any digit
# \D    any non-digit
# \s    any whitespace
# \S    any non-whitespace
# \w    any alphanumeric (word) character, includes uppercase and lowercase letters, digits, and an underscore
# \W    any non word character
# []    define metacharacters as literal characters -- anything in [] will be treated literally
# []    define a set -- [A-Z] or [a-z] or [1-9] or [A-Za-z1-9]
# [^]   define a not set -- [^a-p] means any character not between a and p
# ()    match whatever regular expression is inside the paranthesis, and indicates the start and end of a group


#   regular expression object:  an object that is returned from the compile() function, supports a variety of functions
#   match object:               the object returned from a matching function: https://docs.python.org/3/library/re.html#match-objects


import re
def regex():
    # re flags
    result = re.search('Sam', 'SAM', flags=re.IGNORECASE)           # Ignores case
    result = re.search('^e.*$', 'e\na\ne', flags=re.MULTILINE)      # The '^' matches at the beginng of each string AND the beginning of each line
    result = re.search('.*', '\n', flags=re.DOTALL)                 # . will match new lines as well
    
    # re.sub() and re.split()
    re.sub(r'\t', ', ', '1\t2\t3\t4')                   # '1, 2, 3, 4'
    re.split(r',\s*', '1, 2,   3,4,  5, 6,   7,8')      # ['1', '2', '3', '4', '5', '6', '7', '8']

    # re.search() and re.group()
    result = re.search('Python', 'Python is fun')       # Returns match object
    result.group() if result else 'not found'

    # re.findall() -- list of all matched objects
    contact = 'Wally White, Home: 555-555-1234, Work: 555-555-4321'
    re.findall(r'\d{3}-\d{3}-\d{4}', contact)                       # ['555-555-1234', '555-555-4321']

    # re.finditer() -- returns an iterator that provides SRE_Match objects one at a time
    for phone in re.finditer(r'\d{3}-\d{3}-\d{4}', contact):
        print(phone.group())

    # re.groups() and re.group() -- capturing substrings in a match
    # Each subexpression (paranthesis containg a regular expressions) will be returned as a group. These matches can be obtained using the object groups() method.
    result = re.search(r'([A-Z][a-z]+ [A=Z][a-z]+), e-mail: (\w+@\w+\.\w{3})', 'Charlie Cyan, e-mail: demo@example.com')
    print(result.groups())                  # Tuple -- ('Charlie Cyan', 'demo@example.com')
    print(result.group(1))                  # String -- 'Charlie Cyan'
    print(result.group(0))                  # String -- 'Charlie Cyan, e-mail: demo@example.com'

    # re.compile() -- compiles a regular expression pattern into a regular expression object,
    # which can be used for matching using its match(), search(), and other methods
    reg_exp_obj = re.compile(r'^\d{3}$')
    result = reg_exp_obj.search('123')



# File Processing
# Classes for file objects defined in Python Standard Library's io module: https://docs.python.org/3/library/io.html
def txt_pro():
    with open('accounts.txt', mode='w') as accounts:
        accounts.write('100 Jones 24.98\n')
        accounts.write('200 Doe 345.67\n')
        accounts.write('300 White 0.00\n')
    
    with open('accounts.txt', mode='r') as accounts:
        for record in accounts:
            account, name, balance = record.split()
            print(f'{account:<10}{name:<10}{balance:,10}')

def txt_upd():
    with open('accounts.txt', 'r') as accounts, open('temp_file.txt', 'w') as temp_file:
        for record in accounts:
            account, name, balance = record.split()
            if account != '300':
                temp_file.write(record)
            else:
                new_record = ' '.join([account, 'Williams', balance])
                temp_file.write(new_record + '\n')

    import os
    os.remove('accounts.txt')
    os.rename('temp_file.txt', 'accounts.txt')


# read()            No arguments - entire contents of file. Number n argument specifies number of characters to retrieve
# readline()        Returns one line of text as a string, including the newline. Returns empty string on end-of-file
# readlines()       Return all text as a single string
# write()           writes a string to one line
# writelines()      Writes of a sequence of strings to a file



### JSON
import json
def json_ser_dsr():
    accounts_dict = {'accounts': [{'account': 100, 'name': 'Jones', 'balance': 24.98}, 
                                  {'account': 200, 'name': 'Doe', 'balance': 345.67}]}

    # json.dump() -- accept a python object and dump that, as JSON format, into the provided file object
    with open('accounts.json', 'w') as accounts:
        json.dump(accounts_dict, accounts)

    # json.load() -- accept a file object and return a python dictionary
    with open('accounts.json', 'r') as accounts:
        accounts_dict = json.load(accounts)
    
    # json.dumps() -- beautify the JSON stream
    with open('accounts.json', 'r') as accounts:
        print(json.dumps(json.load(accounts), indent=4, sort_keys=False))
    