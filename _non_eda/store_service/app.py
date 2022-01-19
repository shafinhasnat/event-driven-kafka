from flask import Flask, jsonify, request
import pymongo

app = Flask(__name__)

mongoClient = pymongo.MongoClient("mongodb://localhost:27017")
db = mongoClient["eda"]
collection = db["user"]

@app.route("/store", methods=["POST"])
def store():
    paylad = request.get_json()
    collection.insert_one(paylad)
    res = {"Message": "Data inserted in db", "email": paylad["email"]}
    print(res)
    return jsonify(res)

if __name__ == "__main__":
    app.run(debug=True, port=4002)