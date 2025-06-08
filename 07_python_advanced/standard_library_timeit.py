# 07_python_advanced/stdlib/standard_library_timeit.py

# Python 'timeit' module
# For measuring execution time of small code snippets accurately

import timeit

# Simple example: using timeit.timeit()

# Measure how long it takes to sum numbers 1 to 1000
duration = timeit.timeit("sum(range(1000))", number=1000)
print("sum(range(1000)) x1000:", duration, "seconds")

# Using setup parameter
stmt = "total = math.sqrt(100)"
setup = "import math"
duration = timeit.timeit(stmt, setup=setup, number=100000)
print("math.sqrt(100) x100000:", duration)

# Compare performance of two approaches
# String concatenation vs join

concat = "'-'.join(str(x) for x in range(100))"
plus = "s = ''; [s := s + str(x) + '-' for x in range(100)]"

t1 = timeit.timeit(concat, number=1000)
t2 = timeit.timeit(plus, number=1000)

print("join:", t1)
print("+:  ", t2)

# Using timeit.Timer object
timer = timeit.Timer("math.factorial(100)", setup="import math")
print("factorial(100):", timer.timeit(number=10000))

# Measuring function calls directly
def slow():
    sum(x**2 for x in range(1000))

duration = timeit.timeit(slow, number=1000)
print("slow() x1000:", duration)

# Command line usage
# python -m timeit "sum(range(100))"
# python -m timeit -s "import math" "math.sqrt(2)"

# Best practices
# - Run with high enough number of iterations (e.g., number=100000)
# - Use setup to import modules or define variables
# - Avoid I/O in timed code
# - Use timeit inside functions or scripts — don't benchmark at module level

# Summary
# timeit.timeit(stmt, setup, number)         → total seconds
# timeit.Timer(stmt, setup).timeit(number)   → Timer object
# timeit.repeat(...)                         → list of multiple timings
# python -m timeit                           → command line benchmarking
