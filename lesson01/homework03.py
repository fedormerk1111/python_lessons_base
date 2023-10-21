"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь
ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

'''
user_num = input("Введи число: ")       # Решение через сложение строк и преобразование сложенных строк в числа

num_1 = int(user_num)
num_2 = int(user_num + user_num)
num_3 = int(user_num + user_num + user_num)

print(f"{num_1} + {num_2} + {num_3} = {num_1 + num_2 + num_3}")
'''

user_num = int(input("Введи число: "))      # Решение через умножение

print(f"{user_num} + {user_num * 11} + {user_num * 111} = {user_num * 123}")
