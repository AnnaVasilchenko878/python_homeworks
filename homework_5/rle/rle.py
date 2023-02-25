# Реализуйте RLE алгоритм: реализуйте модуль сжатия данных.

def get_string(get_file):
    path = get_file
    data = open(path, 'r', encoding='utf-8')
    for line in data:
        current_string = line
    data.close()
    return current_string

def rle_encode(current_string):
    result = ''
    char = current_string[0]
    count = 0
    index = 0

    while count < len(current_string):
        if char == current_string[count]:
            index += 1
        else:
            result += str(index) + char
            index = 0
            char = current_string[count]
        count += 1
    return result


def write_result(write_file, result):
    path = write_file
    data = open(path, 'w', encoding='utf-8')
    data.writelines(result)
    data.close()


current_string = get_string('rle_input.txt')
result = rle_encode(current_string)
write_result('rle_result.txt', result)
