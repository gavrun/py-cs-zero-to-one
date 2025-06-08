# 04_python_functions_and_scope/return_values.py

# Return a single value
def double(x):
    return x * 2

result = double(4)
print(result)  # 8

# Return multiple values (as a tuple)
def get_min_max(numbers):
    return min(numbers), max(numbers)

low, high = get_min_max([3, 1, 9, 5])
print(low, high)  # 1 9

# Return early
def safe_divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print(safe_divide(10, 2))  # 5.0
print(safe_divide(5, 0))   # error message

# A function without return returns None by default
def do_nothing():
    pass

print(do_nothing())  # None
