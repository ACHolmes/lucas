# Import Flask (might not need all of these functions, but in case they're helpful)
from flask import Flask, render_template, redirect, url_for, jsonify
import sqlite3 
import random

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
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()

        # Get all the data
        question_data = cur.execute("SELECT * FROM questions ORDER BY RANDOM() LIMIT 1").fetchone()
        
        # Extract information
        question = question_data[0]
        answer = question_data[1]
        incorrect_answers = list(filter(lambda x: x != '', question_data[2:]))
        all_answers = [(answer, True)] + [(ans, False) for ans in incorrect_answers]
        
        # Randomly shuffle the answers, while storing info for which one is correct
        random.shuffle(all_answers)

        # Send to template
        return render_template("quiz.html", question=question, answers=all_answers)


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