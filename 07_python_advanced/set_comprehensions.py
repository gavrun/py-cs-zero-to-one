# 07_python_advanced/set_comprehensions.py

# Set Comprehensions
# Build sets using concise comprehension syntax

# {expr for item in iterable}
# {expr for item in iterable if condition}
# {f(x) for x in items if valid(x)}
# Nested: {subitem for group in groups for subitem in group}


# Basic example
nums = [1, 2, 2, 3, 4, 4, 5]
unique = {x for x in nums}
# {1, 2, 3, 4, 5}

# With condition
evens = {x for x in range(10) if x % 2 == 0}
# {0, 2, 4, 6, 8}

# Set of characters in a string
chars = {c for c in "hello world"}
# {'h', 'e', 'l', 'o', ' ', 'w', 'r', 'd'}

# From multiple sources with filtering
data = ["a", "bb", "ccc", "dd", "eee", "a"]
lengths = {len(word) for word in data if len(word) >= 2}
# {2, 3}

# Using functions inside
def normalize(word):
    return word.strip().lower()

words = ["  Apple", "banana ", "APPLE", "Banana"]
normalized = {normalize(w) for w in words}
# {'apple', 'banana'}

# From nested loops
coords = {(x, y) for x in range(2) for y in range(2)}
# {(0, 1), (1, 0), (1, 1), (0, 0)}

# Flatten nested sets (deduplicate from 2D)
nested = [{1, 2}, {2, 3}, {4}]
flat = {item for group in nested for item in group}
# {1, 2, 3, 4}

# Exclude unwanted values
dirty = ["apple", "", "banana", None, "apple", " "]
clean = {s.strip() for s in dirty if s and s.strip()}
# {'apple', 'banana'}

# Set of lengths from string values
lengths = {len(w) for w in ["one", "three", "seven", "one"]}
# {3, 5}

# With exception-safe conversion
data = ["10", "bad", "20", "30"]
def safe_int(x):
    try:
        return int(x)
    except ValueError:
        return None

nums = {safe_int(x) for x in data if safe_int(x) is not None}
# {10, 20, 30}

