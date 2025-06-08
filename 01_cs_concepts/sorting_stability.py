# 01_cs_concepts/sorting_stability.py

# Sorting Stability

# A sorting algorithm is stable if it preserves the relative order of equal elements.

# Why stability matters

# When sorting by multiple criteria (e.g., first by age, then by name), stable sorts keep previous order intact.
# Unstable sorts may reorder equal elements unpredictably.

# Examples

# | Algorithm       | Stable?   |
# |-----------------|-----------|
# | Bubble Sort     | Yes       |
# | Insertion Sort  | Yes       |
# | Merge Sort      | Yes       |
# | Quick Sort      | No        |
# | Heap Sort       | No        |

# Python's `sorted()` and `.sort()`

# Both use Timsort, which is stable.

data = [("Alice", 25), ("Bob", 20), ("Charlie", 25)]

# Sort by age (stable)
sorted_by_age = sorted(data, key=lambda x: x[1])
print(sorted_by_age)

# [('Bob', 20), ('Alice', 25), ('Charlie', 25)]

