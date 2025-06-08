# 03_python_control_structures/if_else.py

x = int(input("Enter a number: "))

# Basic if
if x > 0:
    print("Positive")

# if-else
if x % 2 == 0:
    print("Even")
else:
    print("Odd")

# if-elif-else
if x < 0:
    print("Negative")
elif x == 0:
    print("Zero")
else:
    print("Positive")

# Multiple conditions
age = int(input("Enter your age: "))
if age >= 18 and age <= 65:
    print("Working age")
else:
    print("Not working age")
