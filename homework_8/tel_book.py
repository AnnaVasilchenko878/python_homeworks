# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
# 5. Дополнить телефонный справочник возможностью изменения и удаления данных(удаление строк)
# 6. Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал изменения 


from pathlib import Path

# получает данные из книги в многомерный массив

def get_subscribe_data():
    temp_list = []
    subscribe_list = []
    with open('D:\\Anna\\lessons\\geek_brains\\python\\homeworks\\homework_8\\data_book.txt', 'r', encoding='utf-8') as data_book:
        for i in data_book:
            temp_list.append(i.strip())

        subscribe_size = len(temp_list)//4
        for i in range(0, len(temp_list)-1, len(temp_list)//subscribe_size):
            temp = slice(i, i+len(temp_list)//subscribe_size)
            subscribe_list.append(temp_list[temp])

    return subscribe_list


# показывает данные книги
def print_subscribe_data(subscribe_data):
    for subscribe in subscribe_data:
        print(*subscribe)


# пользователь вводит новые данные
def input_new_subscribe():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    patronymic = input('Введите Отчество: ')
    number_tel = input('Введите номер телефона: ')

    return name, surname, patronymic, number_tel


# поиск данных по книге
def search_subscribe_data(subscribe_data):
    search_result = []
    search_subscribe_data = input('Введите данные для поиска: ')
    for subscribe in subscribe_data:
        if search_subscribe_data in subscribe:
            search_result.append(subscribe)

    return search_result

# проверка если нет данных и вывод имеющихся


def search_result_print(search_result):
    if len(search_result) != 0:
        print_subscribe_data(search_result)
    else:
        print('Таких данных не существует')


# изменение данных
def change_subscribe_data(subscribe_data):
    change_data = []
    old_data = input('Введите данные которые хотите изменить: ')
    new_data = input('Введите новые данные: ')
    for subscribe in subscribe_data:
        for i in range(len(subscribe)):
            if old_data in subscribe:
                subscribe[i] = new_data

    for i in range(len(subscribe_data)):
        change_data += subscribe_data[i]

    return change_data


def delete_subscribe_data(subscribe_data):
    new_data = []
    delete_data = input('Введите данные которые хотите удалить: ')
    temp = 0
    for subscribe in range(len(subscribe_data)):
        if delete_data in subscribe_data[subscribe]:
            temp = subscribe

    subscribe_data.remove(subscribe_data[temp])

    for i in range(len(subscribe_data)):
        new_data += subscribe_data[i]
    return new_data


def write_subscribe_data(subscribe_data, mode):
    with open('D:\\Anna\\lessons\\geek_brains\\python\\homeworks\\homework_8\\data_book.txt', mode, encoding='utf-8') as data_book:
        for i in subscribe_data:
            data_book.write(i + '\n')


def main():
    # получить данные из файла
    subscribe_data = get_subscribe_data()
    print('\n' + '-----------Меню справочника-----------' + '\n' +
          'Введите 1 чтобы посмотреть список контактов' + '\n' + 'Введите 2 чтобы добавить новый контакт' + '\n' + 'Введите 3 чтобы найти контакт' + '\n' + 'Введите 4 чтобы редактировать  контакт' + '\n' + 'Введите 5 чтобы удалить контакт')
    user_value = int(input('Введите номер команды: '))
    if user_value == 1:
       # показать данные книги
        print_subscribe_data(subscribe_data)
    elif user_value == 2:
        #    # ввести данные в тел книгу
        new_data = input_new_subscribe()
        confirm_new_subscribe = input('Сохранить данные? (Y/N): ')
        if confirm_new_subscribe == 'Y':
            write_subscribe_data(new_data, 'a')
            print('Данные успешно сохранены')
        else:
            print('Данные не сохранены')
    elif user_value == 3:
        search_result = search_subscribe_data(subscribe_data)
        search_result_print(search_result)
    elif user_value == 4:
        change_data = change_subscribe_data(subscribe_data)
        confirm_change = input('Сохранить данные? (Y/N): ')
        if confirm_change == 'Y':
            write_subscribe_data(change_data, 'w')
            print('Данные успешно изменены')
        else:
            print('Данные не изменены')
    elif user_value == 5:
        delete_data = delete_subscribe_data(subscribe_data)
        confirm_delete = input('Удалить эти данные? (Y/N): ')
        if confirm_delete == 'Y':
            write_subscribe_data(delete_data, 'w')
            print('Данные успешно сохранены')
        else:
            print('Данные не удалены')


def is_there_file():
    if Path('D:\\Anna\\lessons\\geek_brains\\python\\homeworks\\homework_8\\data_book.txt').is_file():
        main()
    else:
        print('Отсутствуют данные контактов')


is_there_file()
