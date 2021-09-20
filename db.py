import sqlite3
from sqlite3 import Error

DATABASE_NAME = "flash.db"

def db_connection():
    try:
        con = sqlite3.connect('claypi.db')
        return con
    except Error:
        print(Error)

def create_tables():
    tables = [
        "CREATE TABLE IF NOT EXISTS flashcard(id INTEGER PRIMARY KEY, collection_id INTEGER, sideA TEXT, sideB TEXT)"
    ]
    db = db_connection()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)