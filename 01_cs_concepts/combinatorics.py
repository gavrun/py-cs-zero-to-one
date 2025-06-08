# 01_cs_concepts/combinatorics.py

import math

# Permutations: number of ways to arrange n items
n = 5
perm = math.factorial(n)
print(f"Permutations of {n} items:", perm)

# Permutations of k items from n (order matters)
k = 3
perm_k = math.perm(n, k)  # Python 3.8+
print(f"Permutations of {k} items from {n}:", perm_k)

# Combinations: number of ways to choose k items from n (order doesn't matter)
comb = math.comb(n, k)  # Python 3.8+
print(f"Combinations of {k} items from {n}:", comb)

# Manual computation for combinations (n choose k)
def nCr(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

print(f"Manual combinations nCr({n}, {k}):", nCr(n, k))

# Example: list all combinations (using itertools)
from itertools import combinations

items = ['a', 'b', 'c', 'd', 'e']
for combo in combinations(items, 3):
    print(combo)


