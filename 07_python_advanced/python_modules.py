# 07_python_advanced/python_modules.py

# Creating and using Python modules

# Suppose this is module 'mymodule.py':
# def greet(name):
#     return f"Hello, {name}!"

# Usage example:
import math
import sys

# Using standard modules
print("Square root of 16:", math.sqrt(16))
print("Python version:", sys.version)

# Importing user-defined module example
# (Save the following as mymodule.py in the same directory)
#
# def greet(name):
#     return f"Hello, {name}!"
#
# Then in this file:
# import mymodule
# print(mymodule.greet("Alice"))

# You can also import specific functions
# from mymodule import greet
# print(greet("Bob"))

# Module search path
import sys
print("Module search paths:", sys.path)

# Reloading a module (useful during development)
# import importlib
# importlib.reload(mymodule)

