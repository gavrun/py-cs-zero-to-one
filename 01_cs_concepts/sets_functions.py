# 01_cs_concepts/sets_functions.py

# Functions and their relation to sets

# A function can be viewed as a set of ordered pairs with unique first elements

# Define a function as a dictionary (mapping domain to codomain)
f = {1: 'a', 2: 'b', 3: 'c'}

# Evaluate function
print(f[2])  # 'b'

# Domain and codomain as sets
domain = set(f.keys())
codomain = set(f.values())

print("Domain:", domain)      # {1, 2, 3}
print("Codomain:", codomain)  # {'a', 'b', 'c'}

# Check if function is well-defined (each input maps to exactly one output)
def is_function(mapping):
    return len(mapping) == len(set(mapping.keys()))

print("Is f a function?", is_function(f))  # True

# Compose two functions f and g
f = {1: 2, 2: 3, 3: 4}
g = {2: 'x', 3: 'y', 4: 'z'}

def compose(f, g):
    return {k: g[v] for k, v in f.items() if v in g}

h = compose(f, g)
print("Composition h = g ∘ f:", h)  # {1: 'x', 2: 'y', 3: 'z'}

# Inverse of a function (if it exists)
def inverse(f):
    inv = {}
    for k, v in f.items():
        if v in inv:
            return None  # Not invertible if values repeat
        inv[v] = k
    return inv

f1 = {1: 'a', 2: 'b', 3: 'c'}
print("Inverse of f1:", inverse(f1))  # {'a':1, 'b':2, 'c':3}

f2 = {1: 'a', 2: 'a'}
print("Inverse of f2:", inverse(f2))  # None (not invertible)

