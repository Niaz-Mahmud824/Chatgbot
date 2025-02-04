from flask import Flask, request, jsonify, send_from_directory

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, chatbot is working!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)



# Serve the frontend interface
@app.route("/")
def index():
    print("Home page accessed")
    return send_from_directory(".", "index.html")

@app.route("/chat", methods=["POST"])
def chat():
    print("Received message")  # Check if this triggers when you send a message
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"reply": "I didn't get that. Could you please repeat?"})

    if "hello" in user_message.lower():
        return jsonify({"reply": "Hi there! How can I assist you today?"})
    else:
        return jsonify({"reply": "I'm just a simple bot for now. Ask me something simple!"})

if __name__ == "__main__":
    print("Starting Flask app...")  # Added to verify if app is starting
    app.run(debug=True)
