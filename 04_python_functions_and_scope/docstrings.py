# 04_python_functions_and_scope/docstrings.py

# Docstring: string used to document a function (or module/class)

def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

print(greet("Alice"))

# Accessing a function's docstring
print(greet.__doc__)

# Multiline docstring with explanation and example
def multiply(a, b):
    """
    Multiply two numbers and return the result.

    Args:
        a (int or float): First number.
        b (int or float): Second number.

    Returns:
        int or float: Product of a and b.

    Example:
        multiply(2, 3) -> 6
    """
    return a * b

print(multiply(2, 3))
print(multiply.__doc__)
