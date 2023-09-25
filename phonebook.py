# Задача No49. Решение в группах
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате 
# .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной


def write_first_name():
    first_name = input('Введите имя: ')
    return first_name


def write_sur_name():
    sur_name = input('Введите Фамилию: ')
    return sur_name


def write_phone_number():
    phone_number = input('Введите номер телефона: ')
    return phone_number


def write_adress():
    adress = input('Введите адресс: ')
    return adress


def input_data(a=None):
    first_name = write_first_name()
    sur_name = write_sur_name()
    phone_number = write_phone_number()
    adress = write_adress()
    with open('phonebook.txt', 'a', encoding='utf-8') as data:
        data .write(f'{first_name} {sur_name}: {phone_number},{adress}\n\n')


# def input_data():
#     person = []
#     people = []
#     first_name = input('Введите имя: ')
#     person.append(first_name)
#     sur_name = input('Введите Фамилию: ')
#     person.append(sur_name)
#     phone_number = input('Введите номер телефона: ')
#     person.append(phone_number)
#     adress = input('Введите адресс: ')
#     person.append(adress)
#     people.extend(person)
#     with open('phonebook.txt', 'a', encoding='utf-8') as data:
#         data.write(f'{people}\n\n')


def print_data():
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        data_first = data.readlines()
        for line in data_first:
            print(line, end='')


def search_data():
    search = input('Введите данные для поиска: ')
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        temp = data.readlines()
        data_first = ''.join(temp).split('\n\n')[:-1]
        for line in data_first:
            if search in line:
                print(line)
     
                



def change_data():
    search = input('Введите данные для поиска: ')
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        temp = data.readlines()
        # data_first = read_file_to_list()
        # print(temp)
        data_first = ''.join(temp).split('\n\n')[:-1]
        for line in data_first:
            if search in line:
                old_line = line 
                print(old_line)
                new_first_name = write_first_name()
                new_sur_name = write_sur_name()
                new_phone_number = write_phone_number()
                new_adress = write_adress()
                # new_line = (f'{new_first_name} {new_sur_name}: {new_phone_number}\n{new_adress}\n\n')
                new_line = []
                new_line = [new_first_name + new_sur_name + new_phone_number + new_adress]
                print(new_line)
                line = line.replace(old_line, new_line)
                # data = data.replace()
                data.write(f'{new_first_name} {new_sur_name}: {new_phone_number}\n{new_adress}\n\n')
        return print(new_line)
                

def delete_data():
    search = input('Введите данные для поиска: ')
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        temp = data.readlines()
        print(temp)
        data_first = ''.join(temp).split('\n\n')[:-1]
        for line in data_first:
            if search in line:
                old_line = line 
                new_line = ''
                line = line.replace(old_line, new_line)
            data.write(line)
        return print('Данные удалены!')







def interface():
    command = "0"
    while command !='6':
        print('''Что вы хотите сделать?
            1 - Запись данных
            2 - Вывод данных
            3 - Поиск данных 
            4 - Изменение данных 
            5 - Удаление данных 
            6 - Выход ''')
        command = input('Введите номер опции: ')
        while command not in ('1','2','3','4'):
            print('Введите корретную команду!')
            command = input('Введите номер опции: ')
            
        if command == '1':
            input_data()
        elif command == '2':
            print_data()
        elif command == '3':
            search_data()
        elif command == '4':
            change_data()
        elif command == '5':
            delete_data()


interface()