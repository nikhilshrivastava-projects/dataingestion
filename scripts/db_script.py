import sqlite3

class Database:
    def create_db():
        conn = sqlite3.connect('data_1.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER,
                    date TEXT)''')
        cursor.execute("INSERT INTO users (id, name, age, date) VALUES (1, 'John Doe', 29, '2023-09-28')")
        cursor.execute("INSERT INTO users (id, name, age, date) VALUES (2, 'Jane Smith', 34, '2023-09-27')")
        cursor.execute("INSERT INTO users (id, name, age, date) VALUES (3, 'Mary Johnson', 25, '2023-09-26')")
        conn.commit()
        conn.close()
        print("db_script executed")

