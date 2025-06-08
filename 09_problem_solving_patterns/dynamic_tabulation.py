# 09_problem_solving_patterns/dynamic_tabulation.py

# Dynamic Programming (Bottom-Up / Tabulation)

# This version builds the solution iteratively from the ground up.

def fib_bottom_up(n):
    if n <= 1:
        return n

    # Create a table to store Fibonacci values
    dp = [0] * (n + 1)

    # Base cases
    dp[0] = 0
    dp[1] = 1

    # Fill the table from index 2 to n
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

n = 35
print("Fibonacci (Bottom-Up):", fib_bottom_up(n))

# Time Complexity: O(n)
# Space Complexity: O(n) — can be reduced to O(1) with two variables

