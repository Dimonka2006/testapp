# Реализуйте функцию print_table_of_squares(from, to), которая печатает на экран квадраты чисел. 
# Она первое from и последнее to число печатает строку square of <число> is <результат>

def print_table_of_squares(start, to):

    for i in range(start, to + 1):
        square = i * i
        print(f"square of {i} is {square}")


print_table_of_squares(1, 3)
# => square of 1 is 1
# => square of 2 is 4
# => square of 3 is 9