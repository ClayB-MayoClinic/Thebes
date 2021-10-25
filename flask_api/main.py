import flask
from flask import request, jsonify
from flask import json
from flask.helpers import flash
import flash_controller
import blog_controller
import uuid
from db import create_tables

app = flask.Flask(__name__)
app.config["DEBUG"] = True

BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'date': '01/01/1970',
        'title': 'On the Road',
        'author': 'Jack Kerouac',
    },
    {
        'id': uuid.uuid4().hex,
        'date': '01/01/1970',
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
    },
    {
        'id': uuid.uuid4().hex,
        'date': '01/01/1970',
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
    }
]

# Books route ****************************************************************
@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'date': post_data.get('date'),
            'title': post_data.get('title'),
            'author': post_data.get('author')
        })
        response_object['message'] = 'Book added!'
    else:
        books = BOOKS
        response_object['books'] = books
    return jsonify(response_object)

@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'date': post_data.get('date'),
            'title': post_data.get('title'),
            'author': post_data.get('author')
        })
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)

def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
        return False

# Blog Post Routes ***********************************************************

@app.route('/blog/posts', methods=['GET', 'POST'])
def all_posts():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        post_date = post_data["post_date"]
        edit_date = post_data["edit_date"]
        location = post_data["location"] 
        author = post_data["author"]
        author_id = post_data["author_id"]
        post_title = post_data["post_title"] 
        post_subtitle = post_data["post_subtitle"]
        post_body = post_data["post_body"]
        post_tags = post_data["post_tags"]
        result = blog_controller.insert_post(post_date, edit_date, location, author, author_id, post_title, post_subtitle, post_body, post_tags)
        response_object['message'] = 'Post Added!'
    else:
        posts = blog_controller.get_posts()
        response_object['posts'] = posts
    return jsonify(response_object)

@app.route("/blog/post/<id>", methods=['PUT', 'DELETE'])
def single_post(id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        post_date = post_data["post_date"]
        edit_date = post_data["edit_date"]
        location = post_data["location"] 
        author = post_data["author"]
        author_id = post_data["author_id"]
        post_title = post_data["post_title"] 
        post_subtitle = post_data["post_subtitle"]
        post_body = post_data["post_body"]
        post_tags = post_data["post_tags"]
        blog_controller.update_post(post_date, edit_date, location, author, author_id, post_title, post_subtitle, post_body, post_tags)
        response_object['message'] = 'Post Updated!'
    if request.method == 'DELETE':
        blog_controller.delete_post(id)
        response_object['message'] = 'Post Removed'
    return jsonify(response_object)

@app.route("/blog/post/<id>", methods=["GET"])
def get_post_by_id(id):
    post = blog_controller.get_by_id(id)
    return jsonify(post)

# Flash Card Routes **********************************************************

@app.route("/flashcards", methods=["GET"])
def get_flashcards():
    cards = flash_controller.get_flashcards()
    return jsonify(cards)

@app.route("/flashcard", methods=["POST"])
def insert_flashcard():
    card_info = request.get_json()
    collection_id = card_info["collection_id"]
    side_a = card_info["sideA"]
    side_b = card_info["sideB"]
    result = flash_controller.insert_flash(collection_id, side_a, side_b)
    return jsonify(result)

@app.route("/flashcard", methods=["PUT"])
def update_flashcard():
    card_info = request.get_json()
    id = card_info["flashcard_id"]
    collection_id = card_info["collection_id"]
    side_a = card_info["sideA"]
    side_b = card_info["sideB"]
    result = flash_controller.update_flash(id, collection_id, side_a, side_b)
    return jsonify(result)

@app.route("/flashcard/<id>", methods=["DELETE"])
def delete_flashcard(id):
    result = flash_controller.delete_flash(id)
    return jsonify(result)

@app.route("/flashcard/<id>", methods=["GET"])
def get_flashcard_by_id(id):
    card = flash_controller.get_by_id(id)
    return jsonify(card)
    
# sanity check route *********************************************************

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

# CORS for localhost *********************************************************

@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*" # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response

if __name__ == "__main__":
    create_tables()
    app.run(host='127.0.0.1', port=8000, debug=False)