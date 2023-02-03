# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

number = int(input('Введите число: '))
numbers = []
sum_numbers = 0
count = 1
while count <= number:
    numbers.append(round(1+1/count)**count)
    count += 1
for i in numbers:
    sum_numbers += i
print('Сумма чисел: ', sum_numbers)
