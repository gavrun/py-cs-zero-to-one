# 07_python_advanced/descriptors.py

# Descriptor example: custom attribute access

class Descriptor:
    def __init__(self):
        self.value = None

    def __get__(self, instance, owner):
        print("Getting value")
        return self.value

    def __set__(self, instance, value):
        print("Setting value")
        self.value = value

    def __delete__(self, instance):
        print("Deleting value")
        del self.value

class MyClass:
    attr = Descriptor()

obj = MyClass()
obj.attr = 10       # Setting value
print(obj.attr)     # Getting value -> 10
del obj.attr        # Deleting value

