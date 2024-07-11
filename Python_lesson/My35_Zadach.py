# По данному примеру модифицировать задачу с библиотекой так чтобы сконвертировать 
# данный csv файл с файл базы данных и написать функции для поиска книг по базе данных
# https://github.com/asg0182/simple-db/tree/main

import sqlite3
import csv

# Создание подключения к базе данных
conn = sqlite3.connect('books.db')
cur = conn.cursor()

# Создаем таблицу для хранения данных
cur.execute('''CREATE TABLE IF NOT EXISTS books (
    title TEXT,
    author TEXT,
    genre TEXT,
    height INTEGER,
    publisher TEXT
)''')

# Открытие файла CSV
with open('books.csv', newline='') as f:
    reader = csv.DictReader(f, fieldnames=['Title', 'Author', 'Genre', 'Height', 'Publisher'])

    # Проходим по каждой строке CSV файла и записываем данные в таблицу
    for row in reader:
        cur.execute("INSERT INTO books VALUES (?, ?, ?, ?, ?)", (row['Title'], row['Author'], row['Genre'], row['Height'], row['Publisher']))

# Сохраняем изменения в базе данных
conn.commit()

# Закрываем соединение с базой данных
conn.close()
