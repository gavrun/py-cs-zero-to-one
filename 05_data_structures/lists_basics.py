# 05_data_structures/lists_basics.py

# Create a list
fruits = ["apple", "banana", "cherry"]

# Access items by index
print(fruits[0])     # apple
print(fruits[-1])    # cherry (last item)

# Modify items
fruits[1] = "blueberry"  # banana -> blueberry

# Add items
fruits.append("date")           # add to end
fruits.insert(1, "kiwi")        # insert at index 1

# Remove items
fruits.remove("apple")          # remove by value (first occurrence)
last = fruits.pop()             # remove last item and return it
del fruits[0]                   # remove by index

# Check for existence
if "banana" in fruits:
    print("Found")

# List length
print(len(fruits))

# Loop through list
for fruit in fruits:
    print(fruit)

# Create empty list
empty = []

# List slicing
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])      # [1, 2, 3]
print(numbers[:3])       # [0, 1, 2]
print(numbers[::2])      # [0, 2, 4] (step=2)
print(numbers[::-1])     # [5, 4, 3, 2, 1, 0] (reverse)

# Copying lists
copy1 = numbers[:]             # full slice
copy2 = list(numbers)          # constructor copy
copy3 = numbers.copy()         # method copy

# List comprehension
squares = [x**2 for x in range(6)]          # [0, 1, 4, 9, 16, 25]
evens = [x for x in range(10) if x % 2 == 0]  # filter even numbers

# Sorting
unsorted = [5, 2, 9, 1]
sorted_list = sorted(unsorted)             # returns new sorted list
unsorted.sort()                            # sorts in place
unsorted.sort(reverse=True)                # descending order

words = ["banana", "Apple", "cherry"]
words.sort(key=str.lower)                  # case-insensitive sort

# Nested lists
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix[1][2])        # 6

# Removing all items (clearing)
fruits.clear()

# Safe removal during iteration
data = [1, 2, 3, 4, 5]
data = [x for x in data if x % 2 == 0]  # keep only even numbers

# Min, Max, Sum
nums = [3, 1, 4, 1, 5]
print(min(nums))  # 1
print(max(nums))  # 5
print(sum(nums))  # 14

# Index and Count
letters = ["a", "b", "a", "c"]
print(letters.index("b"))   # 1
print(letters.count("a"))   # 2

