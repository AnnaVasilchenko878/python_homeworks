# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

current_list = [1,2,3,4,2,3,4,5]
new_list = []

for i in current_list: 
  if i not in new_list:
    new_list.append(i)
print(new_list)
