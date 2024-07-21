import sqlite3

def kill_duble_book():
    print('killing')      

     # Открываем соединение с базой данных
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()

    # Читаем все записи из таблицы в список
    cursor.execute("SELECT  *  FROM books")
    records = cursor.fetchall()
    
        # Проверяем каждую запись на наличие дубликатов
    unique_records = []
    for record in records:
        title, author, genre, height, publisher = record
        if (title, author, genre, height, publisher) not in unique_records:
            unique_records.append((title, author, genre, height, publisher))

    # Удаляем дубликаты из списка
    unique_records = list(set(unique_records))
    print(list(set(unique_records)))

#    # Записываем уникальные записи обратно в базу данных
    cursor.executemany("INSERT OR REPLACE INTO books VALUES (?, ?, ?, ?, ?)", unique_records)
    conn.commit()

    # Закрываем соединение с базой данных
    conn.close()

    

# Открываем соединение с базой данных
    # conn = sqlite3.connect('books.db')
    # cursor = conn.cursor()

    # # Читаем все записи из таблицы в список
    # cursor.execute("SELECT Title FROM books GROUP BY Title HAVING count( * ) > 1")
    # titles = cursor.fetchall()

    # # Проверяем каждую запись на наличие дубликатов
    # unique_titles = []
    # for title in titles:
    #     if title[0] not in unique_titles:
    #         unique_titles.append(title[0])

    # # Удаляем дубликаты из списка
    # unique_titles = list(set(unique_titles))

    # # Записываем уникальные записи обратно в базу данных
    # cursor.executemany("DELETE FROM books WHERE Title IN (?)", [(title,) for title in unique_titles])
    # conn.commit()

    # # Закрываем соединение с базой данных
    # conn.close()