# 02_python_basics/errors_and_debugging.py

# SyntaxError: invalid code structure
# print("Hello"  # missing closing parenthesis

# NameError: using undefined variable
# print(xyz)  # xyz is not defined

# TypeError: wrong type operation
# result = "2" + 3  # can't add string and int

# ZeroDivisionError
# print(10 / 0)


# Handle errors with try-except

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")


