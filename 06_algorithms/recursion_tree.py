# 06_algorithms/recursion_tree.py

# Example of recursion tree: Fibonacci sequence naive recursion

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(6))  # 8

# Visualization note:
# fib(6)
# ├─ fib(5)
# │  ├─ fib(4)
# │  └─ fib(3)
# └─ fib(4)
#    ├─ fib(3)
#    └─ fib(2)

# This recursive call tree grows exponentially with n,
# demonstrating redundant calculations.

