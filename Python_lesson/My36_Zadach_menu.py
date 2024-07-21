# Создание меню для работы с 'books.db'
import sqlite3
from collections import Counter

def spisok_command():
    pass

def run_sql(sql, sql_param):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    try:
        cur.execute(sql, sql_param)
        conn.commit()
    except Exception as e:
        print("Error running SQL: ", e)
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def search_book():
    print('searching')
    # поиск в базе данных sq
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    print('Title', 'Название книги')
    print('Author', 'Автор книги')
    print('Genre', 'Жанр книги')
    print('Height', 'Высота книги')
    print('Publisher', 'Издательство')
    # Запрашиваем у пользователя параметр для поиска
    column = input("Введите название столбца для поиска: ")
    value = input("Введите значение для поиска: ")

    # Формируем SQL-запрос
    query = f'SELECT  *  FROM books WHERE {column} LIKE ?'
    cur.execute(query, (value,))
    # Получаем результаты запроса
    results = cur.fetchall()
 
    for result in results:
        print(result)
    # Закрываем соединение с базой данных
    cur.close()
    conn.close()


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
    try:
        # Создаем соединение с базой данных
        conn = sqlite3.connect('books.db')
        cur = conn.cursor()
        # Запрашиваем у пользователя данные по книге
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        genre = input("Введите жанр книги: ")
        height = input("Введите высоту книги: ")
        publisher = input("Введите издателя книги: ")

        # Формируем SQL-запрос для добавления новой записи
        sql = 'INSERT INTO books (Title, Author, Genre, Height, Publisher) VALUES (?, ?, ?, ?, ?)'

        # Добавляем данные в таблицу
        cur.execute(sql, (title, author, genre, height, publisher))

        # Сохраняем изменения в базе данных
        conn.commit()
            # Закрываем соединение
        conn.close()
        cur.close()
    except Exception as e:
        print(f'Ошибка при добавлении книги: {e}')


def kill_duble_book():
    print('killing')      

    # Подключаемся к базе данных
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()

    # Выполняем запрос с оператором DISTINCT
    cur.execute("SELECT DISTINCT  *  FROM books")

    # Обновляем базу данных
    conn.commit()

    # Закрываем соединение
    conn.close()



def menu():
    command = [('Search_book', search_book), ('Dell_book', dell_book), ('Append_book', append_book), ('Kill_duble_book', kill_duble_book)]
    

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
