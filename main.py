import flask
from flask import request, jsonify
from flask.helpers import flash
import flash_controller
from db import create_tables

app = flask.Flask(__name__)
app.config["DEBUG"] = True

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