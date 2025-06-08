# 09_problem_solving_patterns/sliding_window.py or /sliding_window.py

# Sliding window: efficient technique for problems involving subarrays

# Example: find max sum of any subarray of size k
def max_subarray_sum(nums, k):
    if len(nums) < k:
        return None

    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum

# Example usage
numbers = [2, 1, 5, 1, 3, 2]
print(max_subarray_sum(numbers, 3))  # 9 (5 + 1 + 3)

