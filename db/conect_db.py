import psycopg2

from .. config.settings import host, user, db_name, password

def conect():
    try:
        conection = psycopg2.connect(host=host,
                                     user=user,
                                     password=password,
                                     database=db_name)
    except Exception as ex:
        print("ex")