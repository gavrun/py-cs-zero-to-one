# 06_algorithms/find_min_max.py

# Find minimum and maximum values in a list

def find_min_max(lst):
    if not lst:
        return None, None

    min_val = lst[0]
    max_val = lst[0]

    for num in lst[1:]:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    return min_val, max_val

# Example usage
numbers = [4, 1, 9, 3, 7]
low, high = find_min_max(numbers)
print("Min:", low)   # 1
print("Max:", high)  # 9

# Built-in alternatives
print(min(numbers))  # 1
print(max(numbers))  # 9
