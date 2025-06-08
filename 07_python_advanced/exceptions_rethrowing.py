# 07_python_advanced/exceptions_rethrowing.py

# You can catch an exception, log it, and still re-raise it

# This is useful when you want to do something (like logging) without suppressing the error

def risky_operation():
    # This simulates an unexpected error
    raise ValueError("Unexpected value encountered")

try:
    risky_operation()
except ValueError as e:
    print("Logging error:", e)
    # Re-raise the original exception after handling side-effects
    raise

