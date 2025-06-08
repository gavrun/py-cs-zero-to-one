# 07_python_advanced/stdlib/standard_library_math.py

# Python 'math' module
# Provides mathematical functions for floats and integers

import math

# Constants
print("pi:", math.pi)                # 3.14159...
print("e:", math.e)                  # 2.71828...
print("tau:", math.tau)              # 6.28318...
print("infinity:", math.inf)         # positive infinity
print("not-a-number:", math.nan)     # NaN

# Rounding
print("floor(3.9):", math.floor(3.9))   # 3
print("ceil(3.1):", math.ceil(3.1))     # 4
print("trunc(3.7):", math.trunc(3.7))   # 3 (removes decimal)

# Absolute value and sign
print("fabs(-7):", math.fabs(-7))       # 7.0
print("copysign(3, -1):", math.copysign(3, -1))  # -3.0

# Power and roots
print("pow(2, 3):", math.pow(2, 3))     # 8.0 (always float)
print("sqrt(16):", math.sqrt(16))       # 4.0
print("isqrt(17):", math.isqrt(17))     # 4 (int square root)
print("exp(2):", math.exp(2))           # e^2

# Logarithms
print("log(8, 2):", math.log(8, 2))     # 3.0
print("log10(1000):", math.log10(1000)) # 3.0
print("log2(1024):", math.log2(1024))   # 10.0

# Trigonometry (angles in radians)
print("sin(pi/2):", math.sin(math.pi / 2))  # 1.0
print("cos(0):", math.cos(0))               # 1.0
print("tan(pi/4):", math.tan(math.pi / 4))  # ~1.0

# Inverse trig functions
print("asin(1):", math.asin(1))             # pi/2
print("acos(1):", math.acos(1))             # 0.0
print("atan(1):", math.atan(1))             # pi/4

# Degree-radian conversions
print("degrees(pi):", math.degrees(math.pi))    # 180.0
print("radians(180):", math.radians(180))       # pi

# Special comparisons
print("isfinite(5):", math.isfinite(5))         # True
print("isinf(math.inf):", math.isinf(math.inf)) # True
print("isnan(math.nan):", math.isnan(math.nan)) # True

# Greatest common divisor and least common multiple
print("gcd(48, 18):", math.gcd(48, 18))         # 6
print("lcm(4, 6):", math.lcm(4, 6))             # 12  (Python 3.9+)

# Factorial
print("factorial(5):", math.factorial(5))       # 120

# Precision tips
print("round(math.sqrt(2) ** 2, 10):", round(math.sqrt(2) ** 2, 10))  # ~2.0

# math.pi, math.e, math.tau       → constants
# math.floor(), ceil(), trunc()   → rounding
# math.sqrt(), pow(), isqrt()     → roots, powers
# math.exp(), log(), log10(), log2()
# math.sin(), cos(), tan(), asin(), acos(), atan()
# math.degrees(), radians()
# math.factorial(), gcd(), lcm()
# math.isfinite(), isnan(), isinf()
