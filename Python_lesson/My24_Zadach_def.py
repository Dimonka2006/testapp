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

def process_dictionary(json_file_path, keys_to_extract):
    """Проходит по словарю в JSON файле и возвращает новый словарь с найденными ключами и значениями."""
    # Читаем содержимое JSON файла
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    new_dict = {}
    for key in keys_to_extract:
        if key in data: # Создаем новый ключ в новом словаре и присваиваем ему значение из исходного словаря
            new_dict[f'NewKey_{key}'] = data[key]
        
    return new_dict

new_dictionary = task1(json_data, keys_to_extract)

json_file_path = 'C:\\task9_dict.json'  # Путь к JSON файлу
keys_to_extract = ('president', 'collection', 'game', 'voice', 'spaceship') # Ключики

print(new_dictionary)