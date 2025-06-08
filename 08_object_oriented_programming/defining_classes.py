# 08_object_oriented_programming/defining_classes.py

# Defining Classes in Python 


# 1. Minimal class definition

class Person:
    pass

# Create an object (instance)
p1 = Person()
p1.name = "Alice"
p1.age = 30

print(p1.name, p1.age)  # Output: Alice 30

# Note: This manual assignment is not ideal for structured code.


# 2. Using the constructor (__init__)

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def speak(self):
        print(f"{self.name} says woof!")

# Create instances
d1 = Dog("Rex", "Labrador")
d2 = Dog("Max", "Poodle")

print(d1.name, d1.breed)
d2.speak()


# 3. Default values in the constructor

class Car:
    def __init__(self, make, year=2020):
        self.make = make
        self.year = year

car1 = Car("Toyota")
car2 = Car("Ford", 2018)

print(car1.make, car1.year)  # Toyota 2020
print(car2.make, car2.year)  # Ford 2018


# 4. Instance attributes vs class attributes

class Circle:
    pi = 3.14159  # class attribute (shared by all instances)

    def __init__(self, radius):
        self.radius = radius  # instance attribute

    def area(self):
        return Circle.pi * self.radius ** 2

c = Circle(5)
print("Area:", c.area())  # Output: 78.53975


# 5. Method that uses self

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

c = Counter()
c.increment()
c.increment()
print("Count:", c.count)  # 2


# 6. __str__ method for readable output

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

b = Book("1984", "George Orwell")
print(b)  # 1984 by George Orwell


# 7. Type annotations in class definitions (optional but recommended)

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

p = Product("Keyboard", 49.99)
print(p.name, p.price)


# 8. __del__ method (destructor) — rarely used

class Temp:
    def __init__(self):
        print("Created Temp object")

    def __del__(self):
        print("Deleted Temp object")

t = Temp()
del t  # May call __del__ immediately — or maybe later, or never

# Note:
# - __del__ is Python's destructor, called when an object is garbage collected.
# - In practice, it's rarely used because destruction time is not guaranteed.
# - Use context managers (__enter__/__exit__) for managing external resources.


