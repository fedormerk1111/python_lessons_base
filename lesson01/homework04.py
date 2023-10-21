"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

user_num = list(input("Введи число: "))

index = 1
result = user_num[0]

while index < len(user_num):
    if user_num[index] > result:
        result = user_num[index]
    index += 1

print(result)
