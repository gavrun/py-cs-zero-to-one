# 06_algorithms/linear_search.py

# Search for a target in a list (left to right)

def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i  # return index
    return -1  # not found

# Example usage
numbers = [4, 2, 7, 1, 9]
print(linear_search(numbers, 7))  # 2
print(linear_search(numbers, 5))  # -1

# Can also use for-in with enumerate
def linear_search_enum(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1


