# 06_algorithms/fibonacci_recursive_vs_iterative.py

# Recursive Fibonacci (inefficient for large n)
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

print(fib_recursive(5))  # 5

# Iterative Fibonacci (efficient)
def fib_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print(fib_iterative(5))  # 5

# Compare performance for larger values
# print(fib_recursive(35))  # slow
# print(fib_iterative(35))  # fast
