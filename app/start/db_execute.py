import sqlite3

def append_user(user_id)  ->  None:
    """Добавляет пользователя в бвзу данных"""
    conn = sqlite3.connect("/home/tor/PycharmProjects/quzi/quiz/db/db_file")
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO user_scores (user_id) VALUES (?)", (user_id,))
    conn.commit()
    conn.close()


