# Дан список чисел a и список чисел b 
# проверить входят ли числа из списка б в список а, вывести числа которые входят
a = [1, 100, 955, 54, 30, 46, 222, 39, 931, 728, 0, 100, 54]
b = [728, 900, 39, 440, 222]

def new_sp(a, b):
    c = []
    for key in a:
        if key in b:
            c.append(key)
    return c
print(new_sp(a, b))        