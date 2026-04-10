import os
from flask import Flask, request, session

app = Flask(__name__)
app.secret_key = "quizapp123"

questions = [
    {"question": "What is the capital of France?", "options": ["London", "Paris", "Berlin", "Madrid"], "answer": "Paris"},
    {"question": "What is 7 x 8?", "options": ["54", "56", "58", "60"], "answer": "56"},
    {"question": "What is the largest planet in the solar system?", "options": ["Earth", "Saturn", "Jupiter", "Neptune"], "answer": "Jupiter"},
    {"question": "Who painted the Mona Lisa?", "options": ["Picasso", "Da Vinci", "Rembrandt", "Monet"], "answer": "Da Vinci"},
    {"question": "What is the capital of Japan?", "options": ["Beijing", "Seoul", "Tokyo", "Bangkok"], "answer": "Tokyo"},
]

@app.route("/")
def home():
    session["score"] = 0
    session["question"] = 0
    return '''
        <h1>General Knowledge Quiz</h1>
        <p>5 questions. Good luck!</p>
        <a href="/quiz">Start Quiz</a>
    '''

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        selected = request.form.get("answer")
        q = questions[session["question"]]
        if selected == q["answer"]:
            session["score"] += 1
        session["question"] += 1

    if session["question"] >= len(questions):
        return f'''
            <h1>Quiz Complete!</h1>
            <p>You scored {session["score"]} out of {len(questions)}</p>
            <a href="/">Play Again</a>
        '''

    q = questions[session["question"]]
    options_html = "".join([f'<br><input type="radio" name="answer" value="{o}"> {o}' for o in q["options"]])

    return f'''
        <h1>Question {session["question"] + 1} of {len(questions)}</h1>
        <p>{q["question"]}</p>
        <form method="POST">
            {options_html}
            <br><br>
            <button type="submit">Next</button>
        </form>
    '''

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)