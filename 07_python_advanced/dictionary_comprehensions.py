# 07_python_advanced/dictionary_comprehensions.py

# Dictionary Comprehensions
# Build dictionaries from iterables using concise syntax

# {k_expr: v_expr for item in iterable}
# {k: v for k, v in dict.items() if condition}
# {k: v1 if cond else v2 for k, v in dict.items()}
# Nested: {k1: {k2: val for ...} for ...}


# Basic examples
words = ["apple", "banana", "cherry"]
lengths = {word: len(word) for word in words}
# {'apple': 5, 'banana': 6, 'cherry': 6}

# With enumerate()
indexed = {i: word for i, word in enumerate(words)}
# {0: 'apple', 1: 'banana', 2: 'cherry'}

# With zip()
keys = ["name", "age", "country"]
values = ["Alice", 30, "USA"]
person = {k: v for k, v in zip(keys, values)}
# {'name': 'Alice', 'age': 30, 'country': 'USA'}

# With condition (filter)
scores = {"Alice": 85, "Bob": 72, "Carol": 90}
passed = {k: v for k, v in scores.items() if v >= 80}
# {'Alice': 85, 'Carol': 90}

# With conditional expression (ternary)
status = {name: ("pass" if score >= 80 else "fail")
          for name, score in scores.items()}
# {'Alice': 'pass', 'Bob': 'fail', 'Carol': 'pass'}

# Reversing a dictionary
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b', 3: 'c'}

# Nested comprehension
matrix = {
    row: {col: row * col for col in range(1, 4)}
    for row in range(1, 4)
}
# {
#   1: {1: 1, 2: 2, 3: 3},
#   2: {1: 2, 2: 4, 3: 6},
#   3: {1: 3, 2: 6, 3: 9}
# }

# Flattening a nested dict
flat = {(r, c): val
        for r, row in matrix.items()
        for c, val in row.items()}
# {(1, 1): 1, (1, 2): 2, ...}

# Transforming values
raw_prices = {"pen": "$1.20", "pencil": "$0.80", "notebook": "$2.50"}
clean_prices = {k: float(v.strip("$")) for k, v in raw_prices.items()}
# {'pen': 1.2, 'pencil': 0.8, 'notebook': 2.5}

# Filtering invalid keys or values
dirty_data = {"x": "10", "y": "bad", "z": "30"}
parsed = {k: int(v) for k, v in dirty_data.items() if v.isdigit()}
# {'x': 10, 'z': 30}

# Safe transformation using try-except helper
def safe_int(val):
    try:
        return int(val)
    except ValueError:
        return None

parsed_safe = {k: safe_int(v) for k, v in dirty_data.items()
               if safe_int(v) is not None}
# {'x': 10, 'z': 30}

# Working with nested keys
people = {
    "alice": {"age": 30},
    "bob": {"age": 25}
}
ages = {name: data["age"] for name, data in people.items()}
# {'alice': 30, 'bob': 25}

