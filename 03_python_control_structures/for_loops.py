# 03_python_control_structures/for_loops.py


# Loop over a range of numbers
for i in range(5):
    print(i)  # 0 to 4

# Range with start, stop, step
for i in range(2, 10, 2):
    print(i)  # 2, 4, 6, 8

# Loop over a string
for char in "python":
    print(char)

# Loop over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop with index using enumerate
for index, value in enumerate(fruits):
    print(index, value)


# Nested loops

for i in range(3):
    for j in range(2):
        print(i, j)

for k in range(2):
    for n in range(3):
        print(f"{k=}, {n=}")


# Loop over a tuple
coords = [(0, 0), (1, 2), (3, 4)]
for x, y in coords:
    print(f"x={x}, y={y}")


# Loop over a set (unordered)
colors = {"red", "green", "blue"}
for color in colors:
    print(color)


# Loop over a dictionary
person = {"name": "Alice", "age": 30}
for key, value in person.items():
    print(f"{key} → {value}")


# For loop with else
# else block runs only if loop completes normally (no break)
for fruit in fruits:
    if fruit == "durian":
        break
else:
    print("Durian not found")  # this prints


# Generator style loop (collecting results)
squares = []
for x in range(5):
    squares.append(x * x)
print("Squares:", squares)
# Equivalent to:
# squares = [x * x for x in range(5)]

