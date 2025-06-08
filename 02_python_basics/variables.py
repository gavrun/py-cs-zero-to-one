# 02_python_basics/variables.py

# Variable assignment
x = 10
y = 3.5
name = "Alice"

# Multiple assignment
a, b = 1, 2

# Swapping values
a, b = b, a  # now a = 2, b = 1

# Constants (by convention, not enforced)
PI = 3.14159
MAX_USERS = 100

# Naming rules
# - Must start with a letter or underscore
# - Can contain letters, digits, underscores
# - Case-sensitive

# Valid examples
count = 5
_count = 10
count2 = 15

# Invalid (will raise errors)
# 2count = 20
# my-count = 25
# class = "test"  # 'class' is a keyword

# Check current value
print(x, y, name)

