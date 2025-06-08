# 07_python_advanced/debugging_approaches_advanced.py

# 1. Graceful Degradation (e.g. external service fails)

def fetch_user_profile(user_id):
    try:
        # simulate external call failure
        raise TimeoutError("Request to profile service timed out")
    except TimeoutError as e:
        print("Could not fetch live profile. Using default guest profile.")
        return {"name": "Guest", "role": "visitor"}

profile = fetch_user_profile(42)
print("[1] Profile loaded:", profile)


# 2. Logging errors instead of printing

import logging

# Configure logging to file
logging.basicConfig(
    filename='app_advanced.log',
    level=logging.ERROR,
    format='%(asctime)s %(levelname)s: %(message)s'
)

def risky_operation():
    try:
        x = 1 / 0
    except ZeroDivisionError as e:
        logging.error("Division by zero in risky_operation: %s", e)
        print("[2] Something went wrong. Error logged.")

risky_operation()


# 3. Input validation before use

def process_age_input(age_str):
    if not age_str.isdigit():
        raise ValueError("Age must be a number")
    age = int(age_str)
    if not (0 <= age <= 120):
        raise ValueError("Age must be between 0 and 120")
    return age

try:
    age = process_age_input("25")
    print("[3] Validated age:", age)
except ValueError as e:
    print("Invalid input:", e)

# Uncomment this to test failure cases:
# process_age_input("abc")
# process_age_input("-5")


# 4. Resource Cleanup with context manager

def read_file_safely(path):
    try:
        with open(path, "r") as f:
            content = f.read()
            print("[4] File content read successfully.")
            return content
    except FileNotFoundError:
        print("[4] File not found. Please check the path.")
        return None

# Test with a real or missing file
file_data = read_file_safely("nonexistent.txt")

