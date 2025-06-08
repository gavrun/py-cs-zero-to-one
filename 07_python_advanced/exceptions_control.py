# 07_python_advanced/exceptions_control.py

# Using full try/except/else/finally to handle file reading

# Goal: open a file, read its content, and handle all possible issues cleanly

def process_file(path):
    try:
        # Try to open the file
        f = open(path, 'r')
    except FileNotFoundError:
        # File does not exist — handle the error
        print("File not found:", path)
    else:
        try:
            # If file opened successfully, read its content
            data = f.read()
            print("File contents:", data)
        finally:
            # Always close the file if it was opened
            f.close()
            print("File closed.")
    finally:
        # This block always runs, regardless of success or failure
        print("End of file operation block.")

process_file("example.txt")

