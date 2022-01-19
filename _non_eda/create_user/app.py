from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

def sendEmail(payload):
    res = requests.post("http://localhost:4001/send-email", json=payload)
    return res.text

def storeInDB(payload):
    res = requests.post("http://localhost:4002/store", json=payload)
    return res.text

@app.route("/")
def test():
    return "NON EDA"

@app.route("/register", methods=["POST"])
def register():
    payload = request.get_json()
    email = sendEmail(payload)
    print("[SEND EMAIL]==> ", email)

    store = storeInDB(payload)
    print("[STORE IN DB]==> ", store)

    res = {"message": "user creation initiated", "email": payload["email"]}
    return jsonify(res)

if __name__ == "__main__":
    app.run(debug=True, port=4000)