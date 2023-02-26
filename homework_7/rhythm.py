# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов(т.е. число  гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.
# Ввод: пара-ра-рам рам-пам-папам па-ра-па-дам
# Вывод: Парам пам-пам


def get_phrases():
    phrases_list = []
    for i in range(3):
        phrases = input('Введите фразу: ').replace(' ', '-')
        phrases_list.append(phrases)
    return phrases_list


def is_rhythm(phrase_list):
    vowels_count = []
    vowels_list = ['я', 'и', 'ю', 'а', 'о', 'э', 'у', 'е', 'ё', 'ы']
    for phrase in range(len(phrase_list)):
        count = 0
        for i in range(len(phrase_list[phrase])):
            if phrase_list[phrase][i] in vowels_list:
                count += 1
        vowels_count.append(count)
    return vowels_count


def rhythm_result(vowels_count):
    temp = vowels_count[0]
    for i in range(len(vowels_count)):
        if temp == vowels_count[i]:
            is_rhythm = True
        else:
            is_rhythm = False

    if is_rhythm:
        print('Парам пам-пам')
    else:
        print('Пам парам')


phrases_list = get_phrases()
vowels_count = is_rhythm(phrases_list)
rhythm_result(vowels_count)