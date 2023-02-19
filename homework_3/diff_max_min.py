# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

numbers = [1.1, 1.2, 3.1, 5, 10.01]
remainders = []
remainder = 0
for i in numbers:
    digit = int(i)
    remainder = round(i-digit, 2)
    if remainder > 0:
        remainders.append(remainder)
print('Разница между максимальным и минимальным значением дровной части равна: ',
      max(remainders) - min(remainders))
