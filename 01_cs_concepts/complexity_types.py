# 01_cs_concepts/complexity_types.py

# Complexity types in algorithms

# Time complexity: how runtime grows with input size (n)
# Space complexity: how memory usage grows with input size

# Common time complexity classes:

# O(1)       - constant time
# O(log n)   - logarithmic time (e.g. binary search)
# O(n)       - linear time (e.g. simple loop)
# O(n log n) - linearithmic time (e.g. merge sort)
# O(n^2)     - quadratic time (e.g. bubble sort)
# O(2^n)     - exponential time (e.g. naive recursion)
# O(n!)      - factorial time (e.g. permutations)


# Example: linear vs quadratic time

def linear_search(arr, target):
    for i in arr:
        if i == target:
            return True
    return False

def quadratic_example(arr):
    count = 0
    for i in arr:
        for j in arr:
            count += 1
    return count

arr = list(range(1000))

print("Linear search found:", linear_search(arr, 999))
print("Quadratic example count:", quadratic_example(arr))


# Space complexity examples

def create_list(n):
    return [0] * n  # O(n) space

def constant_space(n):
    total = 0
    for i in range(n):
        total += i
    return total  # O(1) space

print(create_list(10))
print(constant_space(10))

