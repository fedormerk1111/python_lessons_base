"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь
ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

'''
user_num = input("Введи число: ")       # Решение через сложение строк и преобразование сложенных строк в числа

num_1 = int(user_num)
num_2 = int(user_num * 2)
num_3 = int(user_num * 3)

print(f"{num_1} + {num_2} + {num_3} = {num_1 + num_2 + num_3}")
'''

user_input = input("Введи число: ")  # Решение через умножение

if not user_input.isdigit():
    print("Неверный формат")
    exit()

user_number = int(user_input)
characters_count = 0
temp_number = user_number

while temp_number:
    temp_number //= 10
    characters_count += 1

first_level_multiplication = (10 ** characters_count) + 1
second_level_multiplication = (10 ** (characters_count * 2)) + first_level_multiplication

result = user_number + (user_number * first_level_multiplication) + (user_number * second_level_multiplication)

print(f"{user_number} + {user_number * first_level_multiplication} + {user_number * second_level_multiplication} = {result}")
