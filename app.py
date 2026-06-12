# app.py
# Flask backend for SafeRoute
# Connects your graph algorithm to the frontend

from flask import Flask, request, jsonify, render_template
from graph import city_graph, find_safest_path

app = Flask(__name__)


@app.route("/")
def home():
    # TODO: render your index.html template
    # Hint: return render_template("index.html")
    pass


@app.route("/route", methods=["POST"])
def get_route():
    # TODO: 
    #   1. Get "start" and "end" from the request (request.json)
    #   2. Call find_safest_path() with those values
    #   3. Return the result as JSON
    pass


@app.route("/chat", methods=["POST"])
def chat():
    # TODO (Sunday): AI safety companion goes here
    pass


if __name__ == "__main__":
    app.run(debug=True)
