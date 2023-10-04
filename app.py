# Import Flask (might not need all of these functions, but in case they're helpful)
from flask import Flask, render_template, redirect, url_for, jsonify
import sqlite3 

# Flask setup
app = Flask(__name__)

DB_PATH = "instance/data.db"

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with index() function.
def index():
    return render_template("index.html")

@app.route('/quiz')
def quiz():
    question = "What is the answer to life, the universe and everything?"
    answers = [21, 42, 420, 1973]
    return render_template("quiz.html", question=question, answers=answers)


# A route in case you want to check answers by making a request
# to the backend from your JS and having the backend check
# against the database and send some info back to the frontend
# that it can use to determine whether an answer is correct.
@app.route('/check_answer')
def check_answer():
    pass


# Run the app
if __name__ == '__main__':
    app.run()
