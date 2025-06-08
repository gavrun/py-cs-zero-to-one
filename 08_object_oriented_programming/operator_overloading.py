# 08_object_oriented_programming/operator_overloading.py

# Operator Overloading in Python

# What is operator overloading?
# Operator overloading lets you define custom behavior for built-in operators
# like +, -, ==, <, etc., for your own classes by implementing special methods
# such as __add__, __eq__, __lt__, __str__, and others.

# Example 1: Overloading __add__ (object addition)

class Counter:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        # called when using a + b
        return Counter(self.count + other.count)

    def __str__(self):
        return f"Counter({self.count})"

# Test
a = Counter(3)
b = Counter(7)
c = a + b
print("Example 1:", c)  # Output: Counter(10)


# Example 2: Overloading arithmetic operators

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"

# Test

v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)
print("Example 2:", v1 + v2)     # Output: Vector2D(4, 6)
print("Example 2:", v2 - v1)     # Output: Vector2D(2, 2)
print("Example 2:", v1 * 3)      # Output: Vector2D(3, 6)


# Example 3: Overloading comparison operators

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

    def __str__(self):
        return f"{self.name} ({self.age})"

# Test

alice = Person("Alice", 30)
bob = Person("Bob", 25)
print("Example 3:", alice == bob)  # Output: False
print("Example 3:", alice < bob)   # Output: False
print("Example 3:", bob < alice)   # Output: True


# Example 4: Overloading __getitem__, __len__, __str__

class CustomList:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return f"CustomList({self.items})"

# Test

clist = CustomList(["a", "b", "c"])
print("Example 4:", clist[1])     # Output: b
print("Example 4:", len(clist))   # Output: 3
print("Example 4:", clist)        # Output: CustomList(['a', 'b', 'c'])


# Reference: Operator Overloading Methods

# __add__(self, other)         => a + b
# __concat__(self, other)      => seq1 + seq2
# __contains__(self, item)     => item in seq
# __truediv__(self, other)     => a / b
# __floordiv__(self, other)    => a // b
# __and__(self, other)         => a & b
# __xor__(self, other)         => a ^ b
# __invert__(self)             => ~a
# __or__(self, other)          => a | b
# __pow__(self, other)         => a ** b
# __setitem__(self, key, val)  => obj[key] = val
# __delitem__(self, key)       => del obj[key]
# __getitem__(self, key)       => obj[key]
# __lshift__(self, other)      => a << b
# __mod__(self, other)         => a % b
# __mul__(self, other)         => a * b
# __matmul__(self, other)      => a @ b
# __neg__(self)                => -a
# __not__(self)                => not a          #rarely user-defined
# __pos__(self)                => +a
# __rshift__(self, other)      => a >> b
# __setitem__(self, slice, v)  => seq[i:j] = v
# __delitem__(self, slice)     => del seq[i:j]
# __getitem__(self, slice)     => seq[i:j]
# __sub__(self, other)         => a - b
# __bool__(self)               => bool(obj)
# __lt__(self, other)          => a < b
# __le__(self, other)          => a <= b
# __eq__(self, other)          => a == b
# __ne__(self, other)          => a != b
# __ge__(self, other)          => a >= b
# __gt__(self, other)          => a > b

# In-place (augmented) assignment operators:

# __iadd__(self, other)        => a += b
# __iconcat__(self, other)     => seq += seq
# __iand__(self, other)        => a &= b
# __ifloordiv__(self, other)   => a //= b
# __ilshift__(self, other)     => a <<= b
# __irshift__(self, other)     => a >>= b
# __imod__(self, other)        => a %= b
# __imul__(self, other)        => a *= b
# __imatmul__(self, other)     => a @= b
# __ior__(self, other)         => a |= b
# __ipow__(self, other)        => a **= b
# __isub__(self, other)        => a -= b
# __itruediv__(self, other)    => a /= b
# __ixor__(self, other)        => a ^= b

# With these methods, you can define intuitive behavior for custom objects.

