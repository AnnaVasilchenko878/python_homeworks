# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('Введите число: '))
count = 1
result = 1
while count <= number:
    result *= count
    print(result)
    count += 1
