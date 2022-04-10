##### Lesson 8 #####
### Formatting Strings
### Formatting Strings -- Field Widths and Alignment
### Formating Strings  -- Numeric Formatting
### Formatting Strings -- String's Format Methods
### Concatenating and Repeating Strings
### Stripping Whitespace From Strings
### Changing Character Case
### Searching For Substrings
### Replacing Substrings
### Splitting and Joining Strings
### Characters and Character-Testing Methods
### Raw Strings
### Regular Expression Metacharacters
### Regular Expressions -- Matching Literals
### Regular Expressions -- Replacing Subsstrings and Splitting Strings
### Regular Expressions -- Searching and Matching (and re flags)
### Regular Expressions -- Capturing Substrings in a Match
### Regular Expressions -- re.compile()



### Formatting Strings
def for_str():
    # Format specifiers -- https://docs.python.org/3/library/string.html#formatspec
    f'17.489:.2f'    # Round to 2 decimal points as a floating point representation

    f'{65:c}'        # Format the number 65 as a character -- 'A'

    f'{"hello":s}'   # Format as a string (the default format specifier)

    from decimal import Decimal
    f'{Decimal("1000000000000000.0"):.3f}'   # 1000000000000000.000
    f'{Decimal("1000000000000000.0"):.3e}'   # 1.000e+25
    f'{Decimal("1000000000000000.0"):.3E}'   # 1.000E+25

    f'{254:b}'       # 254 as binary format      base 2
    f'{254:o}'       # 254 as octal format       base 8
    f'{254:d}'       # 254 as decimal format     base 10
    f'{254:x}'       # 254 as hex format         base 16



### Formatting Strings -- Field Widths and Alignment
def wid_ali():
    f'[{27:10d}]'               # [        27]
    f'[{3.5:10f}]'              # [  3.500000] -- right alignment is default for floats, 6 points of precision is default for formatted floats
    f'[{"hello":10}]'           # [hello     ]
    f'[{27:<15d}]'              # [27             ]
    f'[{27:<15f}]'              # [27.000000      ]
    f'[{"hello":15}]'           # [hello          ]
    f'[{27:^7d}]'               # [  27   ]
    f'[{"hello":^7}]'           # [ hello ]



### Formating Strings -- Numeric Formatting
def num_for():
    f'[{27:+10d}]'              # [       +27]

    f'[{27:+010d}]'             # [+000000027] -- Specifies the padding

    f'{27: d}\n{-27: d}'        #  27          -- Allows positive and negative to be aligned
                                # -27

    f'{12345678:,.2f}'          # 12,345,678.00 -- Insert commas by the thousandths



### Formatting Strings -- String's Format Methods
def for_met():
    '{.2f}'.format(17.489)                          # 17.59

    '{} {}'.format('Amanda', 'Cyan')                # Amanda Cyan

    '{0} {0} {1}'.format('Happy', 'Birthday')       # Happy Happy Birthday

    '{firs} {las}'.format(firs='Cyan', las='Amanda')



### Concatenating and Repeating Strings
def con_rep():
    s1 = 'happy'
    s2 = 'birthday'

    s1 += ' ' + s2              # 'happy birthday'

    symbol = '>'
    symbol *= 5                 # '>>>>>'



### Stripping Whitespace From Strings
def stp_str():
    cuisine = " greek "
    # Strips all whitespace including new lines and tabs
    print(cuisine.rstrip())     # " greek"
    print(cuisine.lstrip())     # "greek "
    print(cuisine.strip())      # "greek"



### Changing Character Case
def chr_cas():
    name = "ada lovelace"
    print(name.title())         # Ada Lovelace
    print(name.upper())         # ADA LOVELACE
    print(name.lower())         # ada lovelace



### Searching For Substrings
def ser_sub():
    sentence = 'to be or not to be that is the question'

    sentence.count('to')        # 2 occurrences of count
    sentence.count('to', 12)    # 1 occurrence of count at index 12

    sentence.index('be')        # 3 is the first occurrence where 'be' starts

    sentence.rindex('be')       # 16, search backwards

    sentence.find('be')
    sentence.rfind('be')        # returns -1 if not found instead of a ValueError like index and rindex

    'that' in sentence          # True
    'THAT' in sentence          # False

    sentence.startswith('to')   # True
    sentence.endswith('be')     # False



### Replacing Substrings
def rep_sub():
    values = '1\t2\t3\t4'
    values.replace('\t', ',')   # 1,2,3,4



### Splitting and Joining Strings
def spl_joi():
    # Split method -- Split a string into a sequence of strings delineated by an optional delimeter
    letters = 'A, B, C, D'

    letters.split(', ')                 # List of strings delineated by a comma and a space

    lines = """Line1
    Line2
    Line3"""
    lines.splitlines()                  # ['Line1', 'Line2', 'Line3']

    # Join method -- Concatenate strings by inserting the calling string between each string
    ",".join(letters)                   # 'A,B,C,D'
    ",".join([str(i) for i in range(10)])

    # Partition method -- Grab a tuple of 3 elements --> one part of the string, the delimeter, and the other part
    "Amanda: 98, 74".partition(': ')    # ('Amanda', ': ', '98, 74')
    url = 'http://deitel.com/books/PyCDS/table_of_contents.html'
    rest_of_url, separator, document = url.rpartition('/')
    # rest_of_url = 'http://deitel.com/books/PyCDS'
    # separator = '/'
    # document = 'table_of_contents.html'



### Characters and Character-Testing Methods
def cha_tes():
    '-27'.isdigit()         # False because every character is not a digit
    '27'.isdigit()          # True
    'A9876'.isalnum()       # True
    'A B C'.isalnum()       # False



### Raw Strings
def raw_str():
    # In a raw string, every character is part of the string and no expansions or escapes shall be made
    file_path = 'C:\\MyFolder\\MySubFolder\\MyFile.txt'

    file_path_raw = r'C:\MyFolder\MySubFolder\MyFile.txt'



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




### Regular Expressions -- Matching Literals
import re
def mat_lit():
    pattern = '02215'

    # Ternary operator fun for ya
    # re.fullmatch returns a match object that evaluates to True or False if the entirity of the literal arguments are matched
    # Match objects: https://docs.python.org/3/library/re.html#match-objects
    'Match' if re.fullmach(pattern, '02215') else 'No match'

    # Notice the regular expression is a raw string. This is to prevent any escaping before the string is passed
    # to the fullmatch() method
    'Valid' if re.fullmatch(r'\d{5}', '02215') else 'Invalid'

    

### Regular Expressions -- Replacing Subsstrings and Splitting Strings
def sub_spl():
    re.sub(r'\t', ', ', '1\t2\t3\t4')                   # '1, 2, 3, 4'

    re.split(r',\s*', '1, 2,   3,4,  5, 6,   7,8')      # ['1', '2', '3', '4', '5', '6', '7', '8']



### Regular Expressions -- Searching and Matching
def re_ser():
    # re.search() returns an SRE_Match object if a match is found anywhere in the sring.
    result = re.search('Python', 'Python is fun')

    # Evaluates to result.group(), which is the matching group 'Python'
    result.group() if result else 'not found'           


    # Flags: https://docs.python.org/3/library/re.html#module-contents
    result = re.search('Sam', 'SAM', flags=re.IGNORECASE)           # Ignores case
    result = re.search('^e.*$', 'e\na\ne', flags=re.MULTILINE)      # The '^' matches at the beginng of each string AND the beginning of each line
    result = re.search('.*', '\n', flags=re.DOTALL)                 # . will match new lines as well


    # Returns a list of all matched values
    contact = 'Wally White, Home: 555-555-1234, Work: 555-555-4321'
    re.findall(r'\d{3}-\d{3}-\d{4}', contact)                       # ['555-555-1234', '555-555-4321']
    
    # finditer() returns an iterator that provides SRE_Match objects one at a time
    for phone in re.finditer(r'\d{3}-\d{3}-\d{4}', contact):
        print(phone.group())
    


### Regular Expressions -- Capturing Substrings in a Match
def cap_sub():
    # Paranthesis () define a set of regular expressions to match. 
    # Each subexpression (paranthesis containg a regular expressions) will be returned as a group.
    # These matches can be obrtained using the object groups() method
    text = 'Charlie Cyan, e-mail: demo@example.com'
    pattern = r'([A-Z][a-z]+ [A=Z][a-z]+), e-mail: (\w+@\w+\.\w{3})'

    result = re.search(text, pattern)

    # Note, the tuple indexing on the group() tuple starts at 1 because 0 represents the entire string
    print(result.groups())                  # Tuple -- ('Charlie Cyan', 'demo@example.com')
    print(result.group(1))                  # String -- 'Charlie Cyan'
    print(result.group(0))                  # String -- 'Charlie Cyan, e-mail: demo@example.com'



### Regular Expressions -- re.compile()
def re_comp():
    # re.compile() compiles a regular expression pattern into a regular expression object,
    # which can be used for matching using its match(), search(), and other methods

    # Using re.compile() is more efficient when the expression will be used several times in a single program
    pattern = r'^\d{$}$'
    text = '123'
    
    reg_exp_obj = re.compile(pattern)
    reg_exp_obj.search(text)
    # is the same as
    re.search(pattern, text)
    
