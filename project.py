# Banking App
# Class Based Bank
# Withdrawl and Deposit
# Write the transaction to a python file
# while True:
# input
# classes
# open()
# methods
# properties

class Bank:
    balance = 0

    def __init__(self, initial_amount=0):
        self.balance = initial_amount
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        self.write_transaction("Deposit", amount)

    def withdrawl(self, amount):
        self.balance = self.balance - amount
        self.write_transaction("Withdrawl", amount)

    def account_balance(self):
        return self.balance
    
    def write_transaction(self, type, amount):
        with open('bank_transaction.txt', 'a') as file:
            file.write(f"{type}:/t/t{amount}:/t{self.balance}/n")

account = Bank(0)

while True:
    print(f"Balance = {account.account_balance()}")
    print("")
    action = input("What do you want to do? ((W)ithdrawl/(D)eposit/(Q)uit) ")
    action = action.lower()
    if action == "q":
        break
    if action not in ["w", "d"]:
        print("You must choose W/D/Q")
    else:
        amount = input("What is the amount of the transaction? ")
        try:
            amount = float(amount)
        except ValueError:
            amount = 0.0
        
        if action == "w":
            account.withdrawl(amount)
        elif action == "d":
            account.deposit(amount)

