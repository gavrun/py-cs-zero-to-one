# 07_python_advanced/exceptions_info_traceback.py

# Extracting Detailed Information from Exceptions in Python

import traceback
import sys


# Example 1: Basic structure using 'as'

try:
    1 / 0
except ZeroDivisionError as e:
    print("Example 1: Caught exception object")
    print("type(e):", type(e))            # <class 'ZeroDivisionError'>
    print("str(e):", str(e))              # division by zero
    print("repr(e):", repr(e))            # ZeroDivisionError('division by zero')


# Example 2: Accessing traceback details

try:
    x = [1, 2, 3]
    print(x[5])
except IndexError as e:
    print("\nExample 2: Accessing traceback via sys.exc_info()")
    exc_type, exc_value, exc_tb = sys.exc_info()
    print("exc_type:", exc_type)          # <class 'IndexError'>
    print("exc_value:", exc_value)        # list index out of range
    print("exc_tb:", exc_tb)              # traceback object
    print("Traceback (most recent call last):")
    traceback.print_tb(exc_tb)


# Example 3: Full traceback + exception in string form

def failing_func():
    return 10 / 0

try:
    failing_func()
except Exception as e:
    print("\nExample 3: Full formatted traceback + exception")
    tb_str = traceback.format_exc()
    print(tb_str)


# Example 4: Using traceback.TracebackException (for structured access)

try:
    {}['missing']
except KeyError as e:
    print("Example 4: Structured access with TracebackException")
    tb_exc = traceback.TracebackException.from_exception(e)
    print("Exception type:", tb_exc.exc_type.__name__)
    print("Exception message:", ''.join(tb_exc.format_exception_only()).strip())
    print("Call stack:")
    for line in tb_exc.format(chain=False):
        print(line.strip())


# Example 5: Capturing stack trace manually

def dummy():
    traceback.print_stack()

print("\nExample 5: Current call stack (no exception)")
dummy()


# Exception info access methods

# try:
#     ...
# except SomeError as e:
#     type(e)             -> Exception class
#     str(e)              -> Error message
#     repr(e)             -> Full exception object representation
#     sys.exc_info()      -> (type, value, traceback)
#     traceback.print_tb(tb)             -> Prints traceback object
#     traceback.format_exc()             -> Returns full traceback as string
#     traceback.TracebackException       -> Structured access to traceback

# Optional: Exception groups (Python 3.11+)
# from exceptions import ExceptionGroup

