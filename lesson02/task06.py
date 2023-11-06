"""
*Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть
два элемента — номер товара и словарь с параметрами (характеристиками товара: название,
цена, количество, единица измерения). Структуру нужно сформировать программно,
т.е. запрашивать все данные у пользователя.
Пример готовой структуры:

[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый
ключ — характеристика товара, например название, а значение — список значений-характеристик,
например список названий товаров.
Пример:

{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""


specification = {"название": str, "цена": str, "кол-во": str, "ед": str}
temp_list = []
result_list = []
name_list =[]
price_list =[]
quantity_list =[]
unit_list =[]

try:
    while True:
        for item in specification:
            specification[item] = input(f"{item}: ")
        print(specification)    # для теста
        temp_list.append(specification.copy())
except KeyboardInterrupt:
    for index, item in enumerate(temp_list):
        user_tuple = (index + 1, item)
        result_list.append(user_tuple)
    print("")
    print(result_list)    # для теста

    for tuple_item in result_list:
        temp_dict = tuple_item[1]
        name_list.append(temp_dict.get("название"))
        price_list.append(temp_dict.get("цена"))
        quantity_list.append(temp_dict.get("кол-во"))
        unit_list.append(temp_dict.get("ед"))

    name_list = list(set(name_list))
    price_list = list(set(price_list))
    quantity_list = list(set(quantity_list))
    unit_list = list(set(unit_list))

    specification = {"название": name_list, "цена": price_list, "кол-во": quantity_list, "ед": unit_list}
    print(specification)
