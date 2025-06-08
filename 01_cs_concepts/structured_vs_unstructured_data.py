# 01_cs_concepts/structured_vs_unstructured_data.py

# Structured vs Unstructured Data

# Structured data: organized, fixed schema (tables, CSV, JSON with fixed keys)
structured_data = [
    {"id": 1, "name": "Alice", "age": 30},
    {"id": 2, "name": "Bob", "age": 25},
]

# Access structured data easily
for record in structured_data:
    print(f"Name: {record['name']}, Age: {record['age']}")

# Unstructured data: raw text, images, audio, etc.
unstructured_data = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Praesent vehicula magna at dui commodo, a posuere nulla dictum.
"""

# Processing unstructured text data example: count words
words = unstructured_data.split()
word_count = len(words)
print("Word count in unstructured text:", word_count)

# JSON can hold structured or semi-structured data
import json

json_str = json.dumps(structured_data)
print("JSON string:", json_str)

# Semi-structured data example: JSON with varying keys
semi_structured_data = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "age": 25},
]

print("Semi-structured data:", semi_structured_data)

