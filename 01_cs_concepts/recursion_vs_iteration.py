# 01_cs_concepts/recursion_vs_iteration.py

# Recursion vs Iteration

# Recursion is elegant for some problems but may cause stack overflow
# Iteration is generally more memory efficient

# Recursive Fibonacci
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# Iterative Fibonacci
def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(fib_recursive(10))  # 55
print(fib_iterative(10))  # 55

# Recursive factorial
def fact_recursive(n):
    if n == 0:
        return 1
    return n * fact_recursive(n-1)

# Iterative factorial
def fact_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(fact_recursive(5))  # 120
print(fact_iterative(5))  # 120

