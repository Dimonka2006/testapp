# Дан словарь в виде json файла
    # написать функции которые проходит по данному словарю и
    # если в текущем словаре есть ключи president collection game voice spaceship
    # 1 по каждому ключу вывести первую строку из значения списка
    #
    # 2 возвращает новый словарь с найденными ключами и значениями
    #
    # 3 вовзращает новый словарь с найденными ключами, 
    # значения-списки должны содержать только строки для которых больше 50
    #
    # 4 вовзращает новый словарь с найденными ключами,
    # значения-списки должны содержать только 2 первых и 2 последних строчки

import json

with open('C:\\task9_dict.json', 'r') as f:
    data = json.load(f)

def task1(json_data, keys_to_extract):

    for key in keys_to_extract:
        if key in json_data:
            value = json_data[key] # значения списка по ключу
            try:
                print(value[0]) # выводим первую строку
            except IndexError:
                pass # список пуст

json_data = data
keys_to_extract = ('president', 'collection', 'game', 'voice', 'spaceship')

print('_____________________________________\n')


def task2(json_file, keys_to_extract):
    
    # Читаем содержимое JSON файла
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    new_dict = {}
    for key in keys_to_extract:
        if key in data: # Создаем новый ключ в новом словаре и присваиваем ему значение из исходного словаря
            new_dict[f'NewKey_{key}'] = data[key]
        
    return new_dict

json_file = 'C:\\task9_dict.json'  # Путь к JSON файлу
keys_to_extract = ('president', 'collection', 'game', 'voice', 'spaceship') # Ключики

new_dictionary = task2('C:\\task9_dict.json', keys_to_extract)

print(new_dictionary)

print('_____________________________________\n')


def task4(json_data, keys_to_extract):
    with open(json_data, 'r') as f:
        data = json.load(f)

    new_dict2 = {} # Создаем новый словарь для хранения результатов
    for key in keys_to_extract:
        if key in data:
        # Преобразуем список строк в список объектов, чтобы работать с ними
            lines = [line.strip() for line in data[key].split('\n')]
                
            # Выбираем первые две и последние две строки
            first_two = lines[:2]
            last_two = lines[-2:]
                
            # Добавляем результаты в новый словарь
            new_dict2[key] = '\n'.join(first_two + last_two)
    return new_dict2

json_data = 'C:\\task9_dict.json'
keys_to_extract = ('president', 'collection', 'game', 'voice', 'spaceship')
new_dict2 = task4(json_data, keys_to_extract)
print(new_dict2)

print('_____________________________________\n')