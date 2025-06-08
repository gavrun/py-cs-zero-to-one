# 07_python_advanced/standard_library_random.py

# Python 'random' module
# For generating pseudo-random numbers

import random

# Random float between 0.0 and 1.0
print("random():", random.random())  # e.g., 0.374

# Random float in range
print("uniform(1.5, 6.5):", random.uniform(1.5, 6.5))  # e.g., 4.21

# Random integer in range (inclusive)
print("randint(1, 10):", random.randint(1, 10))  # e.g., 7

# Random integer in range with step (like range)
print("randrange(0, 100, 5):", random.randrange(0, 100, 5))  # e.g., 55

# Random choice from sequence
choices = ["apple", "banana", "cherry"]
print("choice:", random.choice(choices))  # e.g., 'banana'

# Random sample of N unique elements (without replacement)
print("sample:", random.sample(range(10), 4))  # e.g., [2, 7, 1, 9]

# Random choices with replacement and optional weights
print("choices:", random.choices(choices, k=5))  # e.g., ['banana', 'banana', ...]
print("weighted choices:", random.choices(choices, weights=[10, 1, 1], k=5))

# Shuffle a list in place
data = [1, 2, 3, 4, 5]
random.shuffle(data)
print("shuffled:", data)

# Set random seed for reproducibility
random.seed(42)
print("Seeded random():", random.random())

# Using Random object explicitly
rng = random.Random(123)
print("rng.random():", rng.random())          # consistent across runs
print("rng.randint(1, 5):", rng.randint(1, 5))  # deterministic


# random()              → float [0.0, 1.0)
# uniform(a, b)         → float [a, b]
# randint(a, b)         → int [a, b]
# randrange(start, stop[, step]) → like range, but random
# choice(seq)           → random element
# choices(seq, k=N)     → random elements (with replacement)
# sample(seq, k)        → unique elements (no replacement)
# shuffle(seq)          → in-place shuffling
# seed(n)               → set seed for deterministic output
# Random()              → create independent generator
