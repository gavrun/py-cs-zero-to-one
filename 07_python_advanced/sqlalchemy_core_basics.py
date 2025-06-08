# 07_python_advanced/sqlalchemy_core_basics.py


# SQLAlchemy Core (not ORM) — powerful SQL toolkit, engine-agnostic.
# Build and execute SQL using Python objects
# Tables and statements are fully composable
# Unlike ORM, Core gives you full control of SQL structure

# Works with many databases: SQLite, PostgreSQL, MySQL, MSSQL, Oracle

# pip install sqlalchemy

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, insert, select, update, delete


# Create an SQLite engine (also works with PostgreSQL, MySQL, etc.)
engine = create_engine("sqlite:///example.db", echo=False)
metadata = MetaData()

# Define a table
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("age", Integer)
)

# Create the table in the database (if not exists)
metadata.create_all(engine)

# Insert data
with engine.connect() as conn:
    conn.execute(insert(users).values(name="Alice", age=30))
    conn.execute(insert(users), [
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35}
    ])

# Select data
with engine.connect() as conn:
    result = conn.execute(select(users))
    for row in result:
        print(f"{row.id}: {row.name}, {row.age}")

# Update data
with engine.connect() as conn:
    stmt = update(users).where(users.c.name == "Alice").values(age=31)
    conn.execute(stmt)

# Delete data
with engine.connect() as conn:
    stmt = delete(users).where(users.c.name == "Bob")
    conn.execute(stmt)

# Select with condition
with engine.connect() as conn:
    stmt = select(users).where(users.c.age > 30)
    result = conn.execute(stmt)
    print("Age > 30:")
    for row in result:
        print(row)


# Tips:

# - Use engine.begin() for transactional blocks
# - Use echo=True for debug logging
# - Use SQL expressions instead of string SQL
# - Prefer Core for performance-sensitive or raw-query control
    
