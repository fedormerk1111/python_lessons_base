"""
Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().
"""


user_input = 0
user_list = []

while True:
    user_input = input("Введи: ")
    if user_input != "!":
        user_list.append(user_input)
    else:
        break

print(user_list)

max_count = len(user_list) // 2
index = 0
count = 0

while count != max_count:
    user_list[index], user_list[index + 1] = user_list[index + 1], user_list[index]
    index += 2
    count += 1

print(user_list)
