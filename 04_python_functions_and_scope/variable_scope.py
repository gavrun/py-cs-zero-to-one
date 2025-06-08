# 04_python_functions_and_scope/variable_scope.py

# Global variable
x = 10

def print_global():
    print("Inside function:", x)

print_global()
print("Outside function:", x)

# Local variable (only exists inside the function)
def set_local():
    y = 5
    print("Local y:", y)

set_local()
# print(y)  # NameError: y is not defined

# Modifying global variable (not recommended unless necessary)
count = 0

def increment():
    global count
    count += 1

increment()
print("Global count:", count)

# Variables inside functions don't affect outer scope unless returned
def multiply(n):
    result = n * 2
    return result

output = multiply(4)
print(output)

