# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def simple_milt(number):
  count = 2
  list_divisor = []
  while count <=number:
    if number%count == 0:
      list_divisor.append(count)
      number //= count
    else:
      count +=1
  return list_divisor

print(simple_milt(52))



