# 11_computer_science_concepts/boolean_logic_intro.py

# Boolean Logic

# Boolean logic deals with truth values: **True** and **False**.

# Basic Operators

# | Operator | Symbol | Description       |
# |----------|---------|-------------------|
# | AND      | `and`   | True if both true |
# | OR       | `or`    | True if any true  |
# | NOT      | `not`   | Inverts value     |

# Truth Table

# | A     | B     | A and B | A or B | not A |
# |-------|-------|---------|--------|-------|
# | True  | True  | True    | True   | False |
# | True  | False | False   | True   | False |
# | False | True  | False   | True   | True  |
# | False | False | False   | False  | True  |

# Usage in Python

a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False

