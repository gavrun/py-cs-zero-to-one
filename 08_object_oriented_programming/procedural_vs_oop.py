# 08_object_oriented_programming/procedural_vs_oop.py

# Procedural Programming and Object-Oriented Programming (OOP)

# Problem: Represent and manage bank accounts

# 1. Procedural approach

# Data is stored in dictionaries
account_1 = {"owner": "Alice", "balance": 100}
account_2 = {"owner": "Bob", "balance": 200}

# Functions operate on external data structures
def deposit(account, amount):
    account["balance"] += amount

def withdraw(account, amount):
    if amount > account["balance"]:
        print("Insufficient funds")
    else:
        account["balance"] -= amount

# Usage
deposit(account_1, 50)
withdraw(account_1, 30)
print("Procedural:", account_1)


# 2. Object-Oriented approach

# Data and behavior are bundled into a class
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def __str__(self):
        return f"{self.owner}: ${self.balance}"

# Usage
acc1 = BankAccount("Alice", 100)
acc1.deposit(50)
acc1.withdraw(30)
print("OOP:", acc1)
