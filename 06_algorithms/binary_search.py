# 06_algorithms/binary_search.py

# Binary search requires a sorted list
# Repeatedly divide search interval in half

def binary_search(lst, target):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # not found

# Example usage
numbers = [1, 3, 5, 7, 9, 11]
print(binary_search(numbers, 7))   # 3
print(binary_search(numbers, 4))   # -1
