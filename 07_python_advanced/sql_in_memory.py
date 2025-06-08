# 07_python_advanced/sql_in_memory.py

# Abstract SQL-like in-memory database in Python

from typing import List, Dict, Any, Callable


class Table:
    def __init__(self, name: str, columns: List[str]):
        # Store table name and column definitions
        self.name = name
        self.columns = columns
        self.rows: List[Dict[str, Any]] = []

    def insert(self, values: Dict[str, Any]):
        # Validate and insert a row
        if not all(col in self.columns for col in values):
            raise ValueError("Invalid column in insert data")
        self.rows.append(values)

    def select(self, where: Callable[[Dict[str, Any]], bool] = lambda row: True) -> List[Dict[str, Any]]:
        # Return all rows that match the where condition
        return [row for row in self.rows if where(row)]

    def __str__(self):
        # Pretty print for debugging
        lines = [f"TABLE: {self.name}"]
        lines.append(" | ".join(self.columns))
        for row in self.rows:
            lines.append(" | ".join(str(row.get(col, "")) for col in self.columns))
        return "\n".join(lines)


class Database:
    def __init__(self):
        # Dictionary to hold tables by name
        self.tables: Dict[str, Table] = {}

    def create_table(self, name: str, columns: List[str]):
        # Create and register a new table
        if name in self.tables:
            raise ValueError(f"Table '{name}' already exists.")
        self.tables[name] = Table(name, columns)

    def insert_into(self, table_name: str, values: Dict[str, Any]):
        # Insert row into specified table
        self.tables[table_name].insert(values)

    def select_from(self, table_name: str, where: Callable[[Dict[str, Any]], bool] = lambda row: True) -> List[Dict[str, Any]]:
        # Query rows from specified table
        return self.tables[table_name].select(where)

    def show_table(self, table_name: str):
        # Print table contents
        print(self.tables[table_name])


# TEST: Demonstrate usage of the SQL-like in-memory database

if __name__ == "__main__":
    # Initialize database
    db = Database()
    print("\n=== Connected (Initialized) ===")

    # Create a table with columns
    db.create_table("users", ["id", "name", "age"])

    # Insert sample data
    db.insert_into("users", {"id": 1, "name": "Alice", "age": 30})
    db.insert_into("users", {"id": 2, "name": "Bob", "age": 25})
    db.insert_into("users", {"id": 3, "name": "Charlie", "age": 35})

    # Show full table
    print("\n=== Full Users Table ===")
    db.show_table("users")

    # Simple SELECT: users older than 28
    print("\n=== Users older than 28 ===")
    results = db.select_from("users", where=lambda row: row["age"] > 28)
    for row in results:
        print(row)

    # SELECT with specific name
    print("\n=== User with name 'Bob' ===")
    results = db.select_from("users", where=lambda row: row["name"] == "Bob")
    for row in results:
        print(row)

    print("\n=== Disconnected (Finalized) ===")

