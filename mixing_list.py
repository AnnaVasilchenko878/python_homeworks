# Реализуйте алгоритм перемешивания списка.
import random
numbers = [1, 2, 3, 4, 5]
numbers_lenght = len(numbers)
count = 0
while count < numbers_lenght:
    index_random = random.randint(0, numbers_lenght-1)
    temp = numbers[count]
    numbers[count] = numbers[index_random]
    numbers[index_random] = temp
    count += 1

print(numbers)
