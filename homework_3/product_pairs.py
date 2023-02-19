# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

list_numbers = [2, 3, 4, 5, 6]
list_product = []
count = 0
if len(list_numbers) % 2 == 0:
    while count < len(list_numbers)//2:
        result = list_numbers[count] * list_numbers[len(list_numbers)-count-1]
        list_product.append(result)
        count += 1
    print(list_product)
else:
    while count < len(list_numbers)//2+1:
        result = list_numbers[count] * list_numbers[len(list_numbers)-count-1]
        list_product.append(result)
        count += 1
    print(list_product)
