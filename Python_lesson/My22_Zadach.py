# даны два списка в виде файлов json, 
    # 
    # необходимо написать функцию compare которая отфильтрует
    # строки содержищие 2 и более одинаковых слов
    # результат вывести в json файл в виде списка кортежей
    # в следующем формате

import json
from collections import Counter

with open('/root/testapp/Python_lesson/list1.json', 'r') as f:
    data = json.load(f)
#print(data)
with open('/root/testapp/Python_lesson/list2.json', 'r') as f2:
    data1 = json.load(f2)

def compare(list1, list2):
    # Преобразуем списки строк в списки слов
    slova1 = [word for sentence in list1 for word in sentence.split()]
    slova2 = [word for sentence in list2 for word in sentence.split()]
    # Фильтрация строк, содержащих два и более одинаковых слова
    filtered_sentences1 = []
    filtered_sentences2 = []
    for sentence in list1:
        if any(Counter(sentence.split())[word] > 1 for word in set(sentence.split())):
            filtered_sentences1.append(sentence)
    for sentence in list2:
        if any(Counter(sentence.split())[word] > 1 for word in set(sentence.split())):
            filtered_sentences2.append(sentence)
    
    return filtered_sentences1, filtered_sentences2

filtered_list1, filtered_list2 = compare(list1, list2)
print(f"Filtered list 1: {filtered_list1}")
print(f"Filtered list 2: {filtered_list2}")

                                 
with open('line3.json', 'w') as f_out:
    json.dump(data, f_out, ensure_ascii=False)
            


