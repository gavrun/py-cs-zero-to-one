# 08_object_oriented_programming/abstract_classes.py

# Abstract Classes and Methods in Python (using abc)

import abc

# What are abstract classes?
# An abstract class is a class that cannot be instantiated directly.
# It defines common interface via abstract methods that must be implemented
# by concrete subclasses. Python uses module 'abc' to define these.


# Example 1: Defining an abstract base class

class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        """Return area of the shape"""
        pass

    @abc.abstractmethod
    def perimeter(self):
        """Return perimeter of the shape"""
        pass

# Trying to instantiate Shape will raise a TypeError:
# shape = Shape()  # TypeError: Can't instantiate abstract class Shape with abstract methods ...


# Example 2: Implementing abstract methods in subclasses

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Test instantiation and usage
shapes = [
    Rectangle(3, 4),
    Circle(5)
]

for s in shapes:
    print(f"{s.__class__.__name__}: area = {s.area():.2f}, perimeter = {s.perimeter():.2f}")


# Example 3: Enforcing interface with abstractmethod decorator

class Animal(abc.ABC):
    @abc.abstractmethod
    def speak(self):
        """Animal must implement speak()"""
        pass

# class Dog(Animal):
#     pass
# dog = Dog()  # TypeError: Can't instantiate Dog with abstract methods speak

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Test
animals = [Dog(), Cat()]
for a in animals:
    print(f"{a.__class__.__name__} says: {a.speak()}")



# - Abstract classes cannot be instantiated until all abstract methods are overridden.
# - Use @abstractmethod to mark methods that must be defined in subclasses.
# - Abstract classes can include concrete methods too.
# - Use abc.ABC as a base class for abstract classes in Python.

# Reference

# Pattern:
# class Name(abc.ABC):
#     @abc.abstractmethod
#     def method(self, ...):
#         pass
#
# Concrete subclass must define all abstract methods.
# Attempt to instantiate incomplete subclass ➜ TypeError


