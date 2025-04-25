import sqlite3

def get_random_question()  -> list:
    """возращает рандомный вопрос и ответ в види list()"""
    conn = sqlite3.connect("/home/tor/PycharmProjects/quzi/quiz/db/db_file")
    cur = conn.cursor()
    cur.execute("SELECT * FROM questions ORDER BY RANDOM() LIMIT 1")
    random_user = cur.fetchone()

    conn.close()
    print(random_user)
    return list(random_user)


