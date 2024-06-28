# даны два списка в виде файлов json, 
    # 
    # необходимо написать функцию compare которая отфильтрует
    # строки содержищие 2 и более одинаковых слов
    # результат вывести в json файл в виде списка кортежей
    # в следующем формате

import json


with open('/root/testapp/Python_lesson/list1.json', 'r') as f:
    data1 = json.load(f)
#print(data)
with open('/root/testapp/Python_lesson/list2.json', 'r') as f2:
    data2 = json.load(f2)

def compare(l1, l2):
    res = []
    for i in l1:
            for k in l2:
                set_i = set(i.lower().split(" "))
                set_k = set(k.lower().split(" "))
                set_res=set_i.intersection(set_k)
            
                if len(set_res) > 2:
                    res.append((i, k,tuple(set_res)))
    return res

                                 
with open('line3.json', 'w') as f_out:
    json.dump(compare(data1, data2), f_out, ensure_ascii=False)
            


