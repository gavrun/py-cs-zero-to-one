# 05_data_structures/sets_basics.py


# Creating sets
colors = {"red", "green", "blue"}        # Unordered, unique elements
empty = set()                            # Do NOT use {} — that's a dict

# Adding elements
colors.add("yellow")

# Removing elements
colors.remove("red")         # Raises KeyError if not found
colors.discard("purple")     # Safe — no error if not present
removed = colors.pop()       # Removes arbitrary element
colors.clear()               # Remove all items

# Membership check
print("blue" in colors)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)      # union → {1, 2, 3, 4, 5}
print(a & b)      # intersection → {3}
print(a - b)      # difference → {1, 2}
print(a ^ b)      # symmetric difference → {1, 2, 4, 5}

# In-place set updates
a |= {4, 5}       # union update
a &= {2, 4}       # intersection update
a -= {2}          # difference update
a ^= {1, 4}       # symmetric difference update

# Comparisons
print({1, 2} < {1, 2, 3})     # True (proper subset)
print({1, 2, 3} > {1, 2})     # True (proper superset)
print({1, 2} <= {1, 2})       # True (subset or equal)
print({1, 2} == {2, 1})       # True (order doesn't matter)

# Iterating
colors = {"red", "green", "blue"}
for color in colors:
    print(color)

# Set comprehension
squares = {x * x for x in range(6)}        # {0, 1, 4, 9, 16, 25}
evens = {x for x in range(10) if x % 2 == 0}

# Copying sets
s1 = {1, 2, 3}
s2 = s1.copy()
print(s1 is s2)         # False (new object)

# Frozen sets
# Immutable and hashable set variant
fs = frozenset([1, 2, 3])
# fs.add(4)  # AttributeError

frozen_ops = fs | {3, 4}  # still supports set operations

# Use cases
# - Removing duplicates from iterable: set(items)
# - Membership testing: fast O(1) lookups
# - Computing intersections/differences between datasets
# - Representing unordered unique collections

# Safe remove pattern
def safe_remove(s, item):
    if item in s:
        s.remove(item)

# Key methods

# s.add(x)               → add element
# s.remove(x)            → remove or KeyError
# s.discard(x)           → remove if exists, do nothing otherwise
# s.pop()                → remove arbitrary element
# s.clear()              → remove all
# s.copy()               → shallow copy
# s.update(iterable)     → add multiple
# s.union(other)         → s | other
# s.intersection(other)  → s & other
# s.difference(other)    → s - other
# s.symmetric_difference(other) → s ^ other
