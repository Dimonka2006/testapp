# дан список w с набором слов
# создать словарь в котором слова из списка будут ключами, 
# а значением будет количество повторений слова в списке
# пример {"sausage": 2, ...}
# результат вывести в консоль
w = [
    "beef", "pork", "potato", "mashroom", "creamy", "lemon", "pepper", "milk", "rice", "sausage",
    "cranberry", "pineapple", "chicken", "kebab", "onion", "mustard", "mutton", "olive", "chili",
    "mince", "coconut", "bread", "cheese", "chocolate", "pork", "ribs", "beef mince", "honey",
    "chicken momos", "pizza", "apple pie", "potato", "sweet potato", "tomato", "beef", "pie",
    "onion", "fish", "chops", "apple", "orange", "melon", "dragon fruit", "durian", "mince",
    "potato", "coconut oil", "sunflower oli", "olive", "chili", "pepper", "pie", "bread",
    "chicken", "kebab", "olive oil", "rice oil", "rice", "ginger", "honey", "sausage"
]

def convert(w):
    # Создаем пустой словарь для хранения результата
    res_dict = {}
    for i in w:
         # Разбиваем входную строку на отдельные слова
        if i in res_dict:
                 
            # Увеличиваем счетчик для текущего слова, если он уже есть в словаре
             res_dict[i] += 1
 
        else:
            # Если слово встречается впервые, добавляем его в словарь с начальным значением 1
             res_dict[i] = 1
    
    return res_dict



print(convert(w))
