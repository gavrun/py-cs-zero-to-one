# 00_cs_intro/number_systems.py

# Number systems: binary, octal, decimal, hexadecimal

# Decimal (base 10)
dec = 255

# Binary (base 2) - prefix 0b
bin_num = 0b11111111  # 255 decimal
print(bin_num)

# Octal (base 8) - prefix 0o
oct_num = 0o377  # 255 decimal
print(oct_num)

# Hexadecimal (base 16) - prefix 0x
hex_num = 0xFF  # 255 decimal
print(hex_num)

# Convert decimal to other bases as strings
print(bin(dec))  # '0b11111111'
print(oct(dec))  # '0o377'
print(hex(dec))  # '0xff'

# Convert string in any base back to decimal
print(int('11111111', 2))  # 255
print(int('377', 8))       # 255
print(int('FF', 16))       # 255

# Arithmetic works same regardless of literal base
a = 0b1010  # 10 decimal
b = 0xA     # 10 decimal
print(a + b)  # 20

