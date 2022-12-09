import sqlite3

DATABASE_NAME = "sply.db"

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def create_table():
    tables = [
            """CREATE TABLE IF NOT EXISTS
                tbl_user(
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nama VARCHAR NOT NULL,
                    nis int NOT NULL,
                    password VARCHAR NOT NULL,
                    role VARCHAR NOT NULL)""" 
        ]
    
    db = get_db()
    cursor = db.cursor()
    
    for table in tables:
        cursor.execute(table)