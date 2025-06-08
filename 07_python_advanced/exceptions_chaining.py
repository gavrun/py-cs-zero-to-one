# 07_python_advanced/exceptions_chaining.py

# Raising a new exception while preserving the original one

# This helps with debugging by keeping the full context of what went wrong

def parse_config():
    try:
        # Try to open a required config file
        with open("config.json") as f:
            return f.read()
    except FileNotFoundError as original_error:
        # Raise a more descriptive error, linking the original cause
        raise RuntimeError("Failed to load configuration") from original_error

try:
    parse_config()
except RuntimeError as e:
    print("Caught:", e)
    print("Original cause:", e.__cause__)

