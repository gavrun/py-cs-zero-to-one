# 05_data_structures/strings_operations.py

text = "  Hello, Python!  "

# Length of the string
print(len(text))  # 17

# Case conversion
print(text.lower())   # "  hello, python!  "
print(text.upper())   # "  HELLO, PYTHON!  "
print(text.strip())   # "Hello, Python!"
print(text.lstrip())  # "Hello, Python!  "
print(text.rstrip())  # "  Hello, Python!"

# Find and replace
print(text.find("Python"))              # 9
print(text.find("Python", 5))           # 9
print(text.find("Python", 5, 15))       # 9
print(text.replace("Python", "World"))  # "  Hello, World!  "
print(text.replace(" ", "_", 2))        # Replace first two spaces

# Splitting and joining
words = text.strip().split(",")  # ['Hello', ' Python!']
joined = "-".join(words)         # "Hello- Python!"
print(joined)

# Partition into three parts: before, delimiter, after
parts = text.partition(",")   # ('  Hello', ',', ' Python!  ')
print(parts)

# Check if string starts or ends with a substring
print(text.startswith("  He"))  # True
print(text.endswith("!  "))     # True

# Count character occurrences
print(text.count("l"))   # 2

# Common string checks
print("Python".isalpha())   # True — all characters are alphabetic
print("hello".islower())    # True — all lowercase
print("HELLO".isupper())    # True — all uppercase
print("12345".isdigit())    # True — all digits
print("123.45".isnumeric()) # False — not a numeric string

# Title and capitalization
print("hello world".title())      # Hello World
print("hello world".capitalize()) # Hello world

# Text justification
print("52000".rjust(10))  # Right align with padding
print("52000".ljust(10))  # Left align with padding
print("52000".center(10)) # Centered text

# Input validation example
# string = input("Enter a number: ")
# if string.isnumeric():
#     number = int(string)
#     print(number)

# Splitting by space, comma, and limit
text = "This was a huge, double-wrapped oak, with broken branches and bark"
splitted_text = text.split()   # Split by whitespace
print(splitted_text[6])        # oak,

splitted_commas = text.split(",")   # Split by comma
print(splitted_commas[1])           # double-wrapped oak

splitted_limited = text.split(" ", 5)  # Split by first 5 spaces
print(splitted_limited[5])             # wrapped oak, with broken branches and bark

# Partition example
parts = text.partition("oak")
print(parts)  # ('This was a huge, double-wrapped ', 'oak', ', with broken branches and bark')

# Join a list of strings
words = ["Let", "me", "speak", "from", "my", "heart", "in", "English"]
sentence = " ".join(words)
print(sentence)  # Let me speak from my heart in English

# Join with a custom delimiter
sentence = " | ".join(words)
print(sentence)  # Let | me | speak | from | my | heart | in | English

# Join characters in a string
word = "hello"
joined_word = "|".join(word)
print(joined_word)  # h|e|l|l|o

# Reminder: strings are immutable — all operations return a new string
