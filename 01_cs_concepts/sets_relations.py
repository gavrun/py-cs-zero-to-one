# 01_cs_concepts/sets_relations.py

# Sets and relations 

# Define sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Set operations
print("Union:", A | B)                 # {1, 2, 3, 4, 5, 6}
print("Intersection:", A & B)          # {3, 4}
print("Difference A - B:", A - B)      # {1, 2}
print("Difference B - A:", B - A)      # {5, 6}
print("Symmetric difference:", A ^ B)  # {1, 2, 5, 6}

# Subset and superset
print("A subset of B?", A <= B)    # False
print("B superset of A?", B >= A)  # False

# Relations: represented as sets of ordered pairs
R = {(1, 2), (2, 3), (3, 4)}
print("Relation R:", R)

# Check if relation contains a pair
print("(2,3) in R?", (2, 3) in R)

# Domain and range extraction
domain = {x for (x, y) in R}
range_ = {y for (x, y) in R}
print("Domain:", domain)  # {1, 2, 3}
print("Range:", range_)   # {2, 3, 4}

# Relation properties (example: reflexive)
def is_reflexive(rel, elements):
    return all((e, e) in rel for e in elements)

elements = {1, 2, 3, 4}
print("Is R reflexive?", is_reflexive(R, elements))  # False

