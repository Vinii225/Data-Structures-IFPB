# Exercise: CurrentAccount class with deposit, withdraw, and balance operations, and interactive menu.

class CurrentAccount:
    def __init__(self, number, balance, name):
        self.__number=number
        self.__balance=balance
        self.__name=name
    
    def depositInBalance(self, balance):
        self.__balance+=balance
        
    def retireInBalance(self, balance):
        if self.__balance>=balance:
            self.__balance-=balance
            return True
        else:
            return False
        
    def getNumber(self):
        return self.__number
    
    def getBalance(self):
        return self.__balance
    
    def getName(self):
        return self.__name
     
    def __str__(self):
        return f"Account: {self.getNumber()} - Holder: {self.getName()} - Balance: {self.getBalance()}"
    
quantity = int(input("Enter the number of accounts to create: "))
accounts = []

for i in range(quantity):
    print(f"\nAccount {i+1}")
    number = int(input("Enter account number: "))
    balance = float(input("Enter account balance: "))
    name = str(input("Enter account holder name: "))
    account = CurrentAccount(number, balance, name)
    accounts.append(account)
    
def findAccount(number):
    for account in accounts:
        if account.getNumber() == number:
            return account
    else:
        return False
            
while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Balance")
    print("4. Exit")
    answer = int(input("Enter command number: "))
    
    if answer == 4:
        print("Exiting..")
        break
    if answer < 1 or answer > 4:
        print("Invalid command")
        
    account_number = int(input("Enter account number: "))
    account = findAccount(account_number)
    if account == False:
        print("Account not found...")
    else:
        if answer == 1:
            balance = float(input("Enter deposit amount: "))
            account.depositInBalance(balance)
        elif answer == 2:
            balance = float(input("Enter withdrawal amount: "))
            account.retireInBalance(balance)
        elif answer == 3:
            print(f"Balance: {account.getBalance()}")
            
for i in range(len(accounts)):
    print(accounts[i])