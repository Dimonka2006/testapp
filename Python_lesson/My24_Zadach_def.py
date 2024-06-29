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
        #for k, v in d.items():
         #   print(k, v)    
            # if k  'president'     
    for key in keys_to_extract:
        if key in json_data:
            value = json_data[key] # значения списка по ключу
            try:
                print(value[0]) # выводим первую строку
            except IndexError:
                pass # список пуст

json_data = data
keys_to_extract = ('president', 'collection', 'game', 'voice', 'spaceship')

task1(json_data, keys_to_extract)