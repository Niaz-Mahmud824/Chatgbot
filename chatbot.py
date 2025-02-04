from flask import Flask, render_template, request, jsonify
import os
import string

app = Flask(__name__)

def preprocess_input(input_text):
    # Remove punctuation and convert to lowercase
    return input_text.translate(str.maketrans('', '', string.punctuation)).strip().lower()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.form["user_message"]
    user_message = preprocess_input(user_message)  # Preprocess the user input
    
    # Using if-elif-else to match user input with predefined questions
    if "what is your name" in user_message:
        response = "My name is Niaz Mahmud."
    elif "where are you from" in user_message:
        response = "I am from Bangladesh."
    elif "what do you do" in user_message:
        response = "I am a software engineer, and I work at SimCorp."
    elif "what is your educational background" in user_message:
        response = "I have a Bachelor's degree in Computer Science and Engineering, and I'm pursuing a Master's in Artificial Intelligence."
    elif "what technologies do you work with" in user_message:
        response = "I work with Python, C#, Azure, APL, and various frameworks like Laravel and Flask."
    elif "what is your favorite programming language" in user_message:
        response = "I love working with Python for its simplicity and flexibility."
    elif "what is your experience with ai" in user_message:
        response = "I am currently studying Artificial Intelligence and have worked with machine learning models in the past."
    elif "what do you do in your free time" in user_message:
        response = "I enjoy competitive programming, reading, and exploring new technologies."
    elif "do you speak any other languages" in user_message:
        response = "Yes, I speak Bengali and English."
    elif "what is your most memorable project" in user_message:
        response = "A real estate website I built using Laravel for my previous company was very memorable."
    elif "how do you approach problem-solving" in user_message:
        response = "I break down the problem, analyze it, and come up with an efficient solution using data structures and algorithms."
    elif "what is your experience with web development" in user_message:
        response = "I have experience in building websites using Laravel, Flask, and JavaScript."
    elif "what is your favorite book" in user_message:
        response = "I enjoy reading technical books as well as novels like '1984' by George Orwell."
    elif "what are your future goals" in user_message:
        response = "I want to continue learning and grow as a software engineer, particularly in the field of AI."
    elif "have you worked with databases" in user_message:
        response = "Yes, I have worked with MySQL, SQL Server, and NoSQL databases like MongoDB."
    elif "what is your experience with cloud platforms" in user_message:
        response = "I have experience with Microsoft Azure for developing and deploying applications."
    elif "do you participate in programming contests" in user_message:
        response = "Yes, I have won multiple national and international programming contests."
    elif "what do you think about open-source projects" in user_message:
        response = "I believe open-source projects are a great way to learn, collaborate, and contribute to the community."
    elif "how do you keep up with new technologies" in user_message:
        response = "I keep up by reading tech blogs, attending conferences, and working on personal projects."
    elif "do you have experience with mobile development" in user_message:
        response = "I have limited experience with mobile development but I'm always interested in learning new things."
    else:
        response = "I'm sorry, I don't understand that."
    
    return jsonify({"reply": response})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's dynamic port
    app.run(debug=True, host="0.0.0.0", port=port)

