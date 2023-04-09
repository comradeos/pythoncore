import random

guess = 1
scores = 0

for i in range(1, 6):
    number = random.randint(1, 5)

    print(f'Спроба № {i}: Я загадала число від 1 до 5! Вгадай: ', end='')

    guess = int(input())
    if guess == number:
        print('Правильно! ☺')
        scores += 1
    else:
        print('Не правильно! ☹')


    print(f'В тебе {scores} очок!')

