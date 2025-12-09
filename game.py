# number-guessing-game/game.py
import random


print("="*50)
print('Добро пожаловать в игру "Угадай число"!')

while True:
    print("="*50)
    print("Я загадал число от 1 до 100. Попробуй угадать!")
    print("(Для выхода введите 'exit')")
    print("(Заглушка: игра еще в разработке)")

    secret_number = random.randint(1, 100)
    count = 0

    print(f"(Отладка: загаданное число {secret_number})")

    while True:
        
        user_input = input('\nВведите Ваше число: ')
            
        if user_input.lower() in ('exit'):
            print(f'Игра завершена. Загаданное число было: {secret_number}')
            print("Спасибо за игру! До свидания!")
            exit(    )
            
        is_number = True
        for char in user_input:
            if char not in "0123456789":
                is_number = False
                break
            
        if not is_number:
            print("Ошибка! Пожалуйста, введите целое число.")
            continue    
            
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
            if count == 1:
                attempts_word = "попытку"
            elif 2 <= count <= 4:
                attempts_word = "попытки"
            else:
                attempts_word = "попыток"
        
            print(f'\nПоздравляю, Вы угадали за {count} {attempts_word}!')
            
            
            # Предложение сыграть еще раз
            while True:
                play_again = input('\nХотите сыграть еще раз? (да/нет): ').lower()
                
                if play_again in ('да'):
                    print("Отлично! Начинаем новую игру!")
                    break
                elif play_again in ('нет'):
                    print('\nСпасибо за игру! До новых встреч!')
                    exit()
                else:
                    print('Пожалуйста, введите "да" или "нет"') 
            
            break
          