#  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def fill_numbers():
  diff = int(input('Введите разность элементов'))
  first_elem = int(input('Введите первый элемент'))
  array_len = int(input('Введите количество элементов'))
  numbers = []
  count = 0

  while count < array_len:
    numbers.append(first_elem + count * diff)
    count +=1

  return numbers

print(fill_numbers())