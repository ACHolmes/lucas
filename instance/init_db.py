import sqlite3
import csv

DB_PATH = "data.db"
CSV_PATH = "questions.csv"

# Here's some example code which you can use to help you

def example_csv():
    print("One option: ")
    with open(CSV_PATH) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            print(row)
    
    print("\nAnother option: ")
    with open(CSV_PATH) as csvfile:
        dictreader = csv.DictReader(csvfile, delimiter=",")
        print(dictreader.fieldnames)
        for row in dictreader:
            print(row)

'''
Creates an example table to store questions.
TODO: Update this function to create table(s) to store your question and answer data.

'''
def create_table():
    # Connect to the database (con = connection)
    with sqlite3.connect(DB_PATH) as con:
        # Create a cursor (something to actually modify the databse)
        cur = con.cursor()
        
        # Doing this a much more sensible way, storing questions and answers separately
        cur.execute("""
                        CREATE TABLE IF NOT EXISTS questions (
                            question_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            question VARCHAR(1000)
                        )
                    """)
        # Commit those changes over the connection
        con.commit()

        # Create a table that stores answers and links them to question ids
        # so that we can have unlimited answers per question, and multiple
        # correct answers
        cur.execute("""
                CREATE TABLE IF NOT EXISTS answers (
                    answer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    question_id INTEGER,
                    answer VARCHAR(1000),
                    correct BOOL
                )
            """)
        con.commit()

# Clears all data from table
def clear_table():
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        cur.execute("""
                        DELETE FROM questions
                    """)
        con.commit()

# Helper function to see what's in your table
def see_table():
    print("-----Questions data-----")
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        results = cur.execute("""
                                SELECT * FROM questions
                              """).fetchall()
        for res in results:
            print(res)

        results = cur.execute("""
                                SELECT * FROM answers
                              """).fetchall()
        for res in results:
            print(res)

'''
TODO: Complete the fill_table function to store all the question data.
How you store the data in the database is up to you, but will depend
on how you decide to setup your table in create_table.
'''
def fill_table():
    with sqlite3.connect(DB_PATH) as con:
        with open(CSV_PATH, "r") as csvfile:
            dictreader = csv.DictReader(csvfile, delimiter = ',')
            for q in dictreader:
                cur = con.cursor()
                
                # Insert the question
                cur.execute("""
                                INSERT INTO questions (question) VALUES (?)
                            """,                    (q["Question"], ))
                con.commit()

                id = cur.execute("SELECT question_id FROM questions WHERE question = ?",
                                 (q["Question"], )).fetchone()[0]

                # Insert correct answer
                cur.execute("""
                                INSERT INTO answers (question_id, answer, correct) 
                                            VALUES  (?, ?, ?)
                            """, (id, q["Correct"], True, ))
                con.commit()

                # Insert all incorrect answers
                for k, v in q.items():
                    if not(k == "Correct" or k == "Question" or v==""):
                        cur.execute("""
                                INSERT INTO answers (question_id, answer, correct) 
                                            VALUES  (?, ?, ?)
                            """, (id, v, False))
                        con.commit()

if __name__ == "__main__":
    create_table()
    clear_table()
    fill_table()
    # You can comment see_table out when happy.
    # see_table()