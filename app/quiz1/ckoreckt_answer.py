def text_ckoreckt(user_answer,answer):
    if len(user_answer) != len(answer):
        return False
    return sum(a != b for a, b in zip(user_answer, answer)) <= 2