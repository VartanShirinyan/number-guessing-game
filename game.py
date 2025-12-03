# number-guessing-game/game.py
import random


print("Добро пожаловать в игру 'Угадай число'!")
print("Я загадал число от 1 до 100. Попробуй угадать!")
print("Я думаю, что ты угадаешь максимум за 7 попыток!")
print("Удачи!")
print("(Для выхода введите 'выход', 'exit', 'quit' или 'q')")
print("(Заглушка: игра еще в разработке)")

secret_number = random.randint(1, 100)
count = 0

print(f"(Отладка: загаданное число {secret_number})")

while True:
    try:
        user_input = input('Введите Ваше число: ')
        
        if user_input.lower() in ('выход', 'exit', 'quit', 'q'):
            print(f'Игра завершена. Загаданное число было: {secret_number}')
            break
        
        
        user_number = int(user_input)
        
        if user_number < 1 or user_number > 100:
            print("Пожалуйста, введите число от 1 до 100!")
            continue
        
        count += 1
        
        if user_number > secret_number:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif user_number < secret_number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        else:
            if count % 10 == 1 and count % 100 != 11:
                attempts_word = "попытку"
            elif 2 <= count % 10 <= 4 and not (12 <= count % 100 <= 14):
                attempts_word = "попытки"
            else:
                attempts_word = "попыток"
    
            print(f'Поздравляю, Вы угадали за {count} {attempts_word}!')
            break
        
        
    except ValueError:
        print("Ошибка! Пожалуйста, введите целое число.")
        continue