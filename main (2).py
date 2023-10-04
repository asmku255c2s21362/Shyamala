Implement a class called BankAccount that represents a bank account. The class should 

have private attributes for account number, account holder name, and account balance. Include 

methods to deposit money, withdraw money, and display the account balance. Ensure that the 

account balance cannot be accessed directly from outside the class. Write a program to create an 

instance of the BankAccount class and test the deposit and withdrawal functionality.
class bank account:
def__unit__(self,account_number,account_holder_name,initial_balance_00):
self__account_number=accont_number
self__account_holder_name=account_holder_name
self__account_balance=initial_balance
def deposit(self,amount):
if amount>0:
self.__account_balance+=amount
print(“deposited $():new balance:$()”.format(amount,self.__account_balance))
else:
print(“invalid deposit amount.please deposit a positive amount”)
def with draw(self.amount):
if amount>0 and amount<=self._account_balance
self.__account_balance-=account
print(“with draw$()new balance:$()”.format(amount,self.__account.balance.”)
def display_balance(self):
else:
print(“invalid with draw amount or insufficient balance.”)
def display_balance(self):
print(“account balnce for{}(account#{}):${}”.format(
self.__account_holder_name,self.__account_number,
self.__account_balance)}
#creat an instance of the bank account class
Account=bank account(account_number=”123456789”
Account_holder_name=”hari prabu”
Initial_balance=5000.0)