# Предположим, у нас есть список со строками, представляющими фразы
phrases = ["Я люблю программирование", "Пицца очень вкусная", "Мне нравится изучать Python"]

# Используем max() с ключом key=len для выбора строки с максимальной длиной
longest_phrase = max(phrases, key=len)

print(longest_phrase)  # Выведет самую длинную фразу
