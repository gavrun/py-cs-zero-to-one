# 07_python_advanced/reflection.py

# Reflection: inspecting objects at runtime

class Example:
    def __init__(self, x):
        self.x = x

    def method(self):
        return self.x * 2

obj = Example(10)

# Get attributes and methods
print(dir(obj))

# Access attribute by name string
attr_name = 'x'
print(getattr(obj, attr_name))  # 10

# Set attribute by name string
setattr(obj, 'x', 20)
print(obj.x)  # 20

# Check if object has attribute/method
print(hasattr(obj, 'method'))  # True
print(hasattr(obj, 'missing')) # False

# Call method by name string
method = getattr(obj, 'method')
print(method())  # 40

# Get type of object
print(type(obj))

# Inspect function parameters (requires inspect module)
import inspect
sig = inspect.signature(obj.method)
print(sig)  # () -- no parameters other than self

