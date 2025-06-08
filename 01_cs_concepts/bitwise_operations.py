# 01_cs_concepts/bitwise_operations.py

# Bitwise operators work on binary representations of integers

a = 60  # 0b00111100
b = 13  # 0b00001101

print(a & b)  # AND: 12 (0b00001100)

print(a | b)  # OR: 61  (0b00111101)

print(a ^ b)  # XOR: 49 (0b00110001)

print(~a)     # NOT: -61 (two's complement)

print(a << 2) # Left shift: 240 (0b11110000)

print(a >> 2) # Right shift: 15 (0b00001111)
