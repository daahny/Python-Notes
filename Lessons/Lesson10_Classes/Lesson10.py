##### Lessson 10 #####
### Demo Class - Account
### Demo Classes - Card and DeckOfCards
### Base Classes and Subclasses
### issubclass() and isinstance() 



### Demo Class - Account
# This from statement first checks for libraries part of the installation called account.
# If nothing is found, it'll check the current directory for an account.py file with an Account class.
from account import Account
account1 = Account('Jake', 100.00, 399)
print(repr(account1))



### Demo Classes - Card and DeckOfCards
from deckofcards import DeckOfCards
deck1 = DeckOfCards()
print(deck1)
deck1.shuffle()
print(deck1)
for i in range(53):
    print(deck1.deal_card())



### Base Classes and Subclasses
from savingsaccount import SavingsAccount
sav1 = SavingsAccount('Jane', 1000.00, 500, 0.06)
print(sav1)



### issubclass() and isinstance() 
issubclass(SavingsAccount, Account) # True
isinstance(sav1, SavingsAccount)    # True



### Duck Typing
# A programming style which does not look at an object's type to determine if it has the right interface;
# instead, the method or attribute is simply called or used.
# "If it looks like a duck, talks like a duck, walks like a duck... It's a duck."
#
# In python, this provides tremendous flexibility as it gives you the ability to process different objects of different types
# all in the same manner.
# For example, as long as it has the __str__() method, you can do this:
l = [account1, sav1]
for i in range(2):
    print(l[i].__str__())