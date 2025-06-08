# 01_cs_concepts/big_o_notation.py

# Big O Notation

# Big O describes how the time or space complexity of an algorithm scales with input size `n`.


# Time Complexities

# O(1) – Constant time  
#  Example: accessing an element by index in a list

# O(log n) – Logarithmic time  
#  Example: binary search

# O(n) – Linear time  
#  Example: traversing a list

# O(n log n) – Linearithmic time  
#  Example: efficient sorts like merge sort, quicksort (average)

# O(n²) – Quadratic time  
#  Example: nested loops over the same list (e.g., bubble sort)

# O(2ⁿ) – Exponential time  
#  Example: recursive Fibonacci without memoization

# O(n!) – Factorial time  
#  Example: generating all permutations


# Rule of Thumb

# Favor O(1), O(log n), or O(n)
# Avoid O(n²), O(2ⁿ), and worse for large input sizes

# Drop Constants and Lower Order Terms

# O(3n + 5) → O(n)
# O(n² + n) → O(n²)


# Space Complexity

# Big O also applies to memory usage. 
# E.g., a function that builds a list of size `n` uses O(n) space.


# Use Big O to analyze performance and guide your algorithm and data structure choices.

