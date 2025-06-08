# 07_python_advanced/standard_library_intro.py

# Python Standard Library overview

# Useful built-in modules

import math
import datetime
import os
import sys
import random
import collections

# Math module
print("Square root of 16:", math.sqrt(16))
print("Pi:", math.pi)

# Datetime module
now = datetime.datetime.now()
print("Current date and time:", now)

# OS module - interacting with the operating system
print("Current working directory:", os.getcwd())

# Sys module - system-specific parameters
print("Python version:", sys.version)

# Random module - random number generation
print("Random integer 1-10:", random.randint(1, 10))

# Collections module - specialized container datatypes
Counter = collections.Counter(['a', 'b', 'a', 'c', 'b', 'a'])
print("Counter example:", Counter)

# Helpful functions from built-ins
print("Sum of 1 to 5:", sum([1, 2, 3, 4, 5]))
print("Minimum:", min(5, 2, 9))
print("Maximum:", max(5, 2, 9))
print("Sorted list:", sorted([3, 1, 4, 1, 5]))

