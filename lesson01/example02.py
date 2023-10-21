# password = input("Введите пароль >>> ")
#
# original_password = "correct"
#
# if original_password == password:
#     print("Верно")
# else:
#     print("Неверно")

age = int(input("Введите ваш возраст >>> "))

if age >= 14:
    print("Пасспорт можно получить")

    if 20 <= age < 45:
        print("Пасспорт можно поменять")
elif age < 1:
    print("Custom")
else:
    print("Пасспорт нельзя получить")
