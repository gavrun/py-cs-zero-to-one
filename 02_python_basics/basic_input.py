# 02_python_basics/basic_input.py

# Basic input in Python

# Get user input as string
name = input("Enter your name: ")
print("Hello,", name)

# Input is always a string — convert if needed
age_str = input("Enter your age: ")
age = int(age_str)
print("Next year, you will be", age + 1)

# Float input
height = float(input("Enter your height in meters: "))
print("You entered:", height)

# Direct conversion
num = int(input("Enter a number: "))
print("Squared:", num ** 2)

