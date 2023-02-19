# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# 45 -> 101101
# 3 -> 11
# 2 -> 10

current_number = 2
binary_numbers = ''
while current_number > 0:
    binary_numbers = str(current_number % 2) + binary_numbers
    current_number //= 2
print(binary_numbers)
