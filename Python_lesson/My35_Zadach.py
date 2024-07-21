# По данному примеру модифицировать задачу с библиотекой так чтобы сконвертировать 
# данный csv файл с файл базы данных и написать функции для поиска книг по базе данных
# https://github.com/asg0182/simple-db/tree/main

# import sqlite3
# import csv

# def open_db():
# # Создание подключения к базе данных
#     conn = sqlite3.connect('books.db')
#     cur = conn.cursor()
# #def great_table(): 
# # Создаем таблицу для хранения данных
#     cur.execute('''CREATE TABLE IF NOT EXISTS books (
#          title TEXT,
#          author TEXT,
#          genre TEXT,
#          height INTEGER,
#          publisher TEXT
#          )''')
# #def open_csv():
#     # Открытие файла CSV
#     with open('books.csv', newline='') as f:
#         reader = csv.DictReader(f, fieldnames=['Title', 'Author', 'Genre', 'Height', 'Publisher'])

#             # Проходим по каждой строке CSV файла и записываем данные в таблицу
#         for row in reader:
#             cur.execute("INSERT INTO books VALUES (?, ?, ?, ?, ?)", (row['Title'], row['Author'], row['Genre'], row['Height'], row['Publisher']))

#         # Сохраняем изменения в базе данных
#             conn.commit()
#         # Закрываем соединение с базой данных
#             conn.close()

import sqlite3
import csv

def save_csv_to_sqlite(csv_filepath, db_filepath):
    # Открытие файла CSV
    with open(csv_filepath, newline='') as csvfile:
        reader = csv.reader(csvfile)
        # Создание подключения к базе данных
        conn = sqlite3.connect(db_filepath)
        cur = conn.cursor()
        # Создаем таблицу для хранения данных
        cur.execute('''CREATE TABLE IF NOT EXISTS books (
            title TEXT,
            author TEXT,
            genre TEXT,
            height INTEGER,
            publisher TEXT
        )''')
        # Проходим по каждой строке CSV файла и записываем данные в таблицу
        next(reader)  # Пропускаем заголовок CSV файла
        for row in reader:
            cur.execute("INSERT INTO books VALUES (?, ?, ?, ?, ?)", row)
        # Сохраняем изменения в базе данных
        conn.commit()
        # Закрываем соединение с базой данных
        conn.close()
save_csv_to_sqlite('books.csv', 'books.db')
