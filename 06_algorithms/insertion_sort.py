# 06_algorithms/insertion_sort.py

# Insertion Sort: build sorted list one element at a time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage
nums = [7, 2, 4, 1, 5]
insertion_sort(nums)
print(nums)  # [1, 2, 4, 5, 7]

# Time complexity: O(n^2)

