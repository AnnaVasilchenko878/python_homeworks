# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# k=8 [-21, 13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# 0 1 1 2 3 5 8 13

current_number = int(input('Введите число: '))


def pos_fibonacci(number):
    pos_fib_list = [0]
    if number == 0:
        return pos_fib_list
    elif number == 1:
        pos_fib_list.append(1)
        return pos_fib_list
    else:
        pos_fib_list.append(1)
        first_number = 0
        second_number = 1
        temp = 0
        while number > 1:
            temp = first_number
            first_number = second_number
            second_number = temp + second_number
            number -= 1
            pos_fib_list.append(second_number)
        return pos_fib_list


pos_fib_list = pos_fibonacci(current_number)


def neg_fibonacci(number):
    neg_fib_list = []
    if number == 0:
        return neg_fib_list
    elif number == 1:
        return neg_fib_list.append(1)
    else:
        first_number = 0
        second_number = 1
        temp = 0
        number = -number
        while number < -1:
            temp = first_number
            first_number = second_number
            second_number = temp - second_number
            number += 1
            neg_fib_list.insert(0, second_number)
        return neg_fib_list


neg_fib_list = neg_fibonacci(current_number)
print('Последовательность чисел: ', neg_fib_list + pos_fib_list)
