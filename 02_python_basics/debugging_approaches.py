# 02_python_basics/debugging_approaches.py

# Basic debugging approaches in Python


# 1. Print statements

def buggy_func(x):
    print(f"Input: {x}")
    result = x + 1
    print(f"Result: {result}")
    return result

buggy_func(5)


# 2. Using assert for sanity checks

def divide_with_assert(a, b):
    assert b != 0, "Denominator cannot be zero"
    return a / b

print(divide_with_assert(10, 2))
# print(divide_with_assert(10, 0))  # AssertionError


# 3. Using try-except blocks to catch errors

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: division by zero")
        return None

print(safe_divide(10, 0))


# 4. Using built-in debugger (pdb)

# Uncomment below to run debugger on this function
# import pdb
# def buggy_sum(a, b):
#     pdb.set_trace()  # breakpoint
#     return a + b
# buggy_sum(2, 3)


# 5. Using IDE or editor integrated debugging tools (breakpoints, step execution)


# 6. Fail Fast (early termination)

def load_config_or_fail(path):
    import os
    if not os.path.exists(path):
        raise FileNotFoundError(f"Critical: Config file '{path}' is missing. Exiting.")
    with open(path) as f:
        return f.read()

# Try with existing or missing file
# config = load_config_or_fail("config.json")
# print(config)


# 7. Graceful Degradation (fallback strategy)

def connect_to_service_or_fallback():
    try:
        # Simulate connection error
        raise ConnectionError("Service unreachable")
    except ConnectionError as e:
        print("Could not connect to service. Falling back to cached data.")
        return {"data": "cached fallback"}

data = connect_to_service_or_fallback()
print("Data received:", data)


# Debugging tips:
# - Start simple: print, asserts
# - Break code into small steps
# - Run code often and test small pieces
# - Handle exceptions gracefully
# - Use pdb or IDE debugger for step-by-step inspection
# - Fail fast if a critical component is missing
# - Gracefully degrade when external dependencies fail
