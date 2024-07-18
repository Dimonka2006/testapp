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