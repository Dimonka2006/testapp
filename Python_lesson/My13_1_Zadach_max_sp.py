def pad_strings(strings):
    # Находим максимальную длину среди всех строк
    max_length = max(len(s) for s in strings)
    
    # Создаем новый список, где каждая строка дополнена пробелами до одинаковой длины
    padded_strings = []
    for string in strings:
        padding = ' '  *  (max_length - len(string))
        padded_strings.append(padding + string)
    
    return padded_strings

# Пример использования функции
strings = ['abc', 'abcd', 'abcde', 'abcdef']
padded_strings = pad_strings(strings)
print(padded_strings)
