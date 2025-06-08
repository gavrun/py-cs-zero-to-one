# 08_object_oriented_programming/inheritance.py

# Inheritance in Python

# Inheritance allows one class (child/subclass) to inherit the attributes and methods
# of another class (parent/superclass), promoting code reuse and organization.

# - Use inheritance to share behavior across related classes
# - Override methods to specialize child behavior
# - Use super() to extend base functionality
# - Check types with isinstance/issubclass when needed
# - Prefer composition over complex multiple inheritance


# 1. Basic Inheritance and Method Overriding

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + " makes a sound")

class Dog(Animal):
    def speak(self):  # Override base class method
        print(self.name + " says woof")

class Cat(Animal):
    def speak(self):  # Override base class method
        print(self.name + " says meow")

# Creating instances
creature = Animal("Creature")
d = Dog("Rex")
c = Cat("Whiskers")

creature.speak()  # Creature makes a sound
d.speak()         # Rex says woof
c.speak()         # Whiskers says meow


# 2. isinstance and issubclass checks

print(isinstance(d, Animal))   # True
print(isinstance(c, Dog))      # False
print(issubclass(Dog, Animal)) # True
print(issubclass(Cat, Dog))    # False


# 3. Using super() to call parent methods

class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)  # Call parent constructor
        self.can_fly = can_fly

    def speak(self):
        super().speak()  # Call base class speak
        print("And also chirps")

b = Bird("Parrot", True)
b.speak()


# 4. Multiple inheritance (use with care)

class Flyer:
    def fly(self):
        print("I can fly")

class Swimmer:
    def swim(self):
        print("I can swim")

class Duck(Animal, Flyer, Swimmer):
    def speak(self):
        print(self.name + " says quack")

duck = Duck("Donald")
duck.speak()
duck.fly()
duck.swim()



