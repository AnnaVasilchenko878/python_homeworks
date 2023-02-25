# Реализуйте RLE алгоритм: реализуйте модуль восстановления данных.

def get_string(get_file):
    path = get_file
    data = open(path, 'r', encoding='utf-8')
    for line in data:
        current_string = line
    data.close()
    return current_string

def sort_numbers(current_string):
  numbers_list = []
  count = 0
  while count<len(current_string):
      if count%2 == 0:
        numbers_list.append(int(current_string[count]))
      count +=1
  return numbers_list

def sort_char(current_string): 
  char_list = []
  count = 0
  while count<len(current_string):
    if count%2 != 0:
      char_list.append(current_string[count])
    count += 1
  return char_list


def recovery_string(numbers_list, char_list):
  count = 0
  index = 0
  result = ''
  while count < len(numbers_list): 
    while index < numbers_list[count]:
      result +=char_list[count]
      index +=1
 
    index = 0
    count +=1

  return result
  

def write_result(write_file, result):
    path = write_file
    data = open(path, 'w', encoding='utf-8')
    data.writelines(result)
    data.close()

current_string = get_string('rle_input_reverse.txt')
numbers_list = sort_numbers(current_string)
char_list = sort_char(current_string)
result = recovery_string(numbers_list,char_list)
write_result('rle_result_reverse.txt', result)
