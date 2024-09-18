import sqlite3

# connect - сздает соединение с БД, создает ее и соединяет нас с ней
with sqlite3.connect('test2.db') as con:
    cur = con.cursor() # cursor() - создает обект через который будет идти взаимодействие
    # execute - выполняет SQL запрос
    cur.execute(''' CREATE TABLE IF NOT EXISTS users( 
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                FName TEXT NOT NULL,
                Doljnost TEXT NOT NULL,
                ORab INTEGER NOT NULL,
                ZP INTEGER
                )
                ''')
    res = cur.execute('''SELECT * FROM users''')
    #print(res.fetchmany(5))
    for worker in res.fetchmany(5): # вывели список 
        print(worker)