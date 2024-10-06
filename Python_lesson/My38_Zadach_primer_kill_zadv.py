# Удаление повторяющихся строк и сохранение в отдельный файл
def kill_duble_strok():

    target = input("Введите ссылку на файл\n\n")
    
    f = open(target, 'r')
    l = [line.strip() for line in f]
    unique = []
    [unique.append(item) for item in l if item not in unique]
    if unique[0]:
        print('\n Дубликаты удалены')
    f.close()

    filename2 = target + 'unic_Sp_book.txt'
    fw = open(filename2, 'w')
    for index in unique:
        fw.write(index + '\n')
    fw.close()        
    
kill_duble_strok()