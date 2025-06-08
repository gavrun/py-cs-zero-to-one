# 06_algorithms/merge_sort.py

# Merge Sort: divide-and-conquer sorting algorithm

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # Merge sorted halves
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example usage
nums = [6, 3, 8, 2, 5]
sorted_nums = merge_sort(nums)
print(sorted_nums)  # [2, 3, 5, 6, 8]

# Time complexity: O(n log n)

