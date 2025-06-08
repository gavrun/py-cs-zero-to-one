# 01_cs_concepts/counting_principles.py

# Basic counting principles in combinatorics

# Addition principle
# If event A can occur in m ways, event B in n ways, and they are mutually exclusive,
# then total ways = m + n

ways_A = 3
ways_B = 5
total_ways = ways_A + ways_B
print("Addition principle:", total_ways)  # 8

# Multiplication principle
# If event A can occur in m ways and event B in n ways, independently,
# then total ways = m * n

ways_A = 4
ways_B = 6
total_ways = ways_A * ways_B
print("Multiplication principle:", total_ways)  # 24


# Example: Number of 3-letter codes where
#  first letter can be A or B (2 ways)
#  second letter any of C, D, E (3 ways)
#  third letter any digit 0-9 (10 ways)

total_codes = 2 * 3 * 10
print("Total 3-letter codes:", total_codes)  # 60


# Example: Counting with restrictions 
# Number of 3-digit numbers with distinct digits

digits = 10  # 0-9
first_digit = 9   # can't be 0
second_digit = 9  # can't be first digit
third_digit = 8   # can't be first or second

total_distinct = first_digit * second_digit * third_digit
print("3-digit numbers with distinct digits:", total_distinct)  # 648

