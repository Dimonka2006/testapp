# Реализуйте функцию my_substr(), которая извлекает из переданной строки подстроку указанной длины. 
# Она принимает на вход два аргумента: строку и длину, и возвращает подстроку, начиная с первого символа:

string = 'If I look back I am lost'
def my_substr(string, n) -> str:
    index = 0
    new_str = ''
    while index < n:
        new_str = new_str + string[index]
        index = index + 1
    return new_str

print(my_substr(string, 1)) # => 'I'
print(my_substr(string, 7)) # => 'If I lo'

# Используйте тот же подход, что в функции для переворота строки из урока: 
# собирайте строку-результат в цикле, перебирая начальную строку до определённого момента.
