# Создание меню для работы с 'books.db'
import sqlite3

def spisok_command():
    pass

def menu():
    command = [('Search', search), ('Plus_db', plus_db), ('Dell_book', dell_book), ('Append_book', append_book), ('Kill_duble_book', kill_duble_book)]
    

    while True:
        for i , menu_item in enumerate(command):
            print(i, menu_item[0])
        
        whrite_command = input('whrite comman ' )    

        for k in command:
            if k[0] == whrite_command:
                k[1]()

        # Запрашиваем у пользователя, хочет ли он продолжить работу с программой        
        continue_program = input("Хотите продолжить (y/n)? ")
        # Если пользователь ввел 'n', завершаем программу
        if continue_program == 'n':
            break
menu()

def search():
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

# Вызываем функцию
search()  
print('serching')

def plus_db():
    print('plussing')   

def dell_book():
    print('delling') 

def append_book():
    print('appending')     

def kill_duble_book():
    print('killing')      

