# Отгадай число
#
# Компьютер выбирает случайное число в диапазоне от 1 до 100
# Игрок пытается отгадать это число. и компьютер говорит.
# предположение больше/меньше. чем за.гаданное число.
# или попало в точку

import random

print("Добропожаловать в игру \"Случайное число!\"\n")
print("Попробуйте отгадать число от 1 до 10000\n\n")

the_number = random.randint(1, 10000)
guess = int(input("Ваше предположение: \n"))

tries = 1
while guess != the_number:
    if guess > the_number:
        print("Меньше...")
    elif guess < the_number:
        print("Больше...")
    guess = int(input("Ваше предположение: \n"))
    tries +=1
else:
    print("Вы выиграли, количество попыток: ",  tries)
