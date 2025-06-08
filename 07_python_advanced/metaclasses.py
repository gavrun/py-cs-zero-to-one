# 07_python_advanced/metaclasses.py

# Metaclass controls creation of classes and does not related to OOP itself but rather meta programming 

class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)

# Use Meta as metaclass for a class
class MyClass(metaclass=Meta):
    pass

# Instantiating the class
obj = MyClass()

# Output:
# Creating class MyClass

# Metaclasses can modify class attributes or behavior at creation time

