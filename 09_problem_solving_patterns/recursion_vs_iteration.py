# 09_problem_solving_patterns/recursion_vs_iteration.py

# Comparing recursion vs iteration

# Pattern: Summing elements in a list

# 1. Recursion: sum of list elements
def sum_recursive(arr, index=0):
    if index == len(arr):
        return 0
    return arr[index] + sum_recursive(arr, index + 1)

# 2. Iteration: sum using a loop
def sum_iterative(arr):
    total = 0
    for num in arr:
        total += num
    return total

# Test data
numbers = [3, 1, 4, 1, 5]

# Running both
print("Recursive sum:", sum_recursive(numbers))  # 14
print("Iterative sum:", sum_iterative(numbers))  # 14


# Pattern: Factorial

# Factorial using recursion
def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

# Factorial using iteration
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial_recursive(5))  # 120
print(factorial_iterative(5))  # 120


# Use recursion for problems naturally defined recursively (e.g. trees)

# Use iteration when efficiency and stack safety are important
