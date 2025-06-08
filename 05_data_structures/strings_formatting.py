# 05_data_structures/strings_formatting.py

# f-strings: basic variable interpolation
first_name = "Tom"
text = f"Hello, {first_name}."
print(text)  # Hello, Tom.

name = "Bob"
age = 23
info = f"Name: {name}\t Age: {age}"
print(info)  # Name: Bob   Age: 23

# format(): named arguments
text = "Hello, {first_name}.".format(first_name="Tom")
print(text)  # Hello, Tom.

info = "Name: {name}\t Age: {age}".format(name="Bob", age=23)
print(info)  # Name: Bob   Age: 23

# format(): positional arguments
info = "Name: {0}\t Age: {1}".format("Bob", 23)
print(info)  # Name: Bob   Age: 23

text = "Hello, {0} {0} {0}.".format("Tom")
print(text)  # Hello, Tom Tom Tom.

# Type-specific placeholders
welcome = "Hello {:s}".format("Tom")
print(welcome)  # Hello Tom

source = "{:d} characters"
print(source.format(5))  # 5 characters

# Thousands separator
print("{:,d} characters".format(5000))  # 5,000 characters

# f-strings also support format specifiers
n = 5000
print(f"{n:,d} characters")  # 5,000 characters

# Floating-point precision
number = 23.8589578
print("{:.2f}".format(number))     # 23.86
print("{:.3f}".format(number))     # 23.859
print("{:.4f}".format(number))     # 23.8590
print("{:,.2f}".format(10001.23554))  # 10,001.24

# Minimum field width
print("{:10.2f}".format(23.8589578))  # 23.86
print("{:8d}".format(25))             # 25

# Same with f-strings
n1 = 23.8589578
print(f"{n1:10.2f}")  # 23.86
n2 = 25
print(f"{n2:8d}")     # 25

# Percent formatting
number = 0.12345
print("{:%}".format(number))      # 12.345000%
print("{:.0%}".format(number))    # 12%
print("{:.1%}".format(number))    # 12.3%

print(f"{number:%}")      # 12.345000%
print(f"{number:.0%}")    # 12%
print(f"{number:.1%}")    # 12.3%

# Exponential notation
number = 12345.6789
print("{:e}".format(number))     # 1.234568e+04
print("{:.0e}".format(number))   # 1e+04
print("{:.1e}".format(number))   # 1.2e+04

print(f"{number:e}")     # 1.234568e+04
print(f"{number:.0e}")   # 1e+04
print(f"{number:.1e}")   # 1.2e+04

# Old-style % formatting
info = "Name: %s \t Age: %d" % ("Tom", 35)
print(info)  # Name: Tom     Age: 35

number = 23.8589578
print("%0.2f  - %e" % (number, number))  # 23.86  - 2.385896e+01

# String alignment and truncation
s = "Hello World"
print(f"{s:>16}!")   # right-aligned
print(f"{s:<16}!")   # left-aligned
print(f"{s:^16}!")   # centered
print(f"{s:.16}!")   # truncate to 16 chars
print(f"{s:.5}!")    # truncate to 5 chars
