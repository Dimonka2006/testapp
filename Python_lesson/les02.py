# Функция принимает на вход строку и символ и возвращает новую строку, 
# в которой удалён переданный символ во всех его позициях. На этот раз реализуйте эту функцию с помощью цикла for. 
# Дополнительное условие: регистр исключаемого символа не имеет значения.

text = 'If I look forward I win'

def filter_string(string:str, symbol:str)->str:
    result = ''
    for symbols in string:
        if symbols.lower() != symbol.lower():
            result += symbols 
    return result    


filter_string(text, 'i')  # 'f  look forward  wn'
filter_string(text, 'O')  # 'If I lk frward I win'