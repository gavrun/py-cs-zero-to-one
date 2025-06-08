# 08_object_oriented_programming/dunder_methods.py

# Dunder methods = "double underscore" methods (special behavior)

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' with {self.pages} pages"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return self.title == other.title and self.pages == other.pages

# Create books
b1 = Book("Python 101", 300)
b2 = Book("Python 101", 300)
b3 = Book("Data Structures", 400)

print(str(b1))       # 'Python 101' with 300 pages
print(len(b1))       # 300
print(b1 == b2)      # True
print(b1 == b3)      # False

# Common dunder methods:
# __init__    -> constructor
# __str__     -> string representation
# __len__     -> used by len()
# __eq__      -> used by ==
# __repr__    -> detailed string (optional)


