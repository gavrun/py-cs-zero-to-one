# 00_cs_intro/encoding.py

# Text encoding in Python

# Strings in Python are Unicode by default
text = "hello, world"

# Encode string to bytes using UTF-8
encoded_utf8 = text.encode('utf-8')
print(encoded_utf8)  # b'hello, world'

# Decode bytes back to string
decoded_utf8 = encoded_utf8.decode('utf-8')
print(decoded_utf8)  # hello, world

# Encoding with other codecs
encoded_ascii = text.encode('ascii')
print(encoded_ascii)  # b'hello, world'

# Handling characters outside ASCII range
unicode_text = "café"

# UTF-8 encoding supports accented characters
utf8_bytes = unicode_text.encode('utf-8')
print(utf8_bytes)  # b'caf\xc3\xa9'

# ASCII encoding fails on accented characters
try:
    ascii_bytes = unicode_text.encode('ascii')
except UnicodeEncodeError as e:
    print("ASCII encoding error:", e)

# Common encodings: utf-8, ascii, latin-1, utf-16

# Reading bytes from a file and decoding

# with open('example.txt', 'rb') as f:
#     data = f.read()
#     text = data.decode('utf-8')

