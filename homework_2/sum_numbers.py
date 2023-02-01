# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
number = input('Введите число: ').replace('.', '0')
number = list(number)
result = 0
for i in number:
    i = int(i)
    result += i
print(result)
