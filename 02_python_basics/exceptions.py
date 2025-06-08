# 02_python_basics/exceptions.py


# Level 1: Basic Try/Except

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("That was not a valid number!")


# Level 2: Catching Specific Exceptions

try:
    result = 10 / int(input("Enter a divisor: "))
    print("Result is:", result)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("That wasn't a valid number.")


# Level 3: Using else and finally

try:
    f = open("data.txt")
except FileNotFoundError:
    print("File not found!")
else:
    print("File opened successfully!")
    f.close()
finally:
    print("This runs no matter what.")


# Level 4: Raising Your Own Exceptions

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except ValueError as e:
    print("Error:", e)


# Level 5: Custom Exception Classes

class NegativeAgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise NegativeAgeError("Age cannot be negative")

try:
    set_age(-5)
except NegativeAgeError as e:
    print("Custom error:", e)


