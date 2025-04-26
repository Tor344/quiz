import sqlite3

def get_point_user(user_id) -> int:
    """Возвращает очки пльзователя если он сущестывует"""
    conn = sqlite3.connect("/home/tor/PycharmProjects/quzi/quiz/db/db_file")
    cur = conn.cursor()

    cur.execute("""
        SELECT COALESCE(
            (SELECT score FROM user_scores WHERE user_id = ?),
            0
        ) as score
    """, (user_id,))
    score = cur.fetchone()[0]
    conn.close()
    return score