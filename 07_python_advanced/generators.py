# 07_python_advanced/generators.py

# Generators: functions that yield values one at a time using yield

def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

# Create generator object
gen = count_up_to(5)

# Get values using next()
print(next(gen))  # 1
print(next(gen))  # 2

# Or use in a loop
for num in count_up_to(3):
    print(num)  # 1 2 3

# Generator expressions (like list comprehensions, but lazy)
squares = (x * x for x in range(5))
for val in squares:
    print(val)

# Generators use less memory for large sequences

# one more example

def generator_func():
    i = 1
    print("First")
    yield i

    print("Second")
    i += 1
    yield i

    print("Third")
    i += 1
    yield i

gen = generator_func()

print(next(gen))  # Runs to first yield, prints "First", outputs 1
print(next(gen))  # Resumes, prints "Second", outputs 2
print(next(gen))  # Resumes, prints "Third", outputs 3

# If you call next(gen) again now, StopIteration is raised
try:
    print(next(gen))
except StopIteration:
    print("Generator exhausted")

