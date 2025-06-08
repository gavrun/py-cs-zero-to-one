# 04_python_functions_and_scope/nested_functions.py

# Nested Function Scopes in Python

# Demonstrate how variable scope works with nested functions.

# Examples LEGB rule, closures, and the use of nonlocal/global keywords.


# 1. Inner functions access outer variables (read-only)

def outer_1():
    message = "Hello from outer"
    
    def inner():
        # Accessing outer scope variable (read-only)
        print(message)
    
    inner()

outer_1()


# 2. Inner functions can't assign to outer variables unless 'nonlocal' is used

def outer_2():
    count = 0
    
    def inner():
        # count += 1  # UnboundLocalError without 'nonlocal'
        nonlocal count
        count += 1
    
    inner()
    print("Count is:", count)

outer_2()


# 3. Closures — returning a nested function that remembers outer state

def make_multiplier(factor):
    def multiply(number):
        return number * factor  # 'factor' is captured from outer scope
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print("Double 5:", double(5))  # 10
print("Triple 5:", triple(5))  # 15


# 4. Global keyword — modifying global variables from inside a nested function

counter = 0

def outer_3():
    def inner():
        global counter
        counter += 1
    
    inner()

outer_3()
print("Global counter:", counter)  # 1


# 5. Each function call gets its own scope

def outer_4():
    x = 10
    def inner():
        return x
    return inner

f1 = outer_4()
f2 = outer_4()
print("f1():", f1())  # 10
print("f2():", f2())  # 10


# 6. Functions defined in different scopes do not share state

def outer_5():
    x = 0
    def inner():
        return x
    return inner

a = outer_5()
b = outer_5()

print("a is b:", a is b)  # False — separate function objects


# 7. Modifying mutable outer variable (e.g., list) without nonlocal

def outer_6():
    data = []
    def inner():
        # Modifying mutable object in outer scope (allowed)
        data.append(1)
    inner()
    print("Data:", data)

outer_6()


# 8. Trying to shadow outer scope variable leads to confusion if not handled properly

def outer_7():
    value = "outer"
    def inner():
        value = "inner"  # This is a new local variable, not the outer one
        print("Inner value:", value)
    inner()
    print("Outer value:", value)

outer_7()

