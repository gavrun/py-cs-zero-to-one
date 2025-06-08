# 05_data_structures/nested_structures.py

# List of lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][1])  # 2

# Dictionary with list values
grades = {
    "Alice": [85, 90],
    "Bob": [70, 75]
}

print(grades["Alice"][1])  # 90

# Dictionary inside a list
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25}
]

print(people[1]["name"])  # Bob

# Looping through nested structures
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()

# Use nesting to represent structured data

