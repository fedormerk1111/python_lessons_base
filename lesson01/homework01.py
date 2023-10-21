"""
Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя
несколько чисел и строк и сохраните в переменные, выведите на экран.
"""

string_value = 'Делааа...'
int_value = 17

print(string_value, int_value)

user_string_value = input("Введите строку: ")
user_int_value_1 = int(input("Введите число: "))
user_int_value_2 = int(input("Введите число: "))

print(f"Была введена строка '{user_string_value}', первое число: {user_int_value_1}, второе число: {user_int_value_2}")
