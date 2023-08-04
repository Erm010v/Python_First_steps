# Задача_49:

# Создать телефонный справочник с возможностью импорта и экспорта
# данных в формате .txt. Фамилия, имя, отчество, номер телефона
#  - данные, которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для
# поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

''' 
from view import (show_menu, print_result, get_search_name,
                  get_search_number, get_new_user, get_file_name)
from model import write_txt, write_csv, read_csv, find_by_name, find_by_number, add_user


+  возможность изменения и удаления данных
'''

# Решение_1 Работа с выделением таблицы и цифр цветами:
'''
from tabulate import tabulate


def bold_green(str):
    return "\033[1m\033[92m" + str + "\033[0m"


def header_color(str):
    return "\033[95m" + str + "\033[0m"


def red(str):
    return "\033[91m" + str + "\033[0m"


def show_menu():
    print("\nВыберите необходимое действие:",
          bold_pink("1") + ". Отобразить весь телефонный справочник",
          bold_pink("2") + ". Найти абонента по Фамилии",
          bold_pink("3") + ". Найти абонента по номеру телефона",
          bold_pink("4") + ". Добавить абонента в справочник",
          bold_pink("5") + ". Удалить абонента по номеру телефона",
          bold_pink("6") + ". Изменить абонента по номеру телефона",
          bold_pink("9") + ". Сохранить справочник в текстовом формате",
          bold_pink("0") + ". Закончить работу",
          sep="\n")
    choice = int(input())
    return choice


def write_csv(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ' '
            for v in data[i].values():
                s += v + ','
                fout.write(f'{s[:-1]}\n')

# построчное чтение из файла csv


def read_csv(filename: str) -> list:
    data = []

    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields(), line.strip().split(',')))
            data.append(record)
    return data


def write_phonebook(phone_book):
    write_csv('phonebook.csv', phone_book)


def fields():
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]


def get_file_name():
    return "phon.txt"


def write_txt(filename: str, data: list):
    write_csv(filename, data)


def headers_result():
    return [header_color("N")] + [header_color(x) for x in fields]


def print_result(phone_book):
    # выводится в tabulate списки списков
    # выводится нумерация в таблицу list(enumerate(phone_book)
    print(tabulate(list(map(lambda x: [x[0] + 1] + [y for y in x[1].values()], list(enumerate(phone_book)))),
                   headers=headers_result(),
                   tablefmt="rounded_grid"))


def print_search_result(search_result):
    print_result(search_result) if search_result else print(
        red("Абонент не найден"))


def get_search_name():
    return input("Введите Фамилию\n").strip()


def get_search_number():
    return input(" Введите Номер Телефона\n").strip()


def find_by_name(phone_book, name):
    for record in phone_book:
        if record["Фамилия"].lower() == name.lower():
            return record
        return "Не найден"


def find_by_number(phone_book, number):
    return find_by_field(phone_book, "Телефон", number)


def find_by_field(phone_book, field, value):
    # создание пустого списка куда закидываются записи
    result = []
    for record in phone_book:
        if record[field].lower() == value.lower():
            result.append(record)
        return result


def find_index_by_number(phone_book, number):
    return find_index_by_field(phone_book, "Телефон", number)


def find_index_by_field(phone_book, field, value):
    for index in range(len(phone_book)):
        if phone_book[index][field].lower() == value.lower():
            return index
    return -1


def get_new_user():
    user = dict()
    for field in fields():
        user[field] = input(field + "\n")
    return user


def add_user(phone_book: list, user_data):
    phone_book.append(user_data)


def del_user(phone_book: list, index: int):
    if index < 0:
        print(red("Абонент не найден"))
        return False, phone_book
    return True, phone_book[:index] + phone_book[index + 1:]


def change_user(phone_book):
    index = find_index_by_number(phone_book, get_search_number())
    if index < 0:
        print(red("Абонент не найден"))
        return False, phone_book
    print("Введите новые данные абонента")
    return True, change_record(phone_book, index, get_new_user())


def change_record(phone_book, index, record):
    return phone_book[:index] + [record] + phone_book[index + 1:]


def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('phonebook.csv')


while (choice != 0):
    if choice == 1:
        print_result(phone_book)
    elif choice == 2:
        name = get_search_name()
        print_search_result(find_by_name(phone_book, name))
    elif choice == 3:
        number = get_search_number()
        print_search_result(find_by_number(phone_book, number))
    elif choice == 4:
        user_data = get_new_user()
        add_user(phone_book, user_data)
        write_phonebook(phone_book)
    elif choice == 5:
        number = get_search_number()
        modified, phone_book = del_user(phone_book, find_index_by_number(phone_book, number))
        if modified:
            write_phonebook(phone_book)
    elif choice == 6:
         modified, phone_book = change_user(phone_book)
        if modified:
            write_phonebook(phone_book)
    elif choice == 9:
        file_name = get_file_name()
        write_txt(file_name, phone_book)
    choice = show_menu()

work_with_phonebook()
'''

# Решение_2:
'''
def choose_action(phonebook):
    while True:
        print('Что вы хотите сделать?')
        user_choice = input('1 - Импортировать данные\n2 - Найти контакт\n3 - Добавить контакт\n\
4 - Изменить контакт\n5 - Удалить контакт\n6 - Просмотреть все контакты\n0 - Выйти из приложения\n')
        print()
        if user_choice == '1':
            file_to_add = input('Введите название импортируемого файла: ')
            import_data(file_to_add, phonebook)
        elif user_choice == '2':
            contact_list = read_file_to_dict(phonebook)
            find_number(contact_list)
        elif user_choice == '3':
            add_phone_number(phonebook)
        elif user_choice == '4':
            change_phone_number(phonebook)
        elif user_choice == '5':
            delete_contact(phonebook)
        elif user_choice == '6':
            show_phonebook(phonebook)
        elif user_choice == '0':
            print('До свидания!')
            break
        else:
            print('Неправильно выбрана команда!')
            print()
            continue


def import_data(file_to_add, phonebook):
    try:
        with open(file_to_add, 'r', encoding='utf-8') as new_contacts, open(phonebook, 'a', encoding='utf-8') as file:
            contacts_to_add = new_contacts.readlines()
            file.writelines(contacts_to_add)
    except FileNotFoundError:
        print(f'{file_to_add} не найден')


def read_file_to_dict(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    headers = ['Фамилия', 'Имя', 'Номер телефона']
    contact_list = []
    for line in lines:
        line = line.strip().split()
        contact_list.append(dict(zip(headers, line)))
    return contact_list


def read_file_to_list(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        contact_list = []
        for line in file.readlines():
            contact_list.append(line.split())
    return contact_list


def search_parameters():
    print('По какому полю выполнить поиск?')
    search_field = input('1 - по фамилии\n2 - по имени\n3 - по номеру телефона\n')
    print()
    search_value = None
    if search_field == '1':
        search_value = input('Введите фамилию для поиска: ')
        print()
    elif search_field == '2':
        search_value = input('Введите имя для поиска: ')
        print()
    elif search_field == '3':
        search_value = input('Введите номер для поиска: ')
        print()
    return search_field, search_value


def find_number(contact_list):
    search_field, search_value = search_parameters()
    search_value_dict = {'1': 'Фамилия', '2': 'Имя', '3': 'Номер телефона'}
    found_contacts = []
    for contact in contact_list:
        if contact[search_value_dict[search_field]] == search_value:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print('Контакт не найден!')
    else:
        print_contacts(found_contacts)
    print()


def get_new_number():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    return last_name, first_name, phone_number


def add_phone_number(file_name):
    info = ' '.join(get_new_number())
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{info}\n')


def show_phonebook(file_name):
    list_of_contacts = sorted(read_file_to_dict(file_name), key=lambda x: x['Фамилия'])
    print_contacts(list_of_contacts)
    print()
    return list_of_contacts


def search_to_modify(contact_list: list):
    search_field, search_value = search_parameters()
    search_result = []
    for contact in contact_list:
        if contact[int(search_field) - 1] == search_value:
            search_result.append(contact)
    if len(search_result) == 1:
        return search_result[0]
    elif len(search_result) > 1:
        print('Найдено несколько контактов')
        for i in range(len(search_result)):
            print(f'{i + 1} - {search_result[i]}')
        num_count = int(input('Выберите номер контакта, который нужно изменить/удалить: '))
        return search_result[num_count - 1]
    else:
        print('Контакт не найден')
    print()


def change_phone_number(file_name):
    contact_list = read_file_to_list(file_name)
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    print('Какое поле вы хотите изменить?')
    field = input('1 - Фамилия\n2 - Имя\n3 - Номер телефона\n')
    if field == '1':
        number_to_change[0] = input('Введите фамилию: ')
    elif field == '2':
        number_to_change[1] = input('Введите имя: ')
    elif field == '3':
        number_to_change[2] = input('Введите номер телефона: ')
    contact_list.append(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)


def delete_contact(file_name):
    contact_list = read_file_to_list(file_name)
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)


def print_contacts(contact_list: list):
    for contact in contact_list:
        for key, value in contact.items():
            print(f'{key}: {value:12}', end='')
        print()


if __name__ == '__main__':
    file = 'Phonebook.txt'
    choose_action(file)
'''
