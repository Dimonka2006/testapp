# 1. Преобразование словаря в список пар *  * :
#  Напишите функцию, которая принимает словарь и возвращает список пар ключ-значение.
my_dict = {'arbuz': 1, 'grusha': 2, 'chery': 3}
def sp_is_dict(my_dict):
    return list(my_dict.items())
print(sp_is_dict(my_dict)) # [('arbuz', 1), ('grusha', 2), ('chery', 3)]
print('____________________________\n')

# 2. Преобразование словаря в список значений *  * :
#  Напишите функцию, которая принимает словарь и возвращает список его значений.
my_dict_2 = {'arbuz': 'ygoda', 'grusha': 'fruit', 'chery': 'ygoda'}
def sp_znach_is_dict(my_dict_2):
    return list(my_dict_2.values())
print(sp_znach_is_dict(my_dict_2)) # 'ygoda', 'fruit', 'ygoda']
print('____________________________\n')

# 3. Преобразование словаря в список ключей *  * :
#  Напишите функцию, которая принимает словарь и возвращает список его ключей.
def sp_keys_is_dict(my_dict_2):
    return list(my_dict_2.keys())
print(sp_keys_is_dict(my_dict_2)) # ['arbuz', 'grusha', 'chery']
print('____________________________\n')

# 4. Преобразование словаря в строку *  * :
#  Напишите функцию, которая принимает словарь и возвращает его представление в виде строки.
def dict_in_string(my_dict_2):
    return ', '.join('{}: {}'.format(k, v) for k, v in my_dict_2.items())
print(dict_in_string(my_dict_2)) # arbuz: ygoda, grusha: fruit, chery: ygoda
print('____________________________\n')

# 5. Преобразование словаря в JSON *  * :
#  Напишите функцию, которая принимает словарь и возвращает его представление в формате JSON.

import json

json_string = json.dumps(my_dict)
print(json_string) # {"arbuz": 1, "grusha": 2, "chery": 3}
print('____________________________\n')

# 6. Преобразование словаря в дерево *  * :
#  Напишите функцию, которая принимает словарь и возвращает его представление в виде
#  бинарного дерева поиска.!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# 7. Преобразование словаря в множество *  * :
#  Напишите функцию, которая принимает словарь и возвращает множество его ключей.
def get_keys(my_dict_2):
    keys = my_dict_2.keys() # Получаем все ключи словаря
    unique_keys = set(keys) # Преобразуем их в множество, чтобы получить уникальные элементы
    return unique_keys
unique_keys = get_keys(my_dict_2)
print(unique_keys) # {'chery', 'grusha', 'arbuz'}
print('____________________________\n')

# 8. Преобразование словаря в обратный словарь *  * 
# : Напишите функцию, которая принимает словарь и возвращает обратный словарь, 
# где ключи и значения меняются местами.
def invert_dict(my_dict):
    return {v: k for k, v in my_dict.items()}
inverted_dict = invert_dict(my_dict)
print(inverted_dict) # {1: 'arbuz', 2: 'grusha', 3: 'chery'}
print('____________________________\n')