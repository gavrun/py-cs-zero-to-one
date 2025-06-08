# 01_cs_concepts/abstraction_of_storage_beyond_ram.py

# Storage beyond RAM: files, databases, and persistence concepts

# RAM is volatile; data lost when power off
# Persistent storage keeps data across sessions

# Example: Writing and reading a file (persistent storage)

data = "Hello, persistent storage!"

# Write to file
with open("example.txt", "w") as f:
    f.write(data)

# Read from file
with open("example.txt", "r") as f:
    content = f.read()

print("Read from file:", content)

# Simple key-value storage using JSON (simulates a tiny database)
import json

store = {"user1": {"name": "Alice", "age": 30}, "user2": {"name": "Bob", "age": 25}}

# Save to disk
with open("store.json", "w") as f:
    json.dump(store, f)

# Load from disk
with open("store.json", "r") as f:
    loaded_store = json.load(f)

print("Loaded store:", loaded_store)


# Abstract data storage:
# - Files (text, binary)
# - Databases (SQL, NoSQL)
# - Object storage (cloud services)


# Python's sqlite3 module provides a lightweight database interface

import sqlite3

conn = sqlite3.connect(":memory:")  # In-memory database (RAM)

cursor = conn.cursor()
cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("Users in DB:", rows)

conn.close()

