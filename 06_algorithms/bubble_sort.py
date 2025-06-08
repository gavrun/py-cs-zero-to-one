# 06_algorithms/bubble_sort.py

# Bubble Sort: repeatedly swap adjacent elements if out of order

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage
nums = [5, 3, 8, 1, 4]
bubble_sort(nums)
print(nums)  # [1, 3, 4, 5, 8]

# Time complexity: O(n^2)

