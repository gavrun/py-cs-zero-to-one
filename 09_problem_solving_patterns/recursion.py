# 09_problem_solving_patterns/recursion.py

# Examples of recursion patterns

# 1. Simple linear recursion: factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120

# 2. Tree recursion: Fibonacci
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(6))  # 8

# 3. Tail recursion (not optimized in Python, but illustrative)
def tail_factorial(n, acc=1):
    if n == 0:
        return acc
    return tail_factorial(n - 1, acc * n)

print(tail_factorial(5))  # 120

# 4. Backtracking style recursion (simple subset sum example)
def subset_sum(nums, target, index=0):
    if target == 0:
        return True
    if target < 0 or index == len(nums):
        return False
    # Include nums[index]
    if subset_sum(nums, target - nums[index], index + 1):
        return True
    # Exclude nums[index]
    return subset_sum(nums, target, index + 1)

nums = [3, 34, 4, 12, 5, 2]
target = 9
print(subset_sum(nums, target))  # True (4+5=9)

