import random


def rock_paper_scissors():
    user_choice = input('Выбери камень, ножницы или бумага. ')
    computer_choice = random.choice(['камень', 'ножницы', 'бумага'])
    print('Компьютер выбрал ', computer_choice)
    if user_choice == computer_choice:
        print('Ничья! ')

    elif (user_choice == 'камень' and computer_choice == 'ножницы') or (user_choice == 'ножницы' and computer_choice == 'бумага') or (user_choice == 'бумага' and computer_choice =='камень'):
        print('Пам-пам! Победа!')
    else:
        print('Тебя сделали...')


def guess_number():
    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        user_number = int(input("Угадай число от 1 до 100: "))
        attempts += 1

        if user_number == target_number:
            print(f"Поздравляю, ты угадал число за {attempts} попыток!")
            break
        elif user_number < target_number:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")


# Главная функция
def main():
    while True:
        game_choice = input("Выбери игру: 1 - Камень, ножницы, бумага, 2 - Угадай число, 0 - Выход: ")

        if game_choice == '1':
            rock_paper_scissors()
        elif game_choice == '2':
            guess_number()
        elif game_choice == '0':
            break
        else:
            print("Некорректный выбор. Попробуйте ещё раз.")


# Запуск игры
if __name__ == "__main__":
    main()


