# 07_python_advanced/exceptions_context_manager.py

# Creating a context manager that handles exceptions during file usage

# Allows for safe resource cleanup and optional error inspection

class SafeFile:
    def __init__(self, path):
        self.path = path
        self.file = None

    def __enter__(self):
        # Open the file and return it
        self.file = open(self.path, 'r')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Always close the file, even if an exception occurred
        if self.file:
            self.file.close()
            print("File closed safely.")
        if exc_type:
            # Log or handle the exception here
            print("Exception occurred during file operation:", exc_type.__name__)
        return False  # False means re-raise the exception outside

try:
    with SafeFile("missing.txt") as f:
        print(f.read())
except Exception as e:
    print("Handled outside context manager:", e)

