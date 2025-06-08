# 07_python_advanced/generators_vs_functions.py

# Normal function: runs all code at once, returns single value

def normal_func():
    i = 1
    print("First")
    print(i)
    i += 1

    print("Second")
    print(i)
    i += 1

    print("Third")
    print(i)
    i += 1

    return i

result = normal_func()
print("Returned:", result)


# Generator function: yields values, pauses and resumes on iteration

def generator_func():
    i = 1
    print("First")
    yield i

    print("Second")
    i += 1
    yield i

    print("Third")
    i += 1
    yield i

for value in generator_func():
    print("Yielded:", value)


# Memory comparison example

import sys

list_comp = [i * 2 for i in range(10000)]
gen_expr = (i * 2 for i in range(10000))

print("List comprehension size:", sys.getsizeof(list_comp))  # Large
print("Generator expression size:", sys.getsizeof(gen_expr)) # Small

