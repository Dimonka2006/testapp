import sqlite3

db = sqlite3.connect('itproger.db')

cur = db.cursor() 
# cur.execute(""" CREATE TABLE articles (
#             title TEXT,
#             full_text TEXT,
#             views INTEGER,
#             avtor)
#             """)   # добавление столбцов
# добавление данных
#cur.execute("INSERT INTO articles VALUES ('VK is cool!', 'VK is realy cool', 95, 'Admin+D')")
# удаление данных
#cur.execute("DELETE FROM articles WHERE rowid =2")
# изменение данных
cur.execute("UPDATE articles SET avtor = 'Admin' WHERE title = 'VK is cool!'" )
# выборка данных
cur.execute("SELECT rowid, title FROM articles WHERE rowid < 5 ORDER BY views DESC")
items = cur.fetchall()
#print(cur.fetchall()) # вывод в строку
#print(cur.fetchmany(2)) # кол-во записей списком
#print(cur.fetchone()[1]) # кортеж
for item in items:
    print(items)
db.commit()

db.close()
