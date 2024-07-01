#1.  *  * Списки (Lists) *  * :
 #  - Создайте список из чисел от 1 до 10.
sp = []
for i in range(1, 11):
   # print (i)
   sp.append(i)
print(sp)
  # - Добавьте элемент в начало списка.
sp.insert(0, 0)
print(sp)
   #- Удалите первый элемент из списка
sp.remove(0)
print(sp)
   #- Выведите третий элемент списка.
print(sp[2])

print('____________________________________\n')

#2.  *  * Словари (Dictionaries) *  * :
#  - Создайте словарь, где ключи - это числа от 1 до 10, а значения - их квадраты.
new_dict = {}
for i in range(1, 11):
   new_dict[i] = i ** 2

print(new_dict)

#   - Добавьте новое значение к существующему ключу.
new_dict2 = {'key_1': 'old_v', }
new_dict2['key_1'] += ', new_v'
print(new_dict2)
#   - Удалите пару ключ-значение из словаря.
old_dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
old_dict.clear() # почистил весь словарь от пар ключ-значение
print(old_dict)
cool_dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36,}
cool_dict.popitem() # почистил словарь от последней пары ключ-значение
print(cool_dict)
#   - Выведите значение, соответствующее ключу 5.
print(cool_dict.get(5))

print('____________________________________\n')

#3.  *  * Туризмы (Tuples) *  * :
#   - Создайте кортеж из трех элементов.
#   - Измените второй элемент кортежа.
#   - Добавьте новый элемент в конец кортежа.
#   - Выведите второй элемент кортежа.

#4.  *  * Установки (Sets) *  * :
#   - Создайте множество из чисел от 1 до 10.
#   - Объедините два множества.
#   - Выведите размер множества.
#   - Проверьте, содержится ли число 5 в множестве.

#5.  *  * Функции (Functions) *  * :
#   - Определите функцию, которая принимает список и возвращает его длину.
#   - Определите функцию, которая принимает два аргумента и возвращает их сумму.
#   - Вызовите обе функции с примерами входных данных.