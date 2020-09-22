"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


from random import randint


def gen_number():
    """ Рандомное число """
    return randint(0, 100)


def what(y):
    """ Пользлватель должен угадать загаданное число. """
    print('Угадай число от 0 до 100.')
    x = int(input('Ваш ответ: '))
    if x == y:
        print(f'Вы угадали! Число {x} верный ответ.')
    elif y < x < 101:
        print(f'Загаданное число меньше {x}.')
        what(y)
    elif y > x > -1:
        print(f'Загаданное число больше {x}.')
        what(y)
    else:
        print(f'Число {x} не входит в диапазон.')
        what(y)


z = gen_number()
what(z)
