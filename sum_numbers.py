# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
number_current = input('Введите число: ').replace('.', '0')
digit_list = list(number_current)
result = 0
for i in digit_list:
    i = int(i)
    result += i
print(result)
