# What to do

I would recommend reading this in its entirey once before you get started just so you have an idea of the plan ahead, and what you are allowed to do (i.e. basically anything you want that gets the job done). There may be some unfamiliar tools used in here, and it is expected you use the internet to help you. I have already imported some useful libraries for you, but I imagine you will want to include 1 more library at a minimum, and perhaps more depending on how you choose to implement this.

## Part 1: Setting up the quiz data

For the first part, you will be importing data from an Excel file (I've converted it to a CSV file for your convenience, but you can do this as you wish) into an SQL database. You will be working in `instance/init_db.py`.

You need to:

* tweak the `create_table` function to create a table appropriate to store the questions and corresponding answers to the quiz questions.

    * While not required, if you have time, try to implement this so that your system would work for questions with an unknown number of answers, where there may even be more than one correct answer. Reminder: not required, but if you have time. Otherwise, please writeup how you think you might do so. [This may be of use to you](https://www.sqlitetutorial.net/sqlite-autoincrement/).

* Complete the `fill_table` function to insert the data into your database. Feel free to use any of the code provided above to help you, or other packages you are comfortable with (e.g. `pandas`) if you find them useful.

## Part 2: Setting up the quiz page

Now we need to make sure our questions and answers are actually used by the website, and are in some way an actually interactive quiz. You will now be working with `app.py`, `quiz.html` and `script.js`.

* In `app.py` you will modify the `/quiz` route/the `quiz` function. You will connect to the database and get a **random** question and answer set from your database. You will then pass them to the `quiz` template, as per the example provided. You should ensure that the correct answer isn't always the first one. You could do this now (perhaps by passing something like `correct_answer`, `incorrect_answers` to the template, and shuffling them in there, or using some other method, e.g. tuple, dictionaries etc). You may find [this](https://docs.python.org/3/library/sqlite3.html) useful to you, along with Google if there's any parts of this you are struggling to work out how to implement.

* You may want to modify the code in `quiz.html` to indicate whether an answer is correct or not, which may make your Javascript easier to write, depending on how you implement the next step. The language used by Flask templates is called Jinja/jinja2, as you may want to quickly look up some syntax (e.g. you may want to use if statements.)

* Finally, in `script.js`, implement a system that will notify the user that their answer is correct. This can be via an alert, changing the color of answers, inserting a message into the DOM or anything you'd like. You may have a system from the previous steps that labels the DOM elements to make this easier, or maybe you want to call the backend to check whether an answer is right if you didn't label anything in the DOM.

## Part 3: documentation/cleanup

This shouldn't be its own section, but this is more of a reminder to make sure you keep your code reasonably tidy and well-documented. I've documented just enough so that hopefully everything is clear, but you can certainly do a better job. Feel free to refactor/cleanup or modify any of the code provided to you.

## Part 4: Personal Touch

If you have finished the previous sections within a reasonable amount of time, you should implement a small personal adjustment to this project. Some ideas could be: improving the styling of the `quiz` page, adding a score element to the page to keep track of how many questions you've answered correctly this session, buttons to get a new question once you've answer a question correctly or something of similar scope. Feel free to be creative, but again this is not meant to be large-scale or particulary time-consuming to implement (please spend no more than 30 mins on this).
