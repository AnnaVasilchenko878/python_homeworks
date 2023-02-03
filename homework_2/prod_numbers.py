# Задайте список из N элементов, заполненных числами из промежутка[-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

# number = int(input('Введите число: '))
# numbers = []
# count = -number
# while count<=number:
#   numbers.append(count)
#   count+=1
# print(numbers)
numbers = [1,2,4,5,4]
path = 'file.txt'
data = open(path, 'r')

result = 1
for i in numbers:
  for j in data:
    result = result*
print(result)
data.close()

