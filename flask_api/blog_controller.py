from db import db_connection

def insert_post(post_date, edit_date, location, author, author_id, post_title, post_subtitle, post_body, post_tags):
    db = db_connection()
    cursor = db.cursor()
    statement = "INSERT INTO blogs(post_date, edit_date, location, author, author_id, post_title, post_subtitle, post_body, post_tags) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(statement, [post_date, edit_date, location, author, author_id, post_title, post_subtitle, post_body, post_tags])
    db.commit()

def update_post(post_id, post_date, edit_date, location, author, author_id, post_title, post_subtitle, post_body, post_tags):
    db = db_connection()
    cursor = db.cursor()
    statement = "UPDATE blogs SET post_date = ?, edit_date = ?, location = ?, author = ?, author_id = ?, post_title = ?, post_subtitle = ?, post_body = ? post_tags = ? WHERE id = ?"
    cursor.execute(statement, [post_date, edit_date, location, author, author_id, post_title, post_subtitle, post_body, post_tags, post_id])
    db.commit()

def delete_post(post_id):
    db = db_connection()
    cursor = db.cursor()
    statement = "DELETE FROM blogs WHERE id = ?"
    cursor.execute(statement, [post_id])
    db.commit()

def get_by_id(post_id):
    db = db_connection()
    cursor = db.cursor()
    statement = "SELECT * FROM blogs WHERE id = ?"
    cursor.execute(statement, [post_id])
    return cursor.fetchone()

def get_posts():
    db = db_connection()
    cursor = db.cursor()
    query = "SELECT * FROM blogs"
    cursor.execute(query)
    return cursor.fetchall()
