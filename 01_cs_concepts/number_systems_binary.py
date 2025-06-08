# 01_cs_concepts/number_systems_binary.py

# Binary number basics

# Decimal to binary (built-in)
n = 42
print(bin(n))  # '0b101010'

# Binary literals
b = 0b1010  # 10 in decimal
print(b)

# Convert binary string to int
s = "1101"
x = int(s, 2)
print(x)  # 13

# Binary arithmetic
a = 0b1100  # 12
b = 0b1010  # 10

print(bin(a + b))  # 0b10110 (22)
print(bin(a & b))  # 0b1000  (8)
print(bin(a | b))  # 0b1110  (14)

# Formatting integers as binary with leading zeros
print(f"{n:08b}")  # 00101010 (8 bits)
