# 07_python_advanced/file_io_handling.py


# Basic file writing
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("Hello, file!\n")
    f.write("Second line.\n")

# Appending to a file
with open("example.txt", "a", encoding="utf-8") as f:
    f.write("Appended line.\n")

# Reading entire content
with open("example.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("Full content:")
    print(content)

# Reading line by line
with open("example.txt", "r", encoding="utf-8") as f:
    for line in f:
        print("Line:", line.strip())

# Reading with readline() and readlines()
with open("example.txt", "r") as f:
    first = f.readline()
    all_lines = f.readlines()  # list of lines

# File modes
# "r" = read, "w" = write (overwrite), "a" = append, "x" = create new
# "b" = binary, "+" = read/write
# Use "with" to ensure file is closed automatically

# Binary files
with open("example.bin", "wb") as f:
    f.write(b"binary data \x00\x01")

with open("example.bin", "rb") as f:
    data = f.read()
    print("Binary read:", data)

# File pointer position
with open("example.txt", "r") as f:
    print("Initial position:", f.tell())
    print("First 5 chars:", f.read(5))
    print("After read:", f.tell())
    f.seek(0)
    print("Rewound to:", f.tell())

# Error handling
try:
    with open("nonexistent.txt", "r") as f:
        f.read()
except FileNotFoundError as e:
    print("File not found:", e)

# Writing large files efficiently (chunked)
with open("large_input.txt", "r") as src, open("copy.txt", "w") as dst:
    while True:
        chunk = src.read(1024)
        if not chunk:
            break
        dst.write(chunk)

# Using pathlib for file paths
from pathlib import Path

path = Path("example.txt")
if path.exists():
    print("Size in bytes:", path.stat().st_size)
    print("Absolute path:", path.resolve())

# Creating temporary files
import tempfile

with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
    tmp.write("temp data")
    tmp.seek(0)
    print("Temp content:", tmp.read())
    print("Temp file path:", tmp.name)

# Manually opening with buffering options
import io

with open("buffered.txt", "w", buffering=io.DEFAULT_BUFFER_SIZE) as f:
    f.write("Buffered write.\n")


# Tips

# - Use pathlib for OS-independent paths
# - Always specify encoding="utf-8" for text files
# - Use "with" for safety and context management
# - For big files: use chunked reading (read(size)) or iterate line-by-line
# - Use binary mode for non-text files (.zip, .jpg, etc.)
