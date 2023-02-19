# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

numbers_list = [2, 3, 5, 9, 3]
if len(numbers_list) == 0:
    print('Список пуст')
else:
    count = 0
    sum_numbers = 0
    while count < len(numbers_list):
        if count % 2 != 0:
            sum_numbers += numbers_list[count]
        count += 1
    print('Сумма чисел стоящих на нечетной позиции равна: ', sum_numbers)
