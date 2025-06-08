# 03_python_control_structures/match_case.py

# Pattern Matching (match-case)

# Match with primitive literals

def print_hello(language):
    match language:
        case "russian":
            print("Привет")
        case "english":
            print("Hello")
        case "german":
            print("Hallo")
        case _:
            print("Undefined")

print_hello("english")      # Hello
print_hello("german")       # Hallo
print_hello("spanish")      # Undefined


# Match multiple values in a single case

def print_hello_variant(language):
    match language:
        case "american english" | "british english" | "english":
            print("Hello")
        case "russian":
            print("Привет")
        case _:
            print("Undefined")


# Match integers and perform actions

def operation(a, b, code):
    match code:
        case 1:
            return a + b
        case 2:
            return a - b
        case 3:
            return a * b
        case _:
            return 0

print(operation(10, 5, 1))  # 15
print(operation(10, 5, 2))  # 5
print(operation(10, 5, 3))  # 50
print(operation(10, 5, 4))  # 0


# Match with tuple unpacking

def describe_point(point):
    match point:
        case (0, 0):
            return "Origin"
        case (0, y):
            return f"Y={y}"
        case (x, 0):
            return f"X={x}"
        case (x, y):
            return f"X={x}, Y={y}"

print(describe_point((0, 0)))   # Origin
print(describe_point((5, 0)))   # X=5
print(describe_point((0, 3)))   # Y=3
print(describe_point((4, 2)))   # X=4, Y=2


# Match with list/sequence patterns

def match_sequence(seq):
    match seq:
        case [first, second]:
            print(f"Two elements: {first}, {second}")
        case [first, *rest]:
            print(f"Head: {first}, Tail: {rest}")
        case []:
            print("Empty list")
        case _:
            print("Unknown format")

match_sequence([1, 2])       # Two elements: 1, 2
match_sequence([1, 2, 3])    # Head: 1, Tail: [2, 3]
match_sequence([])          # Empty list


# Match with dictionaries

def match_dict(d):
    match d:
        case {"type": "user", "name": name}:
            print(f"User: {name}")
        case {"type": "admin", "level": level}:
            print(f"Admin level: {level}")
        case _:
            print("Unknown object")

match_dict({"type": "user", "name": "Alice"})   # User: Alice
match_dict({"type": "admin", "level": 3})        # Admin level: 3


# Match with custom classes and attribute patterns

class Point:
    __match_args__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

def match_point(p):
    match p:
        case Point(x=0, y=0):
            return "Origin"
        case Point(x, y):
            return f"Point({x}, {y})"

p = Point(0, 0)
print(match_point(p))            # Origin
print(match_point(Point(3, 4)))  # Point(3, 4)


# Using guards (if conditions) in match-case

def process_value(x):
    match x:
        case int(n) if n > 0:
            print("Positive integer")
        case int(n) if n < 0:
            print("Negative integer")
        case int():
            print("Zero")
        case _:
            print("Not an integer")

process_value(5)     # Positive integer
process_value(-3)    # Negative integer
process_value(0)     # Zero
process_value("hi")  # Not an integer
