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


def up_point(user_id) -> None:
    """прибавляет пользователю очко если он существует"""
    conn = sqlite3.connect("/home/tor/PycharmProjects/quzi/quiz/db/db_file")
    cur = conn.cursor()
    # Сначала проверяем, есть ли пользователь
    cur.execute("SELECT 1 FROM user_scores WHERE user_id = ?", (user_id,))
    exists = cur.fetchone()

    if exists:
        cur.execute("UPDATE user_scores SET score = score + 1 WHERE user_id = ?", (user_id,))
    else:
        cur.execute("INSERT INTO user_scores (user_id, score) VALUES (?, 1)", (user_id,))

    conn.commit()
    conn.close()

