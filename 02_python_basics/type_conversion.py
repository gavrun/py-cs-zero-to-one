# 02_python_basics/type_conversion.py

# Type Conversion

x = int(3.99)     # 3 (truncate toward zero)
y = float(7)      # 7.0
z = str(42)       # "42"

print("int('123'):", int("123"))      # 123
print("float('3.14'):", float("3.14"))# 3.14

# Safe conversion

s = "not a number"
if s.isdigit():
    val = int(s)
else:
    val = None

# Safe conversion with try/except

try:
    num = int("abc")
except ValueError:
    print("Conversion failed")


# Convert string to int/float
num1 = int("42")      # 42
num2 = float("3.14")  # 3.14

# Convert number to string
s1 = str(100)         # "100"
s2 = str(3.5)         # "3.5"

# Convert between int and float
i = int(5.9)          # 5
f = float(10)         # 10.0

# Convert to bool
print(bool(0))        # False
print(bool(1))        # True
print(bool(""))       # False
print(bool("text"))   # True

print("bool(0):", bool(0))       # False
print("bool(42):", bool(42))     # True

print("int(True):", int(True))   # 1
print("int(False):", int(False)) # 0

# Convert iterable types
lst = list("abc")     # ['a', 'b', 'c']
tpl = tuple([1, 2])   # (1, 2)
st = set("aaab")      # {'a', 'b'}


