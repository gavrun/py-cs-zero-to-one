# 07_python_advanced/context_managers.py

# Context managers handle setup and cleanup using 'with' statement

# Example: working with files
with open("example.txt", "w") as f:
    f.write("Hello, file!")

# File is automatically closed after the block

# Custom context manager using class
class SimpleContext:
    def __enter__(self):
        print("Enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit")

with SimpleContext():
    print("Inside context")

# Custom context manager using contextlib
from contextlib import contextmanager

@contextmanager
def custom_context():
    print("Start")
    yield
    print("End")

with custom_context():
    print("Doing work")

