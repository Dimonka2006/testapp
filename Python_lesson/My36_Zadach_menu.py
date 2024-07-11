# Создание меню для работы с 'books.db'

def spisok_command():
    pass



def serch():
    print('serching')

def plus_db():
    print('plussing')   

def dell_book():
    print('delling') 

def append_book():
    print('appending')        

def menu():
    command = [('Serch', serch), ('Plus_db', plus_db), ('Dell_book', dell_book), ('Append_book', append_book)]
    

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