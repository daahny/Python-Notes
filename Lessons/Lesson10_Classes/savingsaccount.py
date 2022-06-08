# savingsaccount.py
"""Subclass of Account to represent a savings account"""
from account import Account

class SavingsAccount(Account):
    def __init__(self, name, balance, account_number=000, interest_rate=0.0):
        # this statement says: use the built-in super() function to move up to the super class (Account) and invoke it's __init__()
        super().__init__(name, balance, account_number)

        self._interest_rate = float(interest_rate)
    
    @property
    def interest_rate(self):
        return self._interest_rate

    # Overridden __str__() method
    def __str__(self):
        """Return string representation of SavingsAccount for __str__()"""
        return f'Name: {self.name}\nBalance: {self.balance}\nAccount Number: {self.account_number}\nInterest Rate: {self.interest_rate}'