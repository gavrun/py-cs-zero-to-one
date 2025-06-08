# 09_problem_solving_patterns/two_pointer.py

# Two-pointer technique: useful for searching/sorting problems in arrays

# Example: check if a pair sums to target (sorted list)
def has_pair_with_sum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current = nums[left] + nums[right]
        if current == target:
            return True
        elif current < target:
            left += 1
        else:
            right -= 1

    return False

# Example usage
nums = [1, 2, 3, 4, 6, 8, 10]
print(has_pair_with_sum(nums, 10))  # True (2 + 8)
print(has_pair_with_sum(nums, 5))   # False

