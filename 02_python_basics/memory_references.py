# 02_python_basics/memory_basics.py

# Basic concepts of using memory in Python


# Variables are labels pointing to memory addresses (references)

# Variables store references to objects
a = [1, 2, 3]
b = a  # b references the same list as a

# Modifying via one reference affects the shared object
b.append(4)
print(a)  # [1, 2, 3, 4] — both 'a' and 'b' point to the same list
print(b)  # [1, 2, 3, 4]


# To copy a list and create a new object in memory
c = a.copy()
c.append(5)
print(a)  # [1, 2, 3, 4]
print(c)  # [1, 2, 3, 4, 5]

# Shallow copy creates a new container but not deep sub-objects
import copy
d = copy.copy(a)
d.append(5)
print(a)  # [1, 2, 3, 4]
print(d)  # [1, 2, 3, 4, 5]


# Immutable objects: ints, strings, tuples are stored differently
x = 10
y = x
y += 1
print(x)  # 10 — original 'x' unchanged
print(y)  # 11 — new int object created for 'y'

# Understanding mutable vs immutable objects helps avoid bugs


# id() shows the memory address of the object reference
print(id(a))  # same as id(b)
print(id(b))
print(id(c))  # different from 'a' and 'b'


# Python uses reference counting and garbage collection for memory management
import sys

print(sys.getrefcount(a))  # Number of references to object 'a'

# Python cleans up unused objects with garbage collection

