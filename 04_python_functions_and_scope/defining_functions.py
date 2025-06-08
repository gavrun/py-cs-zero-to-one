# 04_python_functions_and_scope/defining_functions.py

# Define a simple function
def greet():
    print("Hello!")

# Call the function
greet()

# Function with parameters
def greet_person(name):
    print("Hello,", name)

greet_person("Alice")

# Function with return value
def square(n):
    return n * n

result = square(4)  # 16
print(result)

# Function can be reused multiple times
for i in range(3):
    print(square(i))

