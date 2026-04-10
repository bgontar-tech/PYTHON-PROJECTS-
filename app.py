import os
from flask import Flask, request

app = Flask(__name__)

answer = 50

@app.route("/")
def home():
    return '''
        <h1>Guess a number between 1 and 50</h1>
        <form action="/guess" method="post">
            <input type="number" name="guess">
            <button type="submit">Guess</button>
        </form>
    '''

@app.route("/guess", methods=["POST"])
def guess():
    user_guess = int(request.form["guess"])
    if user_guess < answer:
        return "<p>Too low!</p><a href='/'>Try again</a>"
    elif user_guess > answer:
        return "<p>Too high!</p><a href='/'>Try again</a>"
    else:
        return "<p>Correct!</p>"

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)