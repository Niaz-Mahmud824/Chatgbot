from flask import Flask, request, jsonify, send_from_directory

import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return ("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use the port from Render's environment
    app.run(debug=True, host="0.0.0.0", port=port)


# Serve the frontend interface
@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"reply": "I didn't get that. Could you please repeat?"})

    if "hello" in user_message.lower():
        return jsonify({"reply": "Hi there! How can I assist you today?"})
    else:
        return jsonify({"reply": "I'm just a simple bot for now. Ask me something simple!"})

if __name__ == "__main__":
    app.run(debug=True)
