##### Lesson 9 #####
### Files
### Text File Processing -- open(), with, write(), read()
### Text File Processing -- Updating 
### Other File Object Methods -- read(), readlines(), write(), writelines()
### Serialization with JSON -- Serializing
### Serialization with JSON -- Deserializing
### Serialization with JSON -- Display Formatted JSON Text
### Serialization with JSON -- Bringing it all together
### Handling Exceptions
### Raising Exceptions
### Working with CSVs



### Files
# Text files are viewed as a sequence of characters. 
# The first index is the first character
#
# Binary files are viewed as a sequence of bytes (images, videos)
#
# sys module's standard file descriptors
# sys.stdin
# sys.stdout
# sys.stderr



### Text file processing -- open(), with, write(), read()
def txt_pro():
    # open() opens a file in a given access mode
    # 'r' for read, 'w' for write, 'a' for append, 'r+' and 'w+' for read and write, 'a+' for read and append.
    # *when opening for writing, contents will be erased
    
    # The returned file object depends on the file type and the mode used on the file
    open('accounts.txt', mode='w')


    # The with statement is to acquire a resource, use it in the body of the with statement,
    # then give the resource back to the system once the block finishes execution.
    with open('accounts.txt', mode='w') as accounts:
        # [Account number] [Name] [Account balance (float)]
        accounts.write('100 Jones 24.98\n')
        accounts.write('200 Doe 345.67\n')
        accounts.write('300 White 0.00\n')
        accounts.write('400 Stone -42.16\n')
        accounts.write('500 Rich 224.62')


    # Only works if the file exists at the specified location
    with open('accounts.txt', mode='r') as accounts:
        # File objects are iterable in Python. For text files, each iteration returns a record
        # separated by a newline
        for record in accounts:
            account, name, balance = record.split()
            print(f'{account:<10}{name:<10}{balance:,10}')
        
        accounts.readlines()        # Returns all text as a single string



### Text File Processing -- Updating
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



### Other File Object Methods
# read()            No arguments - entire contents of file. Number n argument specifies number of characters to retrieve
# readline()        Returns one line of text as a string, including the newline. Returns empty string on end-of-file
# write()           writes a string to one line
# writelines()      Writes of a sequence of strings to a file

# Classes for file objects defined in Python Standard Library's io module: https://docs.python.org/3/library/io.html



### Serialization with JSON
# Values in JSON objects and arrays can be
# - Strings in double quotes
# - Numbers
# - JSON Boolean values (true or false)
# - null (to represent no value, like None in Python)
# - arrays
# - other JSON objects


### Serialization with JSON -- Serializing an Object to JSON
import json
def ser_obj():
    accounts_dict = {'accounts': [{'account': 100, 'name': 'Jones', 'balance': 24.98}, 
                                  {'account': 200, 'name': 'Doe', 'balance': 345.67}]}

    with open ('accounts.json', 'w') as accounts:
        # dump() accepts a python object that is to be converted to JSON, and a file object accepting
        # the converted JSON
        json.dump(accounts_dict, accounts)



### Serialization with JSON -- Deserializing a JSON Object into Python
def dsr_obj():
    with open('accounts.json', 'r') as accounts:
        # load() accepts a file object and loads JSON. It returns a Python dictionary.
        accounts_dict = json.load(accounts)

    accounts_dict['accounts']
    accounts_dict['accounts'][0]



### Serialization with JSON -- Display Formatted JSON Text
def for_jsn():
    with open('accounts.json', 'r') as accounts:
        # dumps() accepts a object and transfers it to a pretty JSON format
        print(json.dumps(json.load(accounts), indent=4, sort_keys=False))



### Serialization with JSON -- Bringing it all together
def jsn_fin():
    accounts_dict = {'accounts': [{'account': 100, 'name': 'Jones', 'balance': 24.98}, 
                                {'account': 200, 'name': 'Doe', 'balance': 345.67}]}

    with open('accounts.json', 'w') as accounts:
        json.dump(accounts_dict, accounts)

    with open('accounts.json', 'r') as accounts:
        print(json.dumps(json.load(accounts), indent=4))



### Handling Exceptions
# A number of exceptions can be thrown at runtime relating to file operations
# FileNotFoundError     Open a non-existent file for reading
# PermissionsError      Attempt an unauthorized operation
# ValueError            Attempt to write to a closed file

# Try statement
# try:      (stuff that may throw errors)
# except:   (stuff that executes if an error is thrown)
# else:     (stuff that executes only if no errors were thrown)
# finally:  (stuff that executes always, at the end of a try statement)

def try_sta():
    while True:
        try:
            number_one = input('Enter numerator: ')
            number_two = input('Enter denominator: ')
            result = number_one / number_two
        except ValueError:
            print('You must input only integers!')
        except ZeroDivisionError:
            print('Cannot divide by zero!')
        else:
            print(f'{number_one:.3f} / {number_two:.3f} = {result:.3f}')
            break



### Raising Exceptions
# Built-in exception:   https://docs.python.org/3/library/exceptions.html
# All exceptions are instances of a class that derivces from BaseException.
# A try statement catching an exception will also catch subclasses of that exception
def rai_exn():
    # ***Always release resources when applicable before raising an exception
    raise BaseException
    # BaseException is not meant to be directly inherited (use Exception instead)



### Working with CSV Files
import csv

# Recommended to set the newline argument to '', as this allows the csv module to properly handle newline characters on its own (this functionality is built into the module)  
with open('accounts.csv', mode='w', newline='') as accounts:
    # csv.writer() accepts a text file object and returns a writer object used to write csv values
    writer = csv.writer(accounts)
    writer.writerow([100, 'Jones', 24.98])
    writer.writerow([200, 'Doe', 345.67])
    writer.writerow([300, 'White', 0.00])
    writer.writerow([400, 'Black, Brown, Blue', 50.00])

with open('accounts.csv', mode='r', newline='') as accounts:
    reader = csv.reader(accounts)
    # the reader object is an iterable, returning lists, each list containing fields of each record
    print(reader.__next__())
    for record in reader:
        print(record)