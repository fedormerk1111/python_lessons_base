"""
Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b и выводить
одно натуральное число — номер дня.

Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22

Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""

a = float(input("Введи расстояние первого дня: "))
b = float(input("Введи целевое расстояние: "))

if a < b:
    day_count = 1
    day_result = a
    while day_result < b:
        day_result = day_result * 1.1
        day_count += 1
        print(f"День = {day_count}; Расстояние = {day_result}")
    print(f"Цель будет достигнута на {day_count}-й день")
else:
    print(f"Цель была достигнута")
