# Напишите программу которая будет заносить в список текст введенный пользователем 
# и удалять если такая строка уже имеется в списке после добавления либо удаления 
# должен выводиться список

vivoditca_spisoc =[]

while True:
    user_input = input("Введите строку: ")
    if not user_input:
        continue

    if user_input in vivoditca_spisoc:
        print(f"Строка '{user_input}' такая строка уже есть")
    else:
        # если строки нет добовляем ее
        vivoditca_spisoc.append(user_input)
        print(f"Строка '{user_input}' добавлена")
    print("Текущий список: ", vivoditca_spisoc)

     # Запрашиваем у пользователя, хочет ли он продолжить работу с программой
    continue_program = input("Хотите продолжить (y/n)? ")
    
    # Если пользователь ввел 'n', завершаем программу
    if continue_program == 'n':
        break
