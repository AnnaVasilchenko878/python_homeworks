# # Определить индексы элементов массива(списка), значения которых принадлежат заданному диапазону(т.е. не меньше заданного минимума и не больше заданного максимума)
import random


def fill_array():
    numbers = []
    for i in range(10):
        numbers.append(random.randint(0, 50))
    return numbers


numbers = fill_array()


def input_index(numbers):
    start_index = int(input('Введите число начало диапазона: '))
    end_index = int(input('Введите число конца диапазона: '))
    if 10 > start_index >= 0 and 10 > end_index >= 0:
        while start_index < end_index:
            print(numbers[start_index])
            start_index += 1


input_index(numbers)
