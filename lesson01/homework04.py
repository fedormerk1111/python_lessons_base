"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

'''
user_num = list(input("Введи число: "))

index = 1
result = user_num[0]

while index < len(user_num):
    if user_num[index] > result:
        result = user_num[index]
    index += 1

print(result)
'''

user_input = input("Введите число: ")

if not user_input.isdigit():
    print("invalid_format")
    exit()

number = int(user_input)
max_num = 0

while number and max_num != 9:
    print(number)
    current = number % 10
    number //= 10
    max_num = current if current > max_num else max_num

print(max_num)
