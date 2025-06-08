# 02_python_basics/numbers_and_types.py

# Numeric Types

# Integer (whole number)
a = 5

# Float (decimal number)
b = 3.14

# Complex number (real + imaginary)
c = 2 + 3j       # complex

# Boolean (True or False)
flag = True      # bool is a subtype of int (True == 1, False == 0)


# Basic Arithmetic Operations

add = a + b          # addition → 8.14
sub = a - b          # subtraction → 1.86
mul = a * b          # multiplication → 15.7
div = a / b          # true division → 1.592...
floordiv = a // 2    # integer division → 2
mod = a % 2          # modulo (remainder) → 1
exp = a ** 2         # exponentiation → 25

# Built-in math functions
print("abs(-7):", abs(-7))             # 7
print("round(3.75):", round(3.75))     # 4
print("pow(2, 10):", pow(2, 10))       # 1024


# Type Checking

print(type(a))     # <class 'int'>
print(type(b))     # <class 'float'>
print(type(c))     # <class 'complex'>
print(type(flag))  # <class 'bool'>

# isinstance is preferred over type(...) == ...
print(isinstance(b, float))  # True
print(isinstance(flag, int)) # True (bool is subclass of int)


# Tips:
# - Use `//` if you want integer results
# - Always validate user input before converting to number

