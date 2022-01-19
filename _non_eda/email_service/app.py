from crypt import methods
from flask import Flask, request
import time

app = Flask(__name__)

@app.route("/send-email", methods=["POST"])
def email():
    payload = request.get_json()
    try:
        print("Sending email to: " + payload["email"])
        time.sleep(1)
        print("Email sent to : " + payload["email"])
        return "Email sent to : " + payload["email"]
    except:
        print("errrrrroooorrr")
        return "error"

if __name__ == "__main__":
    app.run(debug=True, port=4001)