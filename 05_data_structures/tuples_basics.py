# 05_data_structures/tuples_basics.py


# Creating tuples
point = (3, 4)
empty = ()                # empty tuple
single = (5,)             # tuple with one item (note the comma)

# Accessing elements
print(point[0])           # 3
print(point[1])           # 4

# Tuples are immutable
# point[0] = 10  # TypeError: 'tuple' object does not support item assignment

# Tuple unpacking
x, y = point
print(x + y)              # 7

# Extended unpacking
a, b, *rest = (1, 2, 3, 4, 5)
print(rest)               # [3, 4, 5]

head, *middle, tail = (10, 20, 30, 40)
print(middle)             # [20, 30]

# Using tuples as fixed records
person = ("Alice", 30)
name, age = person
print(f"{name} is {age} years old")

# Tuple return values from functions
def min_max(seq):
    return min(seq), max(seq)

lo, hi = min_max([3, 5, 1, 8])
print(lo, hi)             # 1 8

# Nested tuples
matrix = (
    (1, 2, 3),
    (4, 5, 6)
)
print(matrix[1][2])       # 6

# Tuples as dictionary keys (must be immutable)
location = {(0, 0): "origin", (1, 2): "target"}
print(location[(1, 2)])   # target

# Membership and length
coords = (1, 2, 3)
print(2 in coords)        # True
print(len(coords))        # 3

# Tuple concatenation and repetition
a = (1, 2)
b = (3, 4)
print(a + b)              # (1, 2, 3, 4)
print(a * 2)              # (1, 2, 1, 2)

# Tuples are hashable (if elements are hashable)
s = {(1, 2), (3, 4)}
print((1, 2) in s)        # True

# Tuples support comparison
print((1, 2) < (1, 3))    # True
print((1, 2, 3) == (1, 2, 3))  # True


# Tuple vs list

# Tuples:
# - Immutable
# - Hashable (usable as dict/set keys)
# - Faster to create
# - Represent fixed-size records
