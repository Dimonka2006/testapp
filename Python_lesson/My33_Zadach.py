# дан файл с книгами, загрузить данные из файла в библиотеку из нашей задачи
#  (структуру библиотеки нужно адаптировать под данные из файла) для загрузки
#  данных использовать модуль стандартной библиотеки csv (сначала стоит
#  ознакомиться с его возможностями) и адаптировать функции для добавления и 
# поиска книг под новый формат библиотеки также реализовать функцию удаления книг
#если будет интересно, то можно реализовать также функцию сохранения текущего состояния 
# библиотеки обратно в csv файл

import csv

with open('books.csv', 'w', newline='', encoding='utf-8') as file:
    # Создаем объект writer для записи данных в файл
    writer = csv.DictWriter(file, fieldnames=['title', 'author', 'genre', 'height', 'publisher'])
    
    # Записываем заголовки столбцов
    writer.writeheader()
    
    # Записываем данные в файл
    writer.writerows(file)

#Title,Author,Genre,Height,Publisher
def new_book(title, author, genre, height, publisher):
    book = {"title":title, "author":author, "genre":genre, "height":height, "publisher":publisher}
    file.append(book)

new_book("Убийство в поезде", "Агата Кристи", "Детектив", 300, "Аркаим")

#print(lib)

def find_book(title, author, genre, height, publisher):
    resault_sp = []
    for book_dict in file:
        #print(book_dict)
        if title == book_dict["title"] or author == book_dict["author"] or genre == book_dict["genre"], or genre == book_dict["height"], or genre == book_dict["publisher"]:

            resault_sp.append(book_dict)


    return resault_sp

books = find_book("Убийство в поезде", "Агата Кристи", "Детектив", 300, "Аркаим")
print(books)