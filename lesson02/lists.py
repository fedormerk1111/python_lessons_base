numbers = [4, 8, 15, 16, 23, 42]

numbers.append(108)
print(numbers)

numbers.remove(16)
print(numbers)

numbers.append(15)
print(numbers)
print(numbers.count(15))

numbers.extend([20, 30, 40])

new_list = [20, 30, 40]
new_list.extend(numbers)
print(new_list)

new_list.sort()
print(new_list)
