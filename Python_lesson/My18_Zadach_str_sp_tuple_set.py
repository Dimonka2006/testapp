# написать функцию 


l = [
    ("Guy"), 
    {"support"}, 
    350,
    ("answer", "nothing"), 
    (), 
    " ", 
    ["involve", "modern"], 
    "its",
    (221)
]
# 1 выведет тип каждого элемента 

for ork in l:
    print(type(ork))

# 2 которая выведет
# Guy support 350 answer nothing modern involve its 221

result = ""
for slovo in l:
    
    if type(slovo) is tuple:
        result += " ".join(slovo)

    elif type(slovo) is set:
        result += " ".join(slovo)
    elif type(slovo) is list:
        result += " ".join(slovo)    
    else:    
        result += str(slovo) + " "
        # Преобразуем каждый элемент в строку и добавляем пробел между ними
print(result)


# 3 выведет только числа (даже если они упакованы в итерируемый тип)

result = ""
for slovo in l:
    if type(slovo).__name__ not in ['str', 'set', 'tuple', 'list']: # исключая типы данных
        result += str(slovo) + " " 

print(result)
