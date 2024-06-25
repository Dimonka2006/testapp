# даны два списка в виде файлов json, 
    # 
    # необходимо написать функцию compare которая отфильтрует
    # строки содержищие 2 и более одинаковых слов
    # результат вывести в json файл в виде списка кортежей
    # в следующем формате

import json


with open('/root/testapp/Python_lesson/list1.json', 'r') as f:
    data = json.load(f)

with open('/root/testapp/Python_lesson/list2.json', 'r') as f:
    data1 = json.load(f)

def compare(l1, l2):
    print("compare")
    line3 = []
    for line in l1:
        for line2 in l2:
            slova = line.split(" ")
            slova2 = line2.split(" ") 
            num = 0
            for s in slova:
                if s in slova2:
                    num += 1
                    if num >= 2:
                        
                        return line3
    
                                 
with open('line3.json', 'w') as f_out:
    json.dump(data, f_out, ensure_ascii=False)
            

print(compare(data, data1))
