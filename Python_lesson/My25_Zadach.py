# Создайте список содержащий названия фруктов, 
# напишите программу которая выведет каждое название в новой строке
fruits = ["apple", "orange", "pineapple", "mango", "cherry"]

for key in fruits:
    print(key)


# Создайте список содержащий названия фруктов, 
# напишите программу которая ваведет каждое название в новой строке
fruits = ["apple", "orange", "pineapple", "mango", "cherry"]

# Александр Гладков, [30.06.2024 12:28]
fruits = ["apple", "orange", "pineapple", "mango", "cherry"]

s = "\n".join(fruits)

print(s)

# отсортировать, наименование с 'a' написать функцию и вернуть списком

def filter(fruits):
    new_fruits = []
    for key in fruits:
        if 'a' in key:
            new_fruits.append(key)
    
    return new_fruits
    
print(filter(fruits))

print(_____________________\n)


a = [ f for f in fruits if "a" in f]

