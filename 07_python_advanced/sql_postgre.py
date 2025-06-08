# 07_python_advanced/sql_postgre.py


# PostgreSQL and Python using psycopg2 (sync driver)

# pip install psycopg2-binary

import psycopg2
from psycopg2 import sql

# Connect to a PostgreSQL database
conn = psycopg2.connect(
    dbname="mydb",
    user="myuser",
    password="secret",
    host="localhost",
    port=5432
)

cur = conn.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
)
""")
conn.commit()

# Insert data (parameterized!)
cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Alice", 30))
conn.commit()

# Select data
cur.execute("SELECT id, name, age FROM users WHERE age > %s", (25,))
rows = cur.fetchall()

for row in rows:
    print(f"User {row[0]}: {row[1]}, age {row[2]}")

# Update
cur.execute("UPDATE users SET age = age + 1 WHERE name = %s", ("Alice",))
conn.commit()

# Delete
cur.execute("DELETE FROM users WHERE age < %s", (18,))
conn.commit()

# Safe dynamic SQL using sql.SQL
table = sql.Identifier("users")
column = sql.Identifier("name")
cur.execute(
    sql.SQL("SELECT {col} FROM {tbl}").format(col=column, tbl=table)
)
print("Names:", cur.fetchall())

# Transactions
try:
    cur.execute("BEGIN")
    cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Bob", 22))
    cur.execute("UPDATE users SET age = age + 5 WHERE name = %s", ("Bob",))
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Transaction failed:", e)

# Close connections
cur.close()
conn.close()

