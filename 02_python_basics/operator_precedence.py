# 02_python_basics/operator_precedence.py

# Operator Precedence (highest to lowest)

# ( )             ← grouping
# **              ← exponent
# +x, -x, not x   ← unary
# *, /, //, %     ← multiplicative
# +, -            ← additive
# <<, >>          ← shifts
# &               ← bitwise AND
# ^               ← bitwise XOR
# |               ← bitwise OR
# ==, !=, <, ...  ← comparisons
# not             ← logical NOT
# and             ← logical AND
# or              ← logical OR
# if ... else     ← conditional expression
# =, +=, ...      ← assignment
# lambda          ← lambda expression

a = 10
b = 3

# 1. PARENTHESES
# Used to group and override precedence
# (a + b) * c → forces addition before multiplication


# 2. EXPONENTIATION
# Right-associative
print(2 ** 3 ** 2)  # 2 ** (3 ** 2) = 512


# 3. UNARY OPERATORS
# Positive, negative, logical NOT
print(-3)          # Unary minus
print(+5)          # Unary plus
print(not True)    # Logical NOT


# 4. MULTIPLICATIVE
# Multiplication, division, floor div, modulo
print(5 * 2)       # 10
print(5 / 2)       # 2.5
print(5 // 2)      # 2
print(5 % 2)       # 1


# 5. ADDITIVE
# Addition, subtraction
print(3 + 4 - 1)   # 6


# 6. BITWISE SHIFTS
print(4 << 1)      # 8 (shift left)
print(8 >> 2)      # 2 (shift right)


# 7. BITWISE AND
print(5 & 3)       # 1 (0101 & 0011)


# 8. BITWISE XOR
print(5 ^ 3)       # 6 (0101 ^ 0011)


# 9. BITWISE OR
print(5 | 2)       # 7 (0101 | 0010)


# 10. COMPARISONS / MEMBERSHIP / IDENTITY
print(3 < 4)         # True
print("a" in "cat")  # True
print(a is b)        # Identity check

# Multiple comparisons are chained:
print(1 < 2 < 3)   # True


# 11. NOT
print(not False)   # True


# 12. AND (logical)
print(True and False)  # False


# 13. OR (logical)
print(True or False)   # True


# 14. CONDITIONAL (TERNARY) EXPRESSION
x = 10
result = "yes" if x > 5 else "no"


# 15. ASSIGNMENT
x = 3
x += 1   # compound assignment (+=, -=, etc.)


# 16. EXPRESSION SEPARATORS
# Commas (tuple, function args, etc.)
# Colons (in slices, dicts)
# Semicolons (multiple statements per line)


# 17. LAMBDA EXPRESSION
f = lambda x: x + 1
print(f(5))  # 6


# Tips:
# - Use parentheses to make intent clear — always better than relying on precedence
# - Most common confusion: `not`, `and`, `or` have lower precedence than expected
#   Example: `not a == b` is parsed as `not (a == b)`, NOT `(not a) == b`
# - Assignment is always last — it never combines with expressions

