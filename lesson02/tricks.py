# 1 - объединение списков
nums = [
    [1, 2, 3],
    [1, 2, 3]
]

joined_list = sum(nums, [])

print(joined_list)


# 2 - удаление дубликатов
unique = [1, 2, 3, 3]
unique = list(set(unique))


# 3 - обмен значениями переменных
a = 10
b = 20

a, b = 10, 20   # то же самое, что и вышее

a, b = b, a


# 4 - посчитать, какой элемент в списке встречается чаще всего
total = [1, 2, 2, 2, 3, 3]
print(
    max(
        set(total),
        key=total.count
    )
)


# 5 - распаковка для отображения
print(*total, end='', sep='-')
