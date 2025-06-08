# 07_python_advanced/python_packages.py

# Basic structure of a Python package

# Suppose you have this folder structure:
# mypackage/
#   __init__.py
#   module1.py
#   module2.py

# Contents of module1.py:
# def func1():
#     return "Function 1"

# Contents of module2.py:
# def func2():
#     return "Function 2"

# Contents of __init__.py:
# from .module1 import func1
# from .module2 import func2

# Usage after installing or adding mypackage to PYTHONPATH:
# import mypackage
# print(mypackage.func1())
# print(mypackage.func2())

# You can also import specific functions:
# from mypackage import func1
# print(func1())

# Note:
# - __init__.py makes the directory a package
# - Use relative imports inside package modules

