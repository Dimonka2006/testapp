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

with open('/root/testapp/Python_lesson/task9_dict.json', 'r') as f:
    data = json.load(f)

def task1(d):
     for k, v in d.items():
        print(k, v)    
         # if k  'president'     
#task(d)