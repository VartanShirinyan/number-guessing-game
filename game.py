# number-guessing-game/game.py
import random


print("Добро пожаловать в игру 'Угадай число'!")
print("Я загадал число от 1 до 100. Попробуй угадать!")
print("Я думаю, что ты угадаешь максимум за 7 попыток!")
print("Удачи!")
print("(Заглушка: игра еще в разработке)")

secret_number = random.randint(1, 100)
count = 0

while True:
    user_number = int(input('Введите Ваше число: '))
    if user_number > secret_number:
        print('Ваше число больше загаданного, попробуйте еще разок')
        count += 1
    elif user_number < secret_number:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        count += 1
    else:
        print(f'Поздравляю, Вы Угадали за {count} попыток(ки)!')
        break