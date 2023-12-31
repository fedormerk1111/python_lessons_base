"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с
тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""

my_list = [7, 5, 3, 3, 2]

while True:
    user_input = input("Введи число: ")
    if user_input != "!":
        if not user_input.isdigit():
            print("Только целые числа!!!")
            continue
        else:
            user_num = int(user_input)

            my_list.append(user_num)
            my_list.sort(reverse=True)
            print(*my_list, sep=", ")
    else:
        print(f"Результат: ", end='')
        print(*my_list, sep=", ")   # * = распаковка для отобоажения (без скобок и запятых)
        exit()