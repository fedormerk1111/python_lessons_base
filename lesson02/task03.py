"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

user_input = input("Введи число от 1 до 12: ")

if not user_input.isdigit():
    print("Нужно число")
    exit()
else:
    user_input = int(user_input)

if user_input < 1 or user_input > 12:
    print("Нужно от 1 до 12")
    exit()

print(user_input)

# Решение через dict:

# year_dict = {"Зима": [12, 1, 2], "Весна": [3, 4, 5], "Лето": [6, 7, 8], "Осень": [9, 10, 11]}
#
# for key in year_dict:
#     for item in year_dict.get(key):
#         if item == user_input:
#             print(key)

# Решение через list:

spring = [3, 4, 5]
winter = [12, 1, 2]
summer = [6, 7, 8]
autumn = [9, 10, 11]

year = [spring, winter, summer, autumn]

for item in year:
    for int_month in item:
        if int_month == user_input:
            print(item)
