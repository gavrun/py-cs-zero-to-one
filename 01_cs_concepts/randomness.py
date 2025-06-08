# 01_cs_concepts/randomness.py

import random

# Generate a random integer between 1 and 10 inclusive
rand_int = random.randint(1, 10)
print("Random integer:", rand_int)

# Generate a random float in [0.0, 1.0)
rand_float = random.random()
print("Random float:", rand_float)

# Choose a random element from a list
items = ['apple', 'banana', 'cherry']
choice = random.choice(items)
print("Random choice:", choice)

# Shuffle a list in place
random.shuffle(items)
print("Shuffled list:", items)

# Sample k unique elements from a population
sample = random.sample(range(100), 5)
print("Random sample:", sample)

# Seed the random number generator for reproducibility
random.seed(42)
print("Seeded random int:", random.randint(1, 10))
