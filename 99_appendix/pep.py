# 99_appendix/pep.py

# Python Enhancement Proposals (PEPs)

# Essential PEPs for beginner to intermediate Python developers, 
# along with real code examples and in-line commentary.


# PEP 8 — Style Guide for Python Code

# Indentation: Use 4 spaces per level
def greet(name):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, stranger!")

# Variable and function names: lowercase_with_underscores
def calculate_area(radius):
    return 3.14 * radius * radius

# Class names: CapWords convention
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0

# Constants: ALL_CAPS_WITH_UNDERSCORES
DEFAULT_INTEREST_RATE = 0.05

# Avoid extraneous whitespace:
x = 1  # Good
y = 2

# Bad: x             = 1
# Bad: y=2

# Line length: recommended limit is 79 characters
long_text = (
    "This is a long string that should be split across multiple lines "
    "to maintain readability and follow PEP 8's line length guidelines."
)

# Use blank lines to separate logical sections
def deposit(account, amount):
    account.balance += amount

def withdraw(account, amount):
    if amount > account.balance:
        raise ValueError("Insufficient funds")
    account.balance -= amount


# PEP 20 — The Zen of Python

# The Zen of Python: guiding principles of good code design
import this

# Example principles:
# - Beautiful is better than ugly
# - Simple is better than complex
# - Readability counts

# Zen principles favor clean, readable, and explicit code.


# PEP 257 — Docstring Conventions

def multiply(a, b):
    """
    Multiply two integers and return the result.

    Parameters:
        a (int): First operand
        b (int): Second operand

    Returns:
        int: Product of a and b
    """
    return a * b

class Greeter:
    """
    Greeter class to demonstrate class-level and method-level docstrings.
    """

    def __init__(self, name):
        """
        Initialize with a name.

        Args:
            name (str): The name to use in greetings
        """
        self.name = name

    def greet(self):
        """
        Print a personalized greeting message.
        """
        print(f"Hi, {self.name}!")


# PEP 484 — Type Hints and Static Typing

# Adding type hints to function signatures
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

# Variable annotation
age: int = 30
name: str = "Alice"


# PEP 572 — Assignment Expressions (Walrus Operator)

# Introduced in Python 3.8: allows assignment inside expressions
numbers = [1, 2, 3, 4, 5]

if (n := len(numbers)) > 3:
    print(f"The list has {n} elements")


# PEP 604 — Union Types with `|`

# Python 3.10+: use `|` instead of Union[]
def square(x: int | float) -> int | float:
    return x * x


# PEP 701 — f-string Improvements (Python 3.12+)

# Multiline and embedded expressions in f-strings
value = 10
message = f"""
Result:
---------
Value squared is: {value ** 2}
"""
print(message)


# Why Follow PEPs?

# - Your code becomes more readable and maintainable
# - It matches the expectations of other Python developers
# - Many tools (e.g., flake8, black, mypy) automatically enforce or validate PEPs
# - Adhering to conventions avoids bikeshedding and team inconsistency

# Static checker for style (PEP 8):
# > pip install flake8
# > flake8 your_script.py

# Formatter that enforces style:
# > pip install black
# > black your_script.py

# Type checker for PEP 484:
# > pip install mypy
# > mypy your_script.py

# Official PEP index:
# https://www.python.org/dev/peps/

