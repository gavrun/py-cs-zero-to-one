# 07_python_advanced/decorators.py

# Decorators: functions that modify other functions

def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function
# Hello!
# After function

# Decorator with arguments
def repeat(n):
    def decorator(func):
        def wrapper():
            for _ in range(n):
                func()
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hi!")

greet()  # prints "Hi!" three times

