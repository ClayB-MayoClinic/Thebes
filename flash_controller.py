from db import db_connection

def insert_flash(collection_id, sideA, sideB):
    db = db_connection()
    cursor = db.cursor()
    statement = "INSERT INTO flashcard(collection_id, sideA, sideB) VALUES (?, ?, ?)"
    cursor.execute(statement, [collection_id, sideA, sideB])
    db.commit()

def update_flash(flashcard_id, collection_id, sideA, sideB):
    db = db_connection()
    cursor = db.cursor()
    statement = "UPDATE flashcard SET collection_id = ?, sideA = ?, sideB = ? WHERE id = ?"
    cursor.execute(statement, [collection_id, sideA, sideB, flashcard_id])
    db.commit()

def delete_flash(flashcard_id):
    db = db_connection()
    cursor = db.cursor()
    statement = "DELETE FROM flashcard WHERE id = ?"
    cursor.execute(statement, [flashcard_id])
    db.commit()

def get_by_id(flashcard_id):
    db = db_connection()
    cursor = db.cursor()
    statement = "SELECT id, collection_id, sideA, sideB FROM flashcard WHERE id = ?"
    cursor.execute(statement, [flashcard_id])
    return cursor.fetchone()

def get_flashcards():
    db = db_connection()
    cursor = db.cursor()
    query = "SELECT id, collection_id, sideA, sideB FROM flashcard"
    cursor.execute(query)
    return cursor.fetchall()
