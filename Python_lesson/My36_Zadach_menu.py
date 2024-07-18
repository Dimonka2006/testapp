# Создание меню для работы с 'books.db'
import sqlite3
from collections import Counter

def spisok_command():
    pass


def search_book():
    print('searching')
    # поиск в базе данных sq
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    # Запрашиваем у пользователя имя автора
    author_name = input("Введите имя автора: ")

    query = 'SELECT  *  FROM books WHERE Author=?'
    cur.execute(query, (author_name,))
    # Получаем результаты запроса
    results = cur.fetchall()
 
    for result in results:
        print(result)
    # Закрываем соединение с базой данных
    cur.close()
    conn.close()


def plus_db():
    print('plussing')   

def dell_book():
    print('delling') 

    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    # Запрашиваем у пользователя название книги
    book_name = input("Введите название книги: ")

    query = 'DELETE FROM books WHERE title = ?'
    cur.execute(query, (book_name,))

    # Сохранение изменений в базе данных
    conn.commit()

    # Закрытие соединения с базой данных
    conn.close()

def append_book():
    print('appending')
    # Создаем соединение с базой данных
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    # Запрашиваем у пользователя данные по книге
    
    info_book = input("Введите 'Название книги', 'Автор', 'Жанр', Страниц, 'Издатель': ")

    # Формируем SQL-запрос для добавления новой записи
    #sql = f"INSERT INTO books (Title, Author, Genre, Height, Publisher) VALUES ('title', 'author', 'genre', height, 'publisher');"
    sql = 'INSERT INTO books (Title, Author, Genre, Height, Publisher) VALUES (?, ?, ?, ?, ?)'
    #sql = "INSERT INTO books VALUES (?, ?, ?, ?, ?), (row['Title'], row['Author'], row['Genre'], ['Height'], row['Publisher']);"
    # Добавляем данные в таблицу
    cursor.execute(sql, (info_book))

    # Сохраняем изменения в базе данных
    conn.commit()

    # Закрываем соединение
    conn.close()



def kill_duble_book():
    print('killing')      

    # # Открываем соединение с базой данных
    # conn = sqlite3.connect('books.db')
    # cursor = conn.cursor()

    # # Читаем все записи из таблицы в список
    # cursor.execute("SELECT  *  FROM books")
    # records = cursor.fetchall()

    # # Проверяем каждую запись на наличие дубликатов
    # unique_records = []
    # for record in records:
    #     title, author, genre, height, publisher = record
    #     if (title, author, genre, height, publisher) not in unique_records:
    #         unique_records.append((title, author, genre, height, publisher))

    # # Удаляем дубликаты из списка
    # unique_records = list(set(unique_records))

    # # Записываем уникальные записи обратно в базу данных
    # cursor.executemany("INSERT OR REPLACE INTO books VALUES (?, ?, ?, ?, ?)", unique_records)
    # conn.commit()

    # # Закрываем соединение с базой данных
    # conn.close()
# Открываем соединение с базой данных
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()

    # Читаем все записи из таблицы в список
    cursor.execute("SELECT Title FROM books GROUP BY Title HAVING count( * ) > 1")
    titles = cursor.fetchall()

    # Проверяем каждую запись на наличие дубликатов
    unique_titles = []
    for title in titles:
        if title[0] not in unique_titles:
            unique_titles.append(title[0])

    # Удаляем дубликаты из списка
    unique_titles = list(set(unique_titles))

    # Записываем уникальные записи обратно в базу данных
    cursor.executemany("DELETE FROM books WHERE Title IN (?)", [(title,) for title in unique_titles])
    conn.commit()

    # Закрываем соединение с базой данных
    conn.close()

def menu():
    command = [('Search_book', search_book), ('Plus_db', plus_db), ('Dell_book', dell_book), ('Append_book', append_book), ('Kill_duble_book', kill_duble_book)]
    

    while True:
        for i , menu_item in enumerate(command):
            print(i, menu_item[0])
        
        whrite_command = input('введите команду ' )    

        for k in command:
            if k[0] == whrite_command:
                k[1]()

        # Запрашиваем у пользователя, хочет ли он продолжить работу с программой        
        continue_program = input("Хотите продолжить (y/n)? ")
        # Если пользователь ввел 'n', завершаем программу
        if continue_program == 'n':
            break
menu()
