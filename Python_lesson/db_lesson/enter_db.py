import sqlite3

# connect - сздает соединение с БД, создает ее и соединяет нас с ней
with sqlite3.connect('test.db') as con:
    cur = con.cursor() # cursor() - создает обект через который будет идти взаимодействие
    # execute - выполняет SQL запрос
    cur.execute(''' CREATE TABLE IF NOT EXISTS users( 
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                adress TEXT)
                ''')
    # cur.execute('''DROP TABLE users''')  # - удаляет данные из табл