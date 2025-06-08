# 06_algorithms/counting_items.py

# Count how many times each item appears in a list

def count_items(lst):
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

# Example usage
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
result = count_items(words)
print(result)  # {'apple': 3, 'banana': 2, 'cherry': 1}

# Using collections.Counter (built-in)
from collections import Counter
counts = Counter(words)
print(counts)  # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
