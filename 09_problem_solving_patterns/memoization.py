# 09_problem_solving_patterns/memoization.py

# Memoization: cache results of expensive function calls

# Fibonacci without memoization (slow)
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

# Fibonacci with memoization
memo = {}
def fib_memo(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]

print(fib_memo(40))  # Fast

# Using functools.lru_cache (built-in memoization)
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_cached(n):
    if n <= 1:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)

print(fib_cached(40))  # Fast

