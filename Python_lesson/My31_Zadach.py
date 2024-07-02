# создайте множество в котором указано несколько стран
# пользователь вводит страну и если страна есть в множестве выводится ответ 
# "Страна уже посещена" если нет такой страны то она добавляется во множество и выводится 
# ответ "Страна добавлена"


country_mnog = {'Russia', 'Germany', 'Britany', 'France', 'Jopan', 'China'}

while True:
    user_input = input("Введите страну: ")
    if not user_input:
        continue

    if user_input in country_mnog:
        print(f"Вы указали '{user_input}' Страна уже посещена")
    else:
        # если строки нет добовляем ее
       country_mnog.add(user_input)
       print(f"Страна '{user_input}' добавлена")
    print("Текущий список: ", country_mnog)

     # Запрашиваем у пользователя, хочет ли он продолжить работу с программой
    continue_program = input("Хотите продолжить (y/n)? ")
    
    # Если пользователь ввел 'n', завершаем программу
    if continue_program == 'n':
        break



