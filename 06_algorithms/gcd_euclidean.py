# 06_algorithms/gcd_euclidean.py

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(48, 18))  # 6
print(gcd(100, 25)) # 25
print(gcd(7, 3))    # 1

