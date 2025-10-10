import random

def main():
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Сначала задайте диапазон чисел.")


    while True:
        try:
            start = int(input("Введите начало диапазона: "))
            end = int(input("Введите конец диапазона: "))
            if start >= end:
                print("Начало диапазона должно быть меньше конца. Попробуйте снова.")
                continue
            break
        except ValueError:
            print("Введите целые числа!")


    secret = random.randint(start, end)
    attempts = 0

    print(f"\nЯ загадал число от {start} до {end}. Попробуй угадать!\n")


    while True:
        try:
            guess = int(input("Твой вариант: "))
            attempts += 1

            if guess < secret:
                print("Мое число больше!")
            elif guess > secret:
                print("Мое число меньше!")
            else:
                print(f"Поздравляю! Ты угадал число {secret} за {attempts} попыток!")
                break
        except ValueError:
            print("Введите целое число!")

if __name__ == "__main__":
    main()
