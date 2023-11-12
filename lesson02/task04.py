"""
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""

user_list = input("Вводи: ").split()
print(user_list)

# for count, item in enumerate(user_list):
#     print(f"{count + 1}. {item[:10]}")

for count, item in enumerate(user_list, start=1):
    print(f"{count}. {item[:10]}")
