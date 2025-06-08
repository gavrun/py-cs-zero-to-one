# 07_python_advanced/sql_sqlite.py

# Using the built-in sqlite3 module.

# SQLite is a lightweight, file-based SQL database included with Python.

import sqlite3


# Example: in-memory SQLite database

# Connect to in-memory database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
''')

# Insert some data
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 30))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Bob', 25))
conn.commit()

# Query data
cursor.execute("SELECT * FROM users WHERE age > ?", (26,))
rows = cursor.fetchall()
print("Users older than 26:")
for row in rows:
    print(row)  # (id, name, age)

# Update data
cursor.execute("UPDATE users SET age = ? WHERE name = ?", (31, 'Alice'))
conn.commit()

# Delete data
cursor.execute("DELETE FROM users WHERE name = ?", ('Bob',))
conn.commit()

# Show all data
cursor.execute("SELECT * FROM users")
all_rows = cursor.fetchall()
print("All users:")
for row in all_rows:
    print(row)

# Close connection
conn.close()


# Example: in-memory SQLite database

# Connect to a file-based SQLite database (creates if not exists)
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Create a table (if not exists)
cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL
)
""")

# Insert a record
cursor.execute("INSERT INTO notes (content) VALUES (?)", ("First note",))
conn.commit()

# Read records
cursor.execute("SELECT id, content FROM notes")
rows = cursor.fetchall()
for row in rows:
    print(f"{row[0]}: {row[1]}")

# Clean up
cursor.close()
conn.close()


# Notes
# - Use ? placeholders for parameters to prevent SQL injection
# - Use context managers or always close connections
# - SQLite is ideal for prototypes and local apps

