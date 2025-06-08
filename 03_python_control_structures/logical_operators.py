# 03_python_control_structures/logical_operators.py

# Basic Logical Operators

a = 5
b = 10

# and: True if BOTH sides are True
print(a > 0 and b > 0)     # True
print(a > 0 and b < 0)     # False

# or: True if AT LEAST ONE side is True
print(a > 0 or b < 0)      # True
print(a < 0 or b < 0)      # False

# not: Inverts the boolean value
print(not True)            # False
print(not (a > 0))         # False


# With if statements

age = 25
if age >= 18 and age <= 30:
    print("Young adult")

# more Pythonic
if 18 <= age <= 30:
    print("Also young adult")


# Short-circuit behavior

# If first condition in `and` is False, second is not evaluated
# If first condition in `or` is True, second is not evaluated

def left():
    print("left evaluated")
    return False

def right():
    print("right evaluated")
    return True

print("\nShort-circuit AND:")
if left() and right():
    print("both True")
else:
    print("short-circuit triggered")

print("\nShort-circuit OR:")
if right() or left():
    print("short-circuit triggered")


# Logical operators with non-boolean values

# In Python, these return the actual object (not just True/False)

x = "" or "fallback"      # '' is falsy → returns "fallback"
print("x =", x)

y = "hello" and 123       # both truthy → returns second value
print("y =", y)

z = None and "skip me"    # None is falsy → returns None
print("z =", z)


# In loops

tries = 0
max_tries = 3
success = False

while tries < max_tries and not success:
    answer = input("Type yes to proceed: ")
    success = (answer == "yes")
    tries += 1

if success:
    print("Thank you!")
else:
    print("Out of attempts")


# Tips 
# - Don't overuse `not not x` to coerce to bool — use `bool(x)`
# - Use parentheses to clarify logic
# - Truthy/falsy: "", 0, None, [] → all count as False

