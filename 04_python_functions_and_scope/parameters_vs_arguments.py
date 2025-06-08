# 04_python_functions_and_scope/parameters_vs_arguments.py

# Parameters: variables defined in the function
# Arguments: actual values passed when calling the function

def add(a, b):  # a and b are parameters
    return a + b

# 5 and 3 are arguments
result = add(5, 3)
print(result)

# Positional arguments (order matters)
print(add(2, 4))  # 6

# Keyword arguments (order doesn't matter)
print(add(b=10, a=1))  # 11

# Mixing positional and keyword
print(add(7, b=2))  # 9
