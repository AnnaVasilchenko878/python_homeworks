# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def del_text(current_string):
    words = 'aбв'
    new_string = current_string.lower().replace(words, '')
    new_string = new_string[0].upper()+new_string[1:]
    return new_string


def get_string():
    path = 'words_input.txt'
    data = open(path, 'r', encoding='utf-8')
    for line in data:
        current_string = line
    data.close()
    return current_string


def write_result(result):
    path = 'words_result.txt'
    data = open(path, 'w', encoding='utf-8')
    data.writelines(result)
    data.close()


current_string = get_string()
new_string = del_text(current_string)
write_result(new_string)
