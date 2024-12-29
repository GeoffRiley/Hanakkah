import sqlite3
from sqlite3 import Error


class Database:
    def __init__(self, db_file):
        """Initialize the database connection."""
        self.conn = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            if not db_file:
                db_file = "/home/geoffr/dev/Hanakkah/data/5784/noahs.sqlite"
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(e)
        return conn

    def create_table(self, create_table_sql):
        """Create a table from the create_table_sql statement."""
        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def create(self, table, data):
        """Create a new row in the table."""
        keys = ", ".join(data.keys())
        question_marks = ", ".join(["?"] * len(data))
        values = tuple(data.values())
        sql = f"INSERT INTO {table} ({keys}) VALUES ({question_marks})"
        cur = self.conn.cursor()
        cur.execute(sql, values)
        self.conn.commit()
        return cur.lastrowid

    def read(self, table, row_id):
        """Query a row by id."""
        cur = self.conn.cursor()
        cur.execute(f"SELECT * FROM {table} WHERE id=?", (row_id,))
        return cur.fetchone()

    def update(self, table, row_id, data):
        """Update a row by id."""
        keys = ", ".join([f"{k}=?" for k in data.keys()])
        values = tuple(data.values()) + (row_id,)
        sql = f"UPDATE {table} SET {keys} WHERE id=?"
        cur = self.conn.cursor()
        cur.execute(sql, values)
        self.conn.commit()

    def delete(self, table, row_id):
        """Delete a row by id."""
        sql = f"DELETE FROM {table} WHERE id=?"
        cur = self.conn.cursor()
        cur.execute(sql, (row_id,))
        self.conn.commit()


# Example usage:
if __name__ == "__main__":
    database = Database("/path/to/your/database.db")

    create_table_sql = """
    CREATE TABLE IF NOT EXISTS users (
        id integer PRIMARY KEY,
        name text NOT NULL,
        age integer
    );
    """
    database.create_table(create_table_sql)

    # Create a new user
    user_id = database.create("users", {"name": "John Doe", "age": 30})

    # Read user data
    user = database.read("users", user_id)
    print(user)

    # Update user data
    database.update("users", user_id, {"name": "Jane Doe", "age": 25})

    # Delete user
    database.delete("users", user_id)
