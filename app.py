from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

answer_dict = {
                "1": ["Chess"],
                "2": ["France"],
        }

words = [
    {
        "inputs": 5,
        "category": "Sports",
        "word": 'Chess',
        "word_id": "1"
    },
    {
        "inputs": 6,
        "category": "European Country Name",
        "word": 'France',
        "word_id": "2"
    },
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-words")
def get_word():
    return jsonify({
        "status": "success",
        "word": random.choice(words)
    })

@app.route("/post-answers", methods=["POST"])
def post_answers():
    word_id = request.json.get("word_id")
    values = request.json.get("values")
    answers = answer_dict.get(word_id)
    index, score = 0, 0
    while index < len(values):
        if values[index].lower() == answers[index].lower():
            score += 1
        index += 1
    return jsonify({
        "status": "success",
        "result": f"{score} / {len(values)}"
    })

if __name__ == "__main__":
    app.run(debug=True)