import random
def guessing_game ():
    answer = random.randint (0, 100)
    while True:
        user_guess = int (input ('Каковы ваши предположения?'))
        if user_guess == answer:
            print(f'Правильно! Ответ {user_guess}')
            break
        if user_guess < answer:
            print(f'Ваше число {user_guess} слишком маленькое!')
        else:
            print(f'Ваше число {user_guess} слишком большое!')
guessing_game ()