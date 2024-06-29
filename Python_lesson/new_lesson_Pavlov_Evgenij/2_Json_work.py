import json

sample_dic = {}

sample_array = []

sample_dic = {"ключ21":"значение 21",
"ключ22":"значение 22"}

sample_array = ["значение 31", "значение 32",
"значение 33"]

main_dic = {"ключ1": "значение 1"}

main_dic ["ключ2"] = sample_dic

main_dic ["ключ3"] = sample_array

print(main_dic)

print("______________________________________\n")

print(json.dumps(main_dic))   #Это, брат, юникод.

print("______________________________________\n")

print(json.dumps(main_dic,ensure_ascii=False)) #отключим его

print("______________________________________\n")

json_str=json.dumps(main_dic, ensure_ascii=False, indent=2)

print(json_str) #JSON игнорирует пробелы, перевод строки и табуляции,
#поэтому можно их добавлять в строку, чтобы выделить структуру данных
#
print("______________________________________\n")

#Нам опять нужен файловый дескриптор, но на этот раз в режиме записи
#‘w’ —write:
file_descriptor=open(r'2_Json_print.json', 'w', encoding='utf16')
file_descriptor.write(json_str)
file_descriptor.close()

print("_________________________________________________________ \n")

file_descriptor=open('2_Json_print.json', 'r', encoding='utf-16')
json_str=file_descriptor.read()
main2_dic=json.loads(json_str)
print(main2_dic)
print(main_dic)





