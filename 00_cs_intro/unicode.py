# 00_cs_intro/unicode.py

# Strings in Python 3 are Unicode by default
s = "Hello, 世界"

print(s)  # prints Unicode characters

# Unicode code points: get ordinal number of a character
print(ord('A'))       # 65
print(ord('世'))      # 19990
print(ord('界'))      # 30028

# Convert code point back to character
print(chr(65))        # 'A'
print(chr(19990))     # '世'

# Unicode normalization (important for comparing accented characters)
import unicodedata

s1 = "café"          # 'é' as single code point
s2 = "cafe\u0301"    # 'e' + combining acute accent

print(s1 == s2)      # False without normalization

# Normalize to NFC (composed form)
nfc_s1 = unicodedata.normalize('NFC', s1)
nfc_s2 = unicodedata.normalize('NFC', s2)
print(nfc_s1 == nfc_s2)  # True

# Normalize to NFD (decomposed form)
nfd_s1 = unicodedata.normalize('NFD', s1)
nfd_s2 = unicodedata.normalize('NFD', s2)
print(nfd_s1 == nfd_s2)  # True

# Unicode categories
print(unicodedata.category('A'))  # 'Lu' (Letter, uppercase)
print(unicodedata.category('1'))  # 'Nd' (Number, decimal digit)
print(unicodedata.category(' '))  # 'Zs' (Separator, space)

