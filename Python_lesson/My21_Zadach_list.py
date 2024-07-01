w = [
    "beef", "pork", "potato", "mashroom", "creamy", "lemon", "pepper", "milk", "rice", "sausage",
    "cranberry", "pineapple", "chicken", "kebab", "onion", "mustard", "mutton", "olive", "chili",
    "mince", "coconut", "bread", "cheese", "chocolate", "pork", "ribs", "beef mince", "honey",
    "chicken momos", "pizza", "apple pie", "potato", "sweet potato", "tomato", "beef", "pie",
    "onion", "fish", "chops", "apple", "orange", "melon", "dragon fruit", "durian", "mince",
    "potato", "coconut oil", "sunflower oli", "olive", "chili", "pepper", "pie", "bread",
    "chicken", "kebab", "olive oil", "rice oil", "rice", "ginger", "honey", "sausage"
]
# выводит множество уникальных (не повторяющ. элементов)
print(set(w))
# кол-во значений 
print(len(w))
# кол-во уникальных значений
print(len(set(w)))

# выводит значения содержащие oil
for slovo in w:
    if 'oil' in slovo:
        print(slovo)