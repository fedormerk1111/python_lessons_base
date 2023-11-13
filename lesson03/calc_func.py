def calculate(salary):
    try:
        return salary - (salary * .13)
    except TypeError:
        return  # то же самое, что return None


# salary_1 = 100

salary_1 = 'test'

print(salary_1, calculate(salary_1))

