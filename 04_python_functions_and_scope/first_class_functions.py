# 04_python_functions_and_scope\first_class_functions.py

# First-Class Functions in Python

# Functions in Python are first-class objects:
# - They can be assigned to variables
# - Passed as arguments
# - Returned from other functions
# - Stored in data structures (like lists, dicts)


# 1. Assigning a function to a variable

def say_hello():
    print("Hello!")

def say_goodbye():
    print("Goodbye!")

# Assign function to a variable
message = say_hello
message()  # Output: Hello!

message = say_goodbye
message()  # Output: Goodbye!


# 2. Passing a function as an argument (Higher-Order)

def operate(a, b, operation):
    result = operation(a, b)
    print("Result:", result)

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

operate(5, 3, add)       # Output: Result: 8
operate(5, 3, multiply)  # Output: Result: 15


# 3. Returning a function from another function

def select_operation(name):
    def add(a, b):
        return a + b
    def subtract(a, b):
        return a - b
    def multiply(a, b):
        return a * b

    if name == "add":
        return add
    elif name == "subtract":
        return subtract
    else:
        return multiply

op = select_operation("add")
print(op(10, 5))  # Output: 15

op = select_operation("subtract")
print(op(10, 5))  # Output: 5


# 4. Functions inside data structures

def square(x):
    return x * x

def cube(x):
    return x * x * x

functions = [square, cube]

for f in functions:
    print(f(3))  # Output: 9, then 27


# 5. Closures: returned function remembers outer variable

def make_power_function(exponent):
    def power(base):
        return base ** exponent  # captures 'exponent'
    return power

square = make_power_function(2)
cube = make_power_function(3)

print(square(4))  # Output: 16
print(cube(2))    # Output: 8


# 6. Lambdas as first-class functions

double = lambda x: x * 2
print(double(10))  # Output: 20

# Can pass lambdas as arguments too
operate(10, 3, lambda a, b: a ** b)  # Output: Result: 1000


# Summary:
# - Python treats functions like any other object
# - This enables powerful patterns like higher-order functions and closures
# - Common use cases: callbacks, decorators, factory functions
