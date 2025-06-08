# 01_cs_concepts/complexity_practice.py

# Examples of different time complexities

def constant_time(lst):
    return lst[0]  # O(1)

def linear_time(lst):
    total = 0
    for x in lst:
        total += x  # O(n)
    return total

def quadratic_time(lst):
    count = 0
    for i in lst:
        for j in lst:
            count += 1  # O(n^2)
    return count

def logarithmic_time(n):
    count = 0
    i = 1
    while i < n:
        count += 1  # O(log n)
        i *= 2
    return count


# Example usage

lst = list(range(10))

print(constant_time(lst))     # 0
print(logarithmic_time(16))   # 4
print(linear_time(lst))       # 45
print(quadratic_time(lst))    # 100

