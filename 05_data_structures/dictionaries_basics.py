# 05_data_structures/dictionaries_basics.py


# Creating dictionaries
person = {"name": "Alice", "age": 30}
empty = {}

# Accessing values
print(person["name"])           # Alice
# print(person["job"])          # KeyError if key doesn't exist
print(person.get("job"))        # None
print(person.get("job", "N/A")) # N/A (default fallback)

# Adding and updating entries
person["job"] = "Engineer"      # Add new
person["age"] = 31              # Update existing

# Removing keys
del person["job"]               # Removes key
# person.pop("job")            # Alternative (raises if not found unless default given)

# Safe pop with default
removed = person.pop("job", "not found")
print(removed)                  # "not found"

# Checking for keys
if "age" in person:
    print("Age is known")

# Looping
for key in person:
    print(key, person[key])         # key access

for key, value in person.items():
    print(key, value)               # key-value pairs

for value in person.values():
    print(value)

# Dictionary length
print(len(person))

# Merge dictionaries
extra = {"city": "Paris"}
person.update(extra)
# {'name': 'Alice', 'age': 31, 'city': 'Paris'}

# Using setdefault()
# Assigns default only if key is missing
person.setdefault("email", "unknown@example.com")

# Dictionary comprehension
squares = {x: x*x for x in range(5)}   # {0: 0, 1: 1, ..., 4: 16}

# Creating from lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
combined = dict(zip(keys, values))     # {'a': 1, 'b': 2, 'c': 3}

# Nested dictionaries
users = {
    "alice": {"age": 30, "job": "dev"},
    "bob": {"age": 25, "job": "analyst"}
}
print(users["alice"]["job"])           # dev

# Using tuples as keys
points = {(0, 0): "origin", (1, 2): "A"}
print(points[(1, 2)])                  # A

# Transforming values
data = {"a": "10", "b": "20", "c": "x"}
parsed = {k: int(v) for k, v in data.items() if v.isdigit()}
# {'a': 10, 'b': 20}

# Key methods

# d[key] = value        → add or update
# d.get(key, default)   → safe access
# d.pop(key, default)   → remove and return
# d.setdefault(key, val)→ insert if missing
# d.update(other_dict)  → merge/update
# d.items()             → (key, value) pairs
# d.keys() / d.values() → views
# dict(zip(keys, values)) → from two lists

# Common use-cases
# - Mapping identifiers to values
# - Nested structured data
# - Lookups, counters, grouping, indexing

