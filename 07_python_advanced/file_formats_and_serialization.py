# 07_python_advanced/file_formats_and_serialization.py


# TEXT (plain text I/O)
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("Line 1\nLine 2\n")

with open("example.txt", "r", encoding="utf-8") as f:
    for line in f:
        print("Text line:", line.strip())


# JSON (human-readable structured data)
import json

data = {'name': 'Alice', 'age': 30, 'items': [1, 2, 3]}

# Serialize to JSON string
json_str = json.dumps(data)  # str
print("JSON string:", json_str)

# Deserialize JSON string
data_back = json.loads(json_str)
print("From JSON string:", data_back)

# Write JSON to file
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

# Read JSON from file
with open('data.json', 'r', encoding='utf-8') as f:
    loaded = json.load(f)
print("From file:", loaded)


# CSV (comma-separated values)
import csv

rows = [
    ["name", "age"],
    ["Alice", 30],
    ["Bob", 25],
]

# Write CSV
with open("people.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

# Read CSV
with open("people.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print("CSV row:", row)

# Using DictReader/DictWriter
with open("people_dict.csv", "w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerow({"name": "Charlie", "age": 40})

with open("people_dict.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print("CSV dict row:", row)


# XML (structured hierarchical text)
import xml.etree.ElementTree as ET

# Create XML
root = ET.Element("people")
ET.SubElement(root, "person", name="Alice", age="30")
ET.SubElement(root, "person", name="Bob", age="25")
tree = ET.ElementTree(root)
tree.write("people.xml")

# Parse XML
tree = ET.parse("people.xml")
root = tree.getroot()
for person in root:
    print("XML person:", person.attrib)


# Binary files
binary_data = b"\x00\x01ABC"

with open("example.bin", "wb") as f:
    f.write(binary_data)

with open("example.bin", "rb") as f:
    read_bytes = f.read()
    print("Binary read:", read_bytes)

# Pickle (Python object serialization - binary format)
import pickle

obj = {"name": "Alice", "items": [1, 2, 3]}

# Serialize to bytes
p_bytes = pickle.dumps(obj)
# Deserialize
p_obj = pickle.loads(p_bytes)

# Write to file
with open("data.pkl", "wb") as f:
    pickle.dump(obj, f)

# Read from file
with open("data.pkl", "rb") as f:
    loaded_obj = pickle.load(f)

print("Pickle:", loaded_obj)

# Shelve (persistent dict-like object)
import shelve

with shelve.open("store.db") as db:
    db["user"] = {"name": "Bob", "score": 42}
    print("Shelved:", db["user"])

# Shelve persists across runs like a key-value store


# Practical use cases

# JSON     → APIs, configs, data exchange
# CSV      → spreadsheets, simple tables
# XML      → legacy formats, some APIs
# pickle   → quick local object storage (not safe for untrusted input)
# shelve   → simple key-value storage across sessions
# binary   → image/audio/custom byte formats


# Tips

# - Use json for portable, safe data exchange
# - Avoid pickle for untrusted input (it's executable!)
# - Always use newline='' when writing CSV on Windows
# - For large binary data: read/write in chunks
