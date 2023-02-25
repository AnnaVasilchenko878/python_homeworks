# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# Входные и выходные данные хранятся в отдельных текстовых файлах.
def get_string():
    path = 'words_input.txt'
    data = open(path, 'r', encoding='utf-8')
    for line in data:
        current_string = line
    data.close()
    return current_string


def del_words(current_string):
    words = current_string.split(' ')
    temp = []
    for word in words:
        if ('Абв' or 'абв') not in word:
            temp.append(word)
    new_string = ' '.join(temp)
    return new_string


def write_result(result):
    path = 'words_result.txt'
    data = open(path, 'w', encoding='utf-8')
    data.writelines(result)
    data.close()


current_string = get_string()
new_string = del_words(current_string)
write_result(new_string)
