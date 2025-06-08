# 05_data_structures/arrays_basics.py

import array

# Arrays: fixed-type, memory-efficient sequences

# Create an array of integers (typecode 'i')
arr = array.array('i', [10, 20, 30, 40])

print("Array:", arr)
print("First element:", arr[0])

# Append and extend
arr.append(50)
arr.extend([60, 70])

print("After append and extend:", arr)

# Iterate over array
for num in arr:
    print(num)

# Array typecodes examples:
# 'i' - signed int
# 'f' - float
# 'd' - double
# 'u' - Unicode char

# Create an array of floats
arr_float = array.array('f', [1.5, 2.5, 3.5])
print("Float array:", arr_float)

# Note: Arrays are more efficient than lists for large numeric data but less flexible
