import sqlite3

def creation():
    conn = sqlite3.connect("db_file")
    cur = conn.cursor()
    cur.execute("CREATE TABLE questions (question CHAR(255),answer CHAR(255))")
    cur.close()

creation()