def multiplies(a, b):
    return a * b, b * a


result1, result2 = multiplies(b=1, a=2)    # именованные аргументы

result1, result2 = multiplies(1, 2) # распаковка -- если знаешь, что функция вернет два значения

print(result1, result2)
