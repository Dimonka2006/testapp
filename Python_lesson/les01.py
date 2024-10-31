# Реализуйте функцию is_contains_char(), которая проверяет с учётом регистра, содержит ли переданная строка указанную букву. Функция принимает два параметра:

# Строка
# Буква для поиска

def is_contains_char(line:str, symbol:str)->bool:
    index = 0
    while index < len(line):
        if line[index] == symbol:
            return True
        index += 1
    return False    

print(is_contains_char('Hexlet', 'H'))  # => True
print(is_contains_char('Hexlet', 'h'))  # => False
print(is_contains_char('Awesomeness', 'm'))  # => True
print(is_contains_char('Awesomeness', 'd'))  # => False