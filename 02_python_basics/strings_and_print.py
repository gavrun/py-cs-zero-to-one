# 02_python_basics/strings_and_print.py

# String creation
s1 = "hello"
s2 = 'world'

# Concatenation
combined = s1 + " " + s2  # "hello world"

# Repetition
repeat = s1 * 3   # "hellohellohello"

# String length
length = len(s1)  # 5

# Indexing (0-based)
first_char = s1[0]   # 'h'
last_char = s1[-1]   # 'o'

# Slicing
sub = s1[1:4]          # 'ell'
every_other = s1[::2]  # 'hlo'

# String formatting
name = "Alice"
age = 30
msg1 = f"{name} is {age} years old"             # f-string
msg2 = "{} is {} years old".format(name, age)   # format()
msg3 = name + " is " + str(age) + " years old"  # manual

# Escape characters
newline = "Line1\nLine2"
tabbed = "Column1\tColumn2"

# Print examples
print(combined)
print(msg1)
print(newline)

