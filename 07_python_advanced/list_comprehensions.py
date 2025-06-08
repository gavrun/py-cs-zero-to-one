# 07_python_advanced/list_comprehensions.py

# List comprehensions
# Concise syntax for creating new lists from iterables

# [expr for item in iterable]
# [expr for item in iterable if condition]
# [expr1 if cond else expr2 for item in iterable]
# [expr for sublist in nested for item in sublist]
# (expr for ...)   => generator expression


# Basic examples
squares = [x * x for x in range(5)]              # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]      # [0, 2, 4, 6, 8]
words = ["apple", "banana", "cherry"]
lengths = [len(w) for w in words]                # [5, 6, 6]

# Nested loops
pairs = [(x, y) for x in range(2) for y in range(3)]
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]

# Nested conditionals
filtered = [x for x in range(20) if x % 2 == 0 if x > 10]  # [12, 14, 16, 18]
labeled = ["even" if x % 2 == 0 else "odd" for x in range(5)]
# ['even', 'odd', 'even', 'odd', 'even']

# Using functions inside
def double(x):
    return x * 2

doubled = [double(x) for x in range(4)]  # [0, 2, 4, 6]

# Flattening nested lists
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]  # [1, 2, 3, 4, 5, 6]

# 2D matrix generation
rows, cols = 2, 3
grid = [[(r, c) for c in range(cols)] for r in range(rows)]
# [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)]]

# Filtering with multiple conditions
nums = [x for x in range(50) if x % 3 == 0 and x % 5 == 0]  # [0, 15, 30, 45]

# List comprehension with exception handling
raw = ["10", "20", "bad", "30"]
parsed = [int(x) for x in raw if x.isdigit()]  # skips "bad"

# or more safely with try-except inside helper function:
def safe_int(x):
    try:
        return int(x)
    except ValueError:
        return None

cleaned = [safe_int(x) for x in raw if safe_int(x) is not None]  # [10, 20, 30]

# With enumerate() or zip()
indexed = [f"{i}: {v}" for i, v in enumerate(words)]  # ['0: apple', '1: banana', ...]
zipped = [f"{a}-{b}" for a, b in zip(["A", "B"], [1, 2])]  # ['A-1', 'B-2']

# Generator expression (lazy version)
gen = (x * x for x in range(1000000))
print(next(gen))  # 0
print(next(gen))  # 1


