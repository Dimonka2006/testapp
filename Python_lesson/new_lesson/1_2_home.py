#1. открой (создай) файл на запись и напечатай туда
#7 строк с номерами;
#2. создай массив из семи чисел, преврати его в json и сохрани в файл

import json

with open(r'1_1_home_print.txt', 'w', encoding='utf16') as file:
    for i in  range(1, 8):
        file.write(f'{i} строка\n')
        
print(file)
        




#jonson_array = ["1", "2", "3", "4", "5", "6", "7" ]



#file_descriptor=open(r'1_2_home_print.json', 'w', encoding='utf16')
#file_descriptor.write(json_array)
#file_descriptor.close()