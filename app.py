import os
from flask import Flask, jsonify
from flask_cors import CORS
from datasets import load_dataset
import random

app = Flask(__name__)
CORS(app)

# Load dataset once at startup
dataset = load_dataset("asuender/motivational-quotes", "quotes")

quotes = []
for item in dataset['train']:
    quotes.append({
        "quote": item["quote"],
        "author": item.get("author", "Unknown")
    })

@app.route("/")
def home():
    return "Flask Quotes API is running! Go to /quote to get a random quote."

@app.route("/quote")
def get_quote():
    return jsonify(random.choice(quotes))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's assigned port
    app.run(host="0.0.0.0", port=port, debug=True)  # Set host to 0.0.0.0 for public access
