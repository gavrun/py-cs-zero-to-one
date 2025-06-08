# 05_data_structures/common_collections_basics.py

# Common operations across data structures 
# These built-in functions work across types: list, tuple, set, dict, str

# 1. Length
print(len([1, 2, 3]))           # 3
print(len("hello"))            # 5
print(len({"a": 1, "b": 2}))    # 2

# 2. Membership check
print("e" in "hello")          # True
print(3 in [1, 2, 3])          # True
print("a" in {"a": 1})         # True

# 3. Looping over elements
for x in [10, 20, 30]:
    print(x)

for char in "abc":
    print(char)

for key in {"x": 1, "y": 2}:
    print(key)

# 4. Indexing (only for ordered types: list, tuple, str)
seq = ["a", "b", "c"]
print(seq[0])        # "a"
print("hello"[1])    # "e"

# 5. Slicing (ordered types)
print([0, 1, 2, 3][1:3])   # [1, 2]
print("abcdef"[::2])      # 'ace'

# 6. Copying
lst = [1, 2, 3]
copy1 = lst[:]            # via slicing
copy2 = lst.copy()        # method
copy3 = list(lst)         # constructor

# 7. Sorting (list, tuple, set)
data = [3, 1, 4, 1]
print(sorted(data))       # [1, 1, 3, 4] (returns new list)

# 8. Reversing
print(list(reversed(data)))  # [1, 4, 1, 3]

# 9. Conversion between types
print(list("abc"))       # ['a', 'b', 'c']
print(set([1, 2, 2, 3]))  # {1, 2, 3}
print(dict([("a", 1), ("b", 2)]))  # {'a': 1, 'b': 2}

# 10. Unpacking
a, b, c = [10, 20, 30]
print(a, b, c)

# 11. Enumerate (index + value)
for i, val in enumerate(["x", "y", "z"]):
    print(i, val)

# 12. Zip (combine multiple iterables)
names = ["Alice", "Bob"]
ages = [30, 25]
for name, age in zip(names, ages):
    print(name, age)

# 13. Any, all
print(any([0, 0, 1]))     # True (at least one true)
print(all([1, True, 5]))  # True (all true)

# 14. max, min, sum
nums = [4, 1, 7]
print(max(nums))    # 7
print(min(nums))    # 1
print(sum(nums))    # 12

