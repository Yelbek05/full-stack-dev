# 1. **Конвертация температуры**
#     - Напиши программу, которая принимает температуру в Цельсиях и переводит её в Фаренгейты.
# 2. **Чётное или нечётное**
#     - Напиши программу, которая принимает число от пользователя и выводит, чётное оно или нечётное.
# 4. **Игра "Угадай число"**
#     - Напиши программу, которая генерирует случайное число и позволяет пользователю его угадать, сообщая, больше или меньше загаданное число.

# №1
# a = float(input("In Celsius(C): "))
# f = (a * 1.8) + 32 #1.8 = 9 / 5
# print(f'{a}C in Fahrenhit {f}')

# №2
# a = int(input("Number: "))
# if a % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# №4
# import random
# r_n = random.randint(1, 100)
# print("Generated the number, GUESS NOW!")

# while True:
#     a = int(input())
#     if a > r_n :
#         print("Too Much")
#     elif a < r_n:
#         print("Too Little")
#     else:
#         print("You guessed the Number!!!")
#         break
