# 04_python_functions_and_scope/default_and_keyword_args.py

# Default arguments
def greet(name="Guest"):
    print("Hello,", name)

greet("Alice")   # Hello, Alice
greet()          # Hello, Guest

# Multiple default arguments
def power(base, exponent=2):
    return base ** exponent

print(power(3))       # 9
print(power(3, 3))    # 27

# Keyword arguments
def describe_pet(animal, name):
    print(f"{name} is a {animal}")

describe_pet("dog", "Buddy")             # positional
describe_pet(animal="cat", name="Milo")  # keyword
describe_pet(name="Rex", animal="dog")   # keyword, order doesn't matter
