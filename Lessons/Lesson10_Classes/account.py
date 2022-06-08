# account.py
"""Docstring -- Account class definition."""

# Define a new type Account
class Account:
    """Account class for maintaining a bank account balance."""

    # The __init__ method is used to initialize objects of a class -- The Constructor
    # self refers to the initializing object, used to initialize properties (like this in Java)
    def __init__(self, name, balance, account_number=000):
        """Initialize an Account object"""

        if balance < 0.0:
            raise ValueError('Initial balance cannot be less than 0.00')

        try:
            self.balance = float(balance)
        except TypeError:
            print('TypeError -- provided balance is not float-compatible. Setting balance to 0.00.')
            self.balance = 0.0
        
        self.name = name

        # account_number actually has properties defined in this class below. 
        # Therefore, this expression would call those expressions rather than initializing the variable inline here
        self.account_number = account_number
    

    ## Benefits Of Using Properties
    # You can access instance attributes exactly as if they were public attributes while using the "magic" of intermediaries (getters and setters) 
    # to validate new values and to avoid accessing or modifying the data directly.
    # Also, by using @property, you can "reuse" the name of a property to avoid creating new names for the getters, setters, and deleters.

    # The @property statement is an example of a decorator.
    # A decorator is used to conveniently alter the functionality of a method/function without having to directly change the source code.
    # In this case, @property defines a getter used to return a class attribute
    # account number getter
    @property
    def account_number(self):
        """Return the hour."""
        return self._account_number

    # account number setter
    # **without a property setter, a property is read-only**
    @account_number.setter
    def account_number(self, account_number):
        """Set the account number."""

        # properties with a preceeding underscore are, by naming convention, private
        self._account_number = account_number



    # Any instance method like this one will implicitily receive the calling object as the first argument.
    # Therefore, you must have the object as the first parameter of an instance method.
    def deposit(self, amount):
        """Deposit money to the account."""

        if amount < 0.0:
            raise ValueError('Amount must be greater than zero')

        self.balance += amount

    
    def withdraw(self, amount):
        """Withdraw money from the account."""

        if amount < 0.0:
            raise ValueError('Amount must be greater than zero.')
        elif amount > self.balance:
            raise ValueError('Amount cannot be greater than balance.')
        
        self.balance -= amount

    
    # repr() is used to return a printable representation of a given object. Used for debugging and should be information rich.
    def __repr__(self):
        """Return string representation of Account."""
        return f'Account(name={self.name}, balance={self.balance}, account_number={self.account_number})'

    def __str__(self):
        """Return string representation of Account when __str__() is implicitly invoked like in a print statement."""
        return f'Name: {self.name}\tBalance: {self.balance}\tAccount Number: {self.account_number}'
