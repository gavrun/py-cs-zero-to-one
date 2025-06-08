# 09_problem_solving_patterns/programming_vs_dynamic_programming.py

# Illustrating difference between simple recursion and dynamic programming on Fibonacci example 

# Fibonacci with simple recursion (exponential time)
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# Fibonacci with dynamic programming (memoization)
def fib_dp(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
        return n
    memo[n] = fib_dp(n-1, memo) + fib_dp(n-2, memo)
    return memo[n]

n = 35
print("Fib recursive:", fib_recursive(n))  # Slow for large n
print("Fib DP:", fib_dp(n))                # Fast with memoization


# PROBLEM:

# You are standing at the bottom of a staircase with N steps.
# You can climb 1 or 2 steps at a time.
# How many different ways can you reach the top?


# 1. Simple recursive solution (no memory)

def ways_simple(n):
    if n < 0:
        return 0
    if n == 0:
        return 1  # One way: do nothing
    return ways_simple(n - 1) + ways_simple(n - 2)


# 2. Smarter solution with memory (dynamic programming)

def ways_dp(n):
    # We remember results we've already calculated
    memo = [0] * (n + 1)

    # Base cases
    memo[0] = 1  # 1 way to stand still
    if n >= 1:
        memo[1] = 1  # 1 way to climb one step

    # Fill the rest
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]

    return memo[n]


# Let's test both

n = 10
print("Ways (simple recursion):", ways_simple(n))  # Very slow for big n
print("Ways (with memory):", ways_dp(n))           # Fast


