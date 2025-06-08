# 07_python_advanced/variables_scope.py

# Variables Scope in Python

# Python resolves variables using the LEGB rule:
# Local → Enclosing → Global → Built-in

# Understanding scope is critical when dealing with:
# - Closures
# - Mutability
# - Functional patterns
# - State tracking


# 1. Global vs Local Scope

x = 100  # Global

def show_scope():
    x = 10  # Local shadowing
    print("Inside function:", x)

show_scope()
print("Outside function:", x)  # Global x remains unchanged

# Best practice: avoid relying on or modifying global state directly.


# 2. Function returns don't leak local variables

def compute_area(radius):
    pi = 3.14  # Local
    return pi * radius * radius

area = compute_area(5)
# print(pi)  # NameError — pi is not accessible here


# 3. Modifying global state with global keyword


config_version = 1

def upgrade_config():
    global config_version
    config_version += 1

upgrade_config()
print("Config version:", config_version)  # 2

# Note: use of 'global' should be limited to simple module-level configs.


# 4. nonlocal for closures that track or mutate state

def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

c = counter()
print(c())  # 1
print(c())  # 2

# Nonlocal allows enclosed variables to persist between calls.


# 5. Closures with mutable state (without nonlocal)

def make_accumulator():
    state = {"total": 0}

    def add(amount):
        state["total"] += amount
        return state["total"]

    return add

acc = make_accumulator()
print(acc(10))  # 10
print(acc(5))   # 15

# Mutable containers can be used instead of nonlocal in some patterns.


# 6. Shadowing built-in or outer names (bad practice)

def shadow():
    list = "I shadowed the built-in 'list'"
    print(list)
    # print(list([1, 2]))  # Uncommenting this will raise TypeError

shadow()

# Avoid shadowing built-ins like `list`, `dict`, `str`, `sum`, etc.


# 7. Nested scope lookup: LEGB resolution in action

name = "Global"

def outer():
    name = "Enclosing"
    def inner():
        name = "Local"
        print("Inner sees:", name)
    inner()
    print("Outer sees:", name)

outer()
print("Global sees:", name)

# Python checks variables in this order: Local → Enclosing → Global → Built-in


# 8. Function factories and closures remembering state

def make_logger(prefix):
    def log(message):
        print(f"[{prefix}] {message}")
    return log

info = make_logger("INFO")
debug = make_logger("DEBUG")

info("Starting system")   # [INFO] Starting system
debug("x=42")             # [DEBUG] x=42

# The returned functions retain access to the 'prefix' value.


# 9. Scope behavior with comprehensions and loops

squares = [x**2 for x in range(3)]
# print(x)  # NameError: x is not defined (list comp has its own scope)

for i in range(2):
    pass
print(i)  # 'i' is still available here (loop does NOT create a new scope)

# In Python 3, comprehensions have their own scope. Loops — do not.


# 10. Class scope is special — no LEGB for methods

x = "global-x"

class MyClass:
    x = "class-x"
    def method(self):
        # x = "method-x"  # Uncomment to create a method-local variable
        print("x from method:", x)  # Looks up global, not class-level x

obj = MyClass()
obj.method()

# Class body is its own scope, but method scope doesn't include class-level names unless accessed as self.x


# 11. Using closures safely in loops (lambda trap)

funcs = []

for i in range(3):
    funcs.append(lambda: i)

print([f() for f in funcs])  # [2, 2, 2] — all captured same 'i'

# Fix: capture current value using default argument
fixed_funcs = []

for i in range(3):
    fixed_funcs.append(lambda i=i: i)

print([f() for f in fixed_funcs])  # [0, 1, 2]

# This is a common closure gotcha in Python!


# 12. Built-in scope — how far Python looks

def uses_len(x):
    return len(x)  # Resolved from built-in scope

print(uses_len([1, 2, 3]))  # 3

# Built-in names like len, print, range, etc., are last in LEGB resolution
