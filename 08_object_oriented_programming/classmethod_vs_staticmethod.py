# 08_object_oriented_programming/classmethod_vs_staticmethod.py

# Class Methods vs Static Methods in Python

# - @classmethod takes cls as first argument and can modify class state
# - @staticmethod behaves like a regular function, just namespaced in the class


# 1. Instance Method — gets self

class Book:
    def __init__(self, title):
        self.title = title

    def describe(self):
        print(f"Instance method: Book title is '{self.title}'")

b = Book("1984")
b.describe()


# 2. Class Method — gets cls, not self
# Useful for factory methods or accessing class-level data

class Dog:
    species = "Canis lupus familiaris"

    def __init__(self, name):
        self.name = name

    @classmethod
    def common_species(cls):
        return cls.species

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"])

print("Dog species:", Dog.common_species())
d1 = Dog.from_dict({"name": "Buddy"})
print("Dog name:", d1.name)


# 3. Static Method — no self or cls
# Use when the method doesn't depend on instance or class

class Math:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(n):
        return n % 2 == 0

print("Add:", Math.add(5, 7))
print("Is even:", Math.is_even(10))


# Use Cases:
# - @staticmethod: utility methods that conceptually belong to class
# - @classmethod: alternative constructors or modifying class-level state
# - instance method: default for behavior tied to object state
