# Создать список словарей для хранения данных о любимых книгах (библиотека), 
# словарь должен содержать поля title, author, genre 
# написать функцию для добавления новой книги в библиотеку 
# а также функции поиска книги по заголовку и по автору

lib = [
    {"title": "Не укратимая планета", "author": "Гари Гариссон", "genre": "Фантастика"}, 
    {"title": "9 принцев Амбера", "author": "Роджер Желязный", "genre": "Фэнтази"}
]

def new_book(title, author, genre):
    book = {"title":title, "author":author, "genre":genre}
    lib.append(book)

new_book("Убийство в поезде", "Агата Кристи", "Детектив")

#print(lib)

def find_book(title, author, genre):
    resault_sp = []
    for book_dict in lib:
        #print(book_dict)
        if title == book_dict["title"] or author == book_dict["author"] or genre == book_dict["genre"]:

            resault_sp.append(book_dict)

        #f author == book_dict["author"]:

        #    resault_sp.append(book_dict)
        
       # if genre == book_dict["genre"]:
            
        #    resault_sp.append(book_dict)
             
       
    return resault_sp

books = find_book("Убийство в поезде", "Агата Кристи", "Детектив")
print(books)