from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
import os

app = Flask(__name__)

# MongoDB Connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client["testdb"]
collection = db["items"]

# Helper to convert Mongo object to JSON
def serialize_doc(doc):
    doc["_id"] = str(doc["_id"])
    return doc

@app.route("/items", methods=["GET"])
def get_items():
    items = list(collection.find())
    return jsonify([serialize_doc(item) for item in items]), 200

@app.route("/items", methods=["POST"])
def create_item():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    result = collection.insert_one(data)
    return jsonify({"inserted_id": str(result.inserted_id)}), 201

@app.route("/items/<id>", methods=["GET"])
def get_item(id):
    item = collection.find_one({"_id": ObjectId(id)})
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(serialize_doc(item)), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=5000)
