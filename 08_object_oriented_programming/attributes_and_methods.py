# 08_object_oriented_programming/attributes_and_methods.py

# Attributes and Methods in Python Classes

# Attributes hold data; methods are functions bound to objects.
# Python distinguishes between class-level and instance-level attributes.

# - Class attributes are shared; instance attributes are per-object.
# - Use instance attributes for state, class attributes for constants/configs.
# - Methods can use both via self or ClassName.
# - Avoid adding dynamic attributes unless intentional.
# - Use __dict__ to debug object state.


# 1. Defining Class and Instance Attributes

class Circle:
    pi = 3.14159  # class attribute: shared by all instances

    def __init__(self, radius):
        self.radius = radius  # instance attribute: unique to each instance

    def area(self):
        return Circle.pi * self.radius ** 2

    def perimeter(self):
        return 2 * Circle.pi * self.radius


# 2. Creating Instances and Calling Methods

c1 = Circle(3)
c2 = Circle(5)

print("Area c1:", c1.area())         # 28.27431
print("Perimeter c2:", c2.perimeter())  # 31.4159


# 3. Accessing Attributes

print("c1 radius:", c1.radius)   # 3
print("Circle.pi:", Circle.pi)   # Access class attribute directly
print("c2.pi:", c2.pi)           # Also accessible via instance (not recommended)


# 4. Modifying Attributes

# Changing class attribute via class affects all (unless shadowed)
Circle.pi = 3.14
print("New area c1:", c1.area())  # 28.26

# Overriding class attribute at instance level (shadowing)
c2.pi = 3.1416
print("Custom area c2:", c2.pi * c2.radius ** 2)  # uses overridden pi


# 5. Dynamic Attribute Assignment (flexible but risky)

c1.color = "blue"  # Adding new attribute at runtime
print("c1 color:", c1.color)

# This does not exist for c2
# print(c2.color)  # AttributeError

# You can inspect all attributes
print("c1.__dict__:", c1.__dict__)

