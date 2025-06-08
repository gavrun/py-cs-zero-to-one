# 07_python_advanced/stdlib/standard_library_decimal.py

# Python 'decimal' module
# Decimal floating-point arithmetic for precision-critical tasks

from decimal import Decimal, getcontext, ROUND_HALF_UP, ROUND_DOWN

# Create decimals
d1 = Decimal('0.1')
d2 = Decimal('0.2')
print("0.1 + 0.2 =", d1 + d2)  # 0.3 (precise)

# float has binary imprecision
print("float(0.1 + 0.2):", 0.1 + 0.2)  # 0.30000000000000004

# Converting from float is unsafe
print("Decimal from float:", Decimal(0.1))  # Inexact!

# Always convert from string or integer
d3 = Decimal(1) / Decimal(7)
print("1/7:", d3)

# Setting precision globally
getcontext().prec = 6
print("Low precision:", Decimal(1) / Decimal(7))  # 0.142857

# Arithmetic operations
a = Decimal('2.5')
b = Decimal('1.3')

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Exponentiation:", a ** 2)

# Rounding
getcontext().prec = 4
x = Decimal('2.675')

print("ROUND_HALF_UP:", x.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))  # 2.68
print("ROUND_DOWN:", x.quantize(Decimal('0.01'), rounding=ROUND_DOWN))        # 2.67

# Comparisons
print(Decimal('1.00') == Decimal('1.000'))     # False (different precision)
print(Decimal('1.00').compare(Decimal('1.000')))  # Decimal('0') if numerically equal

# Special values
print("Infinity:", Decimal('Infinity'))
print("NaN:", Decimal('NaN'))

# Context management
from decimal import localcontext

with localcontext() as ctx:
    ctx.prec = 3
    print("Scoped precision:", Decimal(1) / Decimal(7))  # 0.143


# Decimal(str)           → safe initialization
# getcontext().prec      → global precision
# .quantize(format, rounding) → control rounding
# ROUND_* constants      → various rounding strategies
# Comparisons preserve precision info
# Use localcontext()     → temporary precision override

# Always prefer Decimal over float for:
# - financial apps
# - currency calculations
# - tax computations
# - any domain where 0.1 + 0.2 == 0.3 must hold
