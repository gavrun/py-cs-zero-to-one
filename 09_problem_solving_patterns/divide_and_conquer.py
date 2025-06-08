# 09_problem_solving_patterns/divide_and_conquer.py

# Divide and conquer: break problem into subproblems, solve recursively

# Example: binary search (classic divide and conquer)
def binary_search(arr, target):
    return search(arr, target, 0, len(arr) - 1)

def search(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return search(arr, target, mid + 1, high)
    else:
        return search(arr, target, low, mid - 1)

# Example usage
data = [1, 3, 5, 7, 9, 11]
print(binary_search(data, 7))  # 3
print(binary_search(data, 4))  # -1

