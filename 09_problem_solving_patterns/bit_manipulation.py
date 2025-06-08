# 09_problem_solving_patterns/bit_manipulation.py

# Bit Manipulation Patterns in Python


# 1. Power-of-Two Checks

def is_power_of_two(n):
    # A power of two has only one bit set (e.g. 10000)
    return n > 0 and (n & (n - 1)) == 0


# 2. Counting Set Bits (Brian Kernighan’s Algorithm)

def count_set_bits(n):
    count = 0
    while n:
        n &= n - 1  # Clears the lowest set bit
        count += 1
    return count


# 3. Isolating the Rightmost Set Bit

def rightmost_set_bit(n):
    return n & -n  # Works due to two's complement


# 4. Setting, Clearing, Toggling Bits

def set_bit(n, pos):
    return n | (1 << pos)

def clear_bit(n, pos):
    return n & ~(1 << pos)

def toggle_bit(n, pos):
    return n ^ (1 << pos)


# 5. Checking If a Bit Is Set

def is_bit_set(n, pos):
    return (n & (1 << pos)) != 0


# 6. Swapping Two Numbers Without Temp Variable

def swap(a, b):
    a ^= b
    b ^= a
    a ^= b
    return a, b


# 7. Even/Odd Check Using Bitwise

def is_even(n):
    return (n & 1) == 0


# 8. Multiply/Divide by Powers of 2

def multiply_by_2(n):
    return n << 1

def divide_by_2(n):
    return n >> 1


# 9. Turn Off the Rightmost Set Bit

def clear_rightmost_set_bit(n):
    return n & (n - 1)


# 10. Turn On the Rightmost Zero Bit

def set_rightmost_zero_bit(n):
    return n | (n + 1)


# Example Usage / Test Cases

if __name__ == "__main__":
    print("is_power_of_two(16):", is_power_of_two(16))     # True
    
    print("count_set_bits(15):", count_set_bits(15))       # 4
    
    print("rightmost_set_bit(12):", bin(rightmost_set_bit(12)))  # 0b100
    
    print("toggle_bit(10, 1):", bin(toggle_bit(10, 1)))     # 0b1000
    
    print("is_bit_set(10, 3):", is_bit_set(10, 3))          # True
    
    print("swap(5, 9):", swap(5, 9))                        # (9, 5)
    
    print("is_even(6):", is_even(6))                        # True
    
    print("multiply_by_2(4):", multiply_by_2(4))            # 8
    
    print("clear_rightmost_set_bit(10):", clear_rightmost_set_bit(10))  # 8
    
    print("set_rightmost_zero_bit(10):", set_rightmost_zero_bit(10))    # 11
