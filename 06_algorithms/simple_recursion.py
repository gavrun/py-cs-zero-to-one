# 06_algorithms/simple_recursion.py

# Recursion: function calling itself

# Countdown example
def countdown(n):
    if n <= 0:
        print("Done")
    else:
        print(n)
        countdown(n - 1)

countdown(5)

# Factorial example
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120

# Recursion must have a base case to stop

