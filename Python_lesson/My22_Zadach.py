# даны два списка в виде файлов json, 
    # 
    # необходимо написать функцию compare которая отфильтрует
    # строки содержищие 2 и более одинаковых слов
    # результат вывести в json файл в виде списка кортежей
    # в следующем формате

import json
from collections import Counter

with open('/root/testapp/Python_lesson/list1.json', 'r') as f:
    data1 = json.load(f)
#print(data)
with open('/root/testapp/Python_lesson/list2.json', 'r') as f2:
    data2 = json.load(f2)

def compare(list1, list2):
    # Преобразуем списки строк в списки слов
    slova1 = [word for slova in list1 for word in slova.split()]
    slova2 = [word for slova in list2 for word in slova.split()]
    # Фильтрация строк, содержащих два и более одинаковых слова
    filtered_slovas1 = []
    filtered_slovas2 = []
    for slova in list1:
        if any(Counter(slova.split())[word] > 1 for word in set(slova.split())):
            filtered_slovas1.append(slova)
    for slova in list2:
        if any(Counter(slova.split())[word] > 1 for word in set(slova.split())):
            filtered_slovas2.append(slova)
    
    return filtered_slovas1, filtered_slovas2

filtered_list1, filtered_list2 = compare(data1, data2)
print(f"Filtered list 1: {filtered_list1}")
print(f"Filtered list 2: {filtered_list2}")

                                 
with open('line3.json', 'w') as f_out:
    json.dump(compare(data1, data2), f_out, ensure_ascii=False)
            


