#1. открой (создай) файл на запись и напечатай туда
#7 строк с номерами;
#2. создай массив из семи чисел, преврати его в json и сохрани в файл

import json
# Открываем файл на запись
with open(r'1_1_home_print.txt', 'w', encoding='utf16') as file:
    for i in  range(1, 8): # Создаем последовательность чисел с 1 по 7
        file.write(f'{i} строка\n')
     


# Создаем массив
numbers = [1, 2, 3, 4, 5, 6, 7]

# Преобразуем массив в JSON строку
json_data = json.dumps(numbers)

# Сохраняем JSON строку в файл
with open('numbers.json', 'w') as f:
    f.write(json_data)