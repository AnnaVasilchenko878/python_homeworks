# Задайте список из N элементов, заполненных числами из промежутка[-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

number_current = int(input('Введите число: '))
numbers_list = []
count = -number_current
while count<=number_current:
  numbers_list.append(count)
  count+=1

path_file = 'file.txt'
data_numbers = open(path_file, 'r')

indexes_list = []
result = 1
for i in data_numbers:
  indexes_list.append(int(i))
data_numbers.close()

result =1
for j in indexes_list:
  result *=numbers_list[j]
print('Произведение чисел из заданного файла равно: ',result)