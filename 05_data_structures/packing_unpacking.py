# 05_data_structures/packing_unpacking.py

# Basic packing and unpacking (destructuring)

num1 = 1
num2 = 2
num3 = 3
*numbers,=num1,num2,num3
print(numbers)  #[1, 2, 3]

# Unpacking a tuple or list into variables

point = (3, 4)
x, y = point
print(x, y)           # 3 4

items = ["apple", "banana", "cherry"]
a, b, c = items
print(a, c)           # apple cherry

# Ignoring values with underscore
name, _, age = ("Alice", "skip", 30)
print(name, age)      # Alice 30

# Extended unpacking with *
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(first)          # 1
print(middle)         # [2, 3, 4]
print(last)           # 5

# Leading or trailing rest
head, *tail = numbers
*init, end = numbers

print(tail)           # [2, 3, 4, 5]
print(init)           # [1, 2, 3, 4]

# Packing with *args and **kwargs in functions
def greet(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

greet("hello", "world", user="Alice", lang="EN")

# Unpacking in function calls
def show(a, b, c):
    print(a, b, c)

values = [10, 20, 30]
show(*values)         # 10 20 30

params = {"a": 1, "b": 2, "c": 3}
show(**params)        # 1 2 3

# Merging lists, sets, and dicts (Python 3.5+)
a = [1, 2]
b = [3, 4]
combined = [*a, *b]    # [1, 2, 3, 4]

s1 = {1, 2}
s2 = {2, 3}
merged_set = {*s1, *s2}  # {1, 2, 3}

d1 = {"x": 1}
d2 = {"y": 2}
merged_dict = {**d1, **d2}  # {'x': 1, 'y': 2}


# (a, b) = (1, 2)                    # unpacking
# (a, _, c) = (1, 2, 3)              # ignore value
# (a, *rest) = [1, 2, 3, 4]          # extended unpack
# def f(*args, **kwargs):           # packing
# f(*list), f(**dict)               # unpack when calling
# [*a, *b], {*a, *b}, {**a, **b}     # merging with unpacking

