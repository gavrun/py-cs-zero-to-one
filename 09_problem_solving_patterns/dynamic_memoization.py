# 09_problem_solving_patterns/dynamic_memoization.py

# Dynamic Programming (Top-Down / Memoization)

# This version uses recursion + memoization to avoid redundant work.

def fib_top_down(n, memo=None):
    if memo is None:
        memo = {}

    # If already computed, return from cache
    if n in memo:
        return memo[n]

    # Base cases
    if n <= 1:
        memo[n] = n
        return n

    # Recursive case with memoization
    memo[n] = fib_top_down(n - 1, memo) + fib_top_down(n - 2, memo)
    return memo[n]

n = 35
print("Fibonacci (Top-Down):", fib_top_down(n))

# Time Complexity: O(n)
# Space Complexity: O(n) — due to recursion stack and memo dictionary

