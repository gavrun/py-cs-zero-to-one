# 06_algorithms/quick_sort.py

# Quick Sort: divide-and-conquer using pivot partitioning

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)

# Example usage
nums = [9, 3, 7, 1, 5]
sorted_nums = quick_sort(nums)
print(sorted_nums)  # [1, 3, 5, 7, 9]

# Time complexity:
# Average: O(n log n)
# Worst: O(n^2) (e.g. sorted input with bad pivot)

