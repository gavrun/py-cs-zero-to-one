# 06_algorithms/recursion_tail.py

# Tail recursion example: factorial using tail recursion

def factorial_tail(n, accumulator=1):
    if n == 0:
        return accumulator
    return factorial_tail(n - 1, accumulator * n)

print(factorial_tail(5))  # 120

# Note: Python does not optimize tail recursion,
# so deep recursion may lead to stack overflow.

