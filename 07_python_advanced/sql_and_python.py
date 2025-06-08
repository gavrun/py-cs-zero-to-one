# 07_python_advanced/sql_and_python.py

# SQL and Python — 

# Overview of capabilities and ecosystem support

# Python supports working with relational databases through:
# 1. DB-API 2.0 (standard interface for SQL backends)
# 2. Native drivers for specific engines (PostgreSQL, MySQL, etc.)
# 3. ORMs like SQLAlchemy
# 4. Tools for migrations, testing, and query building


# Python can:

# - Connect to almost any SQL database (via drivers or ORMs)
# - Execute raw SQL queries
# - Use prepared statements to avoid SQL injection
# - Fetch and process result sets (rows, columns)
# - Handle transactions (commit, rollback)
# - Interact with stored procedures
# - Reflect or introspect schema metadata
# - Generate SQL dynamically (query builders, ORMs)
# - Work with in-memory databases (e.g. SQLite)
# - Support typed results (with named tuples or dataclasses)

# Access Methods

# 1. DB-API 2.0 — low-level access

#   Supported by:
#     - sqlite3 (builtin)
#     - psycopg2 (PostgreSQL)
#     - mysql-connector-python / PyMySQL (MySQL)
#     - pyodbc (MS SQL, Oracle via ODBC)
#     - ibm_db (IBM DB2)
#   Typical usage:
#     - connect()
#     - cursor.execute(...)
#     - cursor.fetchall()
#     - connection.commit()
#     - context managers (with ...)

# 2. ORMs and DSLs

#   - SQLAlchemy: ORM and Core DSL (database-agnostic)
#   - peewee: lightweight ORM
#   - Tortoise ORM: async ORM
#   - Django ORM: tightly coupled to Django framework

# 3. Async support

#   - asyncpg (PostgreSQL)
#   - databases (async wrapper for SQLAlchemy core)
#   - Tortoise ORM (fully async)
#   - AioSQLite (async SQLite)

# 4. Query builders

#   - SQLModel (by FastAPI author, uses SQLAlchemy under the hood)
#   - PyPika
#   - records (thin wrapper for executing SQL)

# 5. Migration tools

#   - Alembic (for SQLAlchemy)
#   - yoyo-migrations
#   - Django's built-in migration system
#   - Flyway / Liquibase (external tools, often used with Python projects)


# Best Practices

# - Use parameterized queries (e.g., "WHERE id = ?") to avoid SQL injection
# - Always close cursors and connections (or use `with`)
# - Use transactions to ensure consistency
# - Separate SQL from business logic where possible
# - Avoid ORM magic for critical performance sections — profile and benchmark

# Development Tips

# - Use SQLite in-memory DB for fast unit tests
# - Use factory functions or DI to abstract database access
# - Use logging to debug raw SQL and bindings
# - Tools like DBVisualizer / DBeaver / pgAdmin help debug from outside

