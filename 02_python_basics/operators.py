# 02_python_basics/operators.py

# Arithmetic operators
a = 10
b = 3

add = a + b       # 13
sub = a - b       # 7
mul = a * b       # 30
div = a / b       # 3.333...
floordiv = a // b # 3
mod = a % b       # 1
exp = a ** b      # 1000

# Comparison operators (return bool)
print(a == b)   # False
print(a != b)   # True
print(a > b)    # True
print(a < b)    # False
print(a >= b)   # True
print(a <= b)   # False

# Logical operators
x = True
y = False

print(x and y)  # False
print(x or y)   # True
print(not x)    # False

# String and list operators
print("py" + "thon")  # "python"
print([1, 2] + [3])   # [1, 2, 3]
print("a" * 3)        # "aaa"
print([0] * 4)        # [0, 0, 0, 0]
