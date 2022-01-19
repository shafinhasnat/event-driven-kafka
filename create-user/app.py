from flask import Flask, jsonify, request
from kafka import KafkaProducer
import json

app = Flask(__name__)
producer = KafkaProducer(bootstrap_servers='127.0.0.1:9093', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

@app.route("/")
def home():
    return "OUR MICROSERVICE"

@app.route("/register")
def register():
    payload = request.get_json()
    res = {"Message": "user creation request initiated", "email": payload["email"]}
    producer.send('usertopic', payload)
    producer.flush()
    return jsonify(res)

if __name__ == "__main__":
    app.run(debug=True, port=5001)