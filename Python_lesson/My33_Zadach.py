# дан файл с книгами, загрузить данные из файла в библиотеку из нашей задачи
#  (структуру библиотеки нужно адаптировать под данные из файла) для загрузки
#  данных использовать модуль стандартной библиотеки csv (сначала стоит
#  ознакомиться с его возможностями) и адаптировать функции для добавления и 
# поиска книг под новый формат библиотеки также реализовать функцию удаления книг
#если будет интересно, то можно реализовать также функцию сохранения текущего состояния 
# библиотеки обратно в csv файл

import csv

lib = []
with open('books.csv', 'r', newline='', encoding='utf-8') as file:
    # Создаем объект writer для записи данных в файл
    reader = csv.DictReader(file, fieldnames=['Title', 'Author', 'Genre', 'Height', 'Publisher'])
    
    for row in reader:
        lib.append(row)
    # читаем заголовки столбцов
        #print(row)         
#print(lib)


# #Title,Author,Genre,Height,Publisher
def new_book(title, author, genre, height, publisher):
     book = {"Title":title, "Author":author, "Genre":genre, "Height":height, "Publisher":publisher}
     lib.append(book)

new_book("Убийство в поезде", "Агата Кристи", "Детектив", 300, "Аркаим")
#print(lib[-2:])
# #print(lib)

def find_book(title = None, author = None, genre = None, height = None, publisher = None): # не обязательные именованные аргументы
    resault_sp = []
    for book_dict in lib:
#         #print(book_dict)
        if title == book_dict["Title"] or author == book_dict["Author"] or genre == book_dict["Genre"] or height == book_dict["Height"] or publisher == book_dict["Publisher"]:

            resault_sp.append(book_dict)


    return resault_sp

books = find_book(genre = "history") # Поиск по именованному аргументу
# print(books)


def remove_book(lib, title):
    # Удаляет книгу с заданным названием из списка книг.
    for i, book in enumerate(lib):
        if book['title'] == title:
            del lib[i]
            break
    # Удаляем книгу
    remove_book(lib, 'The Hobbit')
# 2 вариант: удаляем строку, например, под номером -1
# del lib[-1:] # из общей библиотеки
#print(lib[-2:])

def save_books_to_csv():
    
    with open('new_books.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Title', 'Author', 'Genre', 'Height', 'Publisher'])
        writer.writerow()
        for book in books:
            writer.writerow(book)
            print(book)
                
# proverka = save_books_to_csv(books)
# print(proverka)
    