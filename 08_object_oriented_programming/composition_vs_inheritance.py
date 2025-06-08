# 08_object_oriented_programming/composition_vs_inheritance.py

# Inheritance: "is-a" relationship
class Engine:
    def start(self):
        print("Engine started")

class Car(Engine):  # Car *is an* Engine
    def drive(self):
        print("Car is driving")

my_car = Car()
my_car.start()  # inherited
my_car.drive()

# Composition: "has-a" relationship
class Engine:
    def start(self):
        print("Engine started")

class Vehicle:
    def __init__(self):
        self.engine = Engine()  # Vehicle *has an* Engine

    def drive(self):
        self.engine.start()
        print("Vehicle is moving")

v = Vehicle()
v.drive()

# Use inheritance when subclass is a specialized form of the parent
# Use composition when building complex behavior from simpler parts

