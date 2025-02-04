from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.form["user_message"]
    # Here, you can integrate your chatbot logic to process the user message and return a response
    chatbot_reply = "This is the chatbot reply for: " + user_message
    return jsonify({"reply": chatbot_reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's dynamic port
    app.run(debug=True, host="0.0.0.0", port=port)

