# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
#Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

number = int(input('Введите число: '))
numbers = []
sum =0
count = 1
while count<=number:
  numbers.append(round((1+1/count)**count,2))
  count+=1
print('Последовательность чисел: ', numbers)
for i in numbers:
  sum +=i
print('Сумма чисел: ', sum)

