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
        # Run an SQL command
        cur.execute("""
                        CREATE TABLE IF NOT EXISTS questions (
                            question VARCHAR(1000),
                            correct VARCHAR(1000),
                            incorrect VARCHAR(1000)
                        )
                    """)
        # Commit those changes over the connection
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

'''
TODO: Complete the fill_table function to store all the question data.
How you store the data in the database is up to you, but will depend
on how you decide to setup your table in create_table.
'''
def fill_table():
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        cur.execute("""
                        INSERT INTO questions (question, correct, incorrect) VALUES (?, ?, ?)
                    """, ("When will Rick Astley give you up?", "Never", "Sometime"))
        con.commit()

if __name__ == "__main__":
    create_table()
    clear_table()
    fill_table()
    # You can comment see_table out when happy.
    see_table()