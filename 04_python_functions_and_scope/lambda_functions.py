# 04_python_functions_and_scope/lambda_functions.py

# Lambda: small anonymous function (one expression)

# Regular function
def square(x):
    return x * x

# Lambda version
square_lambda = lambda x: x * x
print(square_lambda(5))  # 25

# Lambda with multiple arguments
add = lambda a, b: a + b
print(add(3, 4))  # 7

# Use with sorted()
points = [(2, 3), (1, 5), (4, 1)]
sorted_points = sorted(points, key=lambda p: p[1])
print(sorted_points)  # sort by second element

# Use with map()
nums = [1, 2, 3]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)

# Use with filter()
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
