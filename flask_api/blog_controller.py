import json
import collections
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

    rows = cursor.fetchall()

    rowarray_list = []
    for row in rows: 
        t = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
        rowarray_list.append(t)
    
    j = json.dumps(rowarray_list)

    with open ('blog_rowarrays.js', 'w') as f:
        f.write(j)

    # Convert query to objects of key-value pairs
    objects_list = []
    for row in rows:
        d = collections.OrderedDict()
        d['post_id'] = row[0] 
        d['post_date'] = row[1]
        d['edit_date'] = row[2] 
        d['location'] = row[3] 
        d['author'] = row[4] 
        d['author_id'] = row[5] 
        d['post_title'] = row[6] 
        d['post_subtitle'] = row[7] 
        d['post_body'] = row[8] 
        d['post_tags'] = row[9]
        objects_list.append(d)

    j = json.dumps(objects_list)

    with open('blog_objects.js', 'w') as f:
        f.write(j)
    
    return j


        


