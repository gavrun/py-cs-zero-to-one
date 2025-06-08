# 05_data_structures/strings_basics.py

# A string is a sequence of Unicode characters wrapped in quotes

message = "Hello World!"
print(message)  # Hello World!

name = 'Tom'
print(name)  # Tom

# Long string split across lines using parentheses
text = (
    "Laudate omnes gentes laudate "
    "Magnificat in secula "
)
print(text)

# Multiline string using triple quotes
text = '''Laudate omnes gentes laudate
Magnificat in secula
Et anima mea laudate
Magnificat in secula'''
print(text)

# Escape sequences in strings
text = "Message:\n\"Hello World\""
print(text)  # Message: \n"Hello World"

# Raw strings ignore escape sequences
path = r"C:\\python\\name.txt"
print(path)  # C:\python\name.txt

# f-strings allow variable interpolation
userName = "Tom"
userAge = 37
user = f"name: {userName}  age: {userAge}"
print(user)  # name: Tom  age: 37

# Indexing characters in a string
string = "hello world"
c0 = string[0]  # h
print(c0)
c6 = string[6]  # w
print(c6)

# Negative indexing
c1 = string[-1]  # d
print(c1)
c5 = string[-5]  # w
print(c5)

# Strings are immutable — this will cause an error:
# string[1] = "R"  # TypeError

# Iterating over a string
for char in string:
    print(char)

# Slicing substrings
print(string[:5])       # hello
print(string[2:5])      # llo
print(string[2:9:2])    # lowr

# Concatenation and type conversion
name = "Tom"
age = 33
info = "Name: " + name + " Age: " + str(age)
print(info)

# Repeating strings
print("a" * 3)      # aaa
print("he" * 4)     # hehehehe

# String comparison (lexicographical)
str1 = "1a"
str2 = "aa"
str3 = "Aa"
print(str1 > str2)  # False
print(str2 > str3)  # True

# Case-insensitive comparison
str1 = "Tom"
str2 = "tom"
print(str1 == str2)              # False
print(str1.lower() == str2.lower())  # True

# Unicode code point and length
print(ord("A"))  # 65
print(len("hello world"))  # 11

# Membership testing
text = "hello world"
print("hello" in text)   # True
print("sword" in text)   # False
print("hello" not in text)  # False
print("sword" not in text)  # True

