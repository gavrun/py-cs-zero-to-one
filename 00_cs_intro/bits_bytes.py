# 00_cs_intro/bits_bytes.py

# Bits and Bytes basics

# A bit is a binary digit: 0 or 1
bit_0 = 0
bit_1 = 1

# A byte is 8 bits
byte = 0b01101001  # example byte

# Number of bits in a byte
BITS_IN_BYTE = 8

# Convert integer to bytes and back
num = 1024
num_bytes = num.to_bytes(2, byteorder='big')  # 2 bytes big-endian
print(num_bytes)  # b'\x04\x00'

num_back = int.from_bytes(num_bytes, byteorder='big')
print(num_back)  # 1024

# Bitwise operations examples

x = 0b1010  # 10 decimal
y = 0b1100  # 12 decimal

print(bin(x & y))  # AND: 0b1000 (8)
print(bin(x | y))  # OR:  0b1110 (14)
print(bin(x ^ y))  # XOR: 0b0110 (6)
print(bin(~x & 0b1111))  # NOT on 4 bits: 0b0101 (5)

# Shifts
print(bin(x << 1))  # Left shift: 0b10100 (20)
print(bin(y >> 2))  # Right shift: 0b0011 (3)

