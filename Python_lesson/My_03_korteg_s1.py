#кортежи
sp1 = ('яблоки', 'бананы', 'капуста', 'морковь', 'грибы', 'сыр')
print(sp1)
print(sp1[2])
print(sp1[2:])

#словари

s1 = {"ключ":"значение",
       "Яблоко":"Яблоне", "Груша":"жвачка", "бананы":"Ананы"}
print(s1)
print(s1["Яблоко"])

s1["dvigatel"] = "mashina"
print(s1)

s1["Груша"] = "Высокое грушевое дерево"
print(s1)

del s1["Груша"]
print(s1)
