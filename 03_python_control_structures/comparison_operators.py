# 03_python_control_structures/comparison_operators.py

a = 10
b = 20

print(a == b)   # False (equal to)
print(a != b)   # True  (not equal to)
print(a < b)    # True  (less than)
print(a <= b)   # True  (less than or equal to)
print(a > b)    # False (greater than)
print(a >= b)   # False (greater than or equal to)

# Compare strings (lexicographical)
print("apple" == "apple")   # True
print("apple" < "banana")   # True
print("a" > "Z")            # True (lowercase > uppercase in ASCII)

# Compare mixed types (avoid)
# print(3 < "4")  # TypeError in Python 3
