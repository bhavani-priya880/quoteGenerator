from flask import Flask, jsonify
from flask_cors import CORS
from datasets import load_dataset
import random

# Initialize Flask
app = Flask(__name__)
CORS(app)  # Enable CORS after app is created

# Load dataset from Hugging Face
dataset = load_dataset("asuender/motivational-quotes", "quotes")

# Extract all quotes into a list of dicts (quote + author)
quotes = []
for item in dataset['train']:
    quotes.append({
        "quote": item["quote"],
        "author": item.get("author", "Unknown")  # some may not have author
    })

# Root route
@app.route("/")
def home():
    return "Flask Quotes API is running! Go to /quote to get a random quote."

# Random quote route
@app.route("/quote")
def get_quote():
    return jsonify(random.choice(quotes))

if __name__ == "__main__":
    app.run(debug=True, port=5001)
