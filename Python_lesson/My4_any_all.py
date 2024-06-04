## any all
sp2 = [1, 15 , 50, 100, 200]
if any (number>50 for number in sp2):
    print("Есть число больше 50")

sp1 = [True, False, True]

if all (sp1):
    print ("Все элементы True")
else:
    print("Не все элементы True")

if any (sp1):
    print ("Хотя бы один элемент True")

if any (sp1) and not all (sp1):
    print ("Есть элемент True и False")
