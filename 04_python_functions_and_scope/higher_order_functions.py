# 04_python_functions_and_scope/higher_order_functions.py

# Higher-Order Functions in Python

# A function is called "higher-order" if it:
# - Takes one or more functions as arguments
# - Returns a function as a result

# Purpose:
# - Reuse logic (abstract over behavior)
# - Compose operations
# - Customize code flow (callbacks, decorators, pipelines)


# 1. Passing functions as arguments

def apply_twice(func, value):
    """
    Apply a function to the value two times.
    """
    return func(func(value))

def increment(x):
    return x + 1

print(apply_twice(increment, 3))  # Output: 5


# 2. Returning a function (custom behavior generator)

def make_multiplier(factor):
    """
    Return a function that multiplies by the given factor.
    """
    def multiply(x):
        return x * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15


# 3. Simple function decorator (adding logging)

def log_call(func):
    """
    Decorator-like function that logs before calling the function.
    """
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}")
        return func(*args, **kwargs)
    return wrapper

def greet(name):
    return f"Hello, {name}"

greet_logged = log_call(greet)
print(greet_logged("Alice"))  # Logs + returns "Hello, Alice"


# 4. Customizable control flow (callback pattern)

def fetch_data(source, on_success, on_error):
    """
    Simulate data fetch with callbacks.
    """
    if source == "valid":
        on_success({"id": 1, "name": "Item"})
    else:
        on_error("404 Not Found")

def handle_success(data):
    print("Data received:", data)

def handle_error(message):
    print("Error:", message)

fetch_data("valid", handle_success, handle_error)
fetch_data("invalid", handle_success, handle_error)


# 5. Functional tools: map, filter, reduce (built-in HOFs)

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))
print("Squares:", squares)  # [1, 4, 9, 16, 25]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Evens:", evens)  # [2, 4]

from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print("Product:", product)  # 120


# Summary:

# Why Higher-Order Functions?
# - Abstract patterns of behavior (apply_twice, make_multiplier)
# - Customize logic via callbacks (e.g. fetch_data)
# - Build modular, reusable code (like decorators)
# - Enable functional-style operations (map, filter, reduce)

# Built-in HOFs in Python:
# - map(func, iterable)
# - filter(func, iterable)
# - sorted(..., key=func)
# - any(), all() with generators
# - functools.reduce
