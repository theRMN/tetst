documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def search_person(documents, user_input=None):
    if user_input is None:
        user_input = input('Введите номер документа: ')
    else:
        user_input = '10006'

    name = ''

    for doc in documents:
        if doc['number'] == user_input:
            name = doc['name']
    if name == '':
        print('\nДокумент с таким номером не найден в базе')
    else:
        return print('\n' + 'ФИО -', name)


def search_shelf(directories, user_input=None):
    if user_input is None:
        user_input = input('Введите номер документа: ')
    else:
        user_input = '10006'

    directory = ''

    for number_list in directories.items():
        for number in number_list[1]:
            if number == user_input:
                directory = number_list[0]
    if directory == '':
        print('\nДокумент с таким номером не найден в базе')
    else:
        return print('\n' + 'Документ находится на полке №' + directory)


def doc_list_print(documents):
    print('\nСписок документов:')
    doc_list = []
    for doc in documents:
        doc = (doc['type'], '"' + doc['number'] + '"', '"' + doc['name'] + '"')
        doc_list.append(doc)
    return print(doc_list)


def doc_add(documents, directories, doc_type=None, doc_number=None, directory_number=None, doc_name=None):
    number_list = []
    document = {}
    documents.append(document)

    if directory_number is None:
        directory_number = input('Введите номер полки: ')
    else:
        directory_number = '2'

    for number in directories:
        number_list.append(number)

    if directory_number not in number_list:
        doc_number_list = []
        if doc_type is None and doc_number is None:
            doc_type = input('Введите тип документа: ')
            doc_number = input('Введите номер документа: ')
        else:
            doc_type = 'passport'
            doc_number = '5555555'
        doc_number_list.append(doc_number)
        if doc_name is None:
            doc_name = input('Введите ФИО: ')
        else:
            doc_name = 'Ivan Ivanovich'

        directories[directory_number] = doc_number_list + directories[directory_number]

        document['type'] = doc_type
        document['number'] = doc_number
        document['name'] = doc_name
        print('\nТакой полки не существует')
    else:
        return print('\nДокумент успешно добавлен')


def doc_delete(documents, directories, user_input=None):
    if user_input is None:
        user_input = input('Введите номер документа: ')
    else:
        user_input = '10006'

    doc_number_list = []

    for doc_dict in documents:
        doc_number_list.append(doc_dict['number'])
        if doc_dict['number'] == user_input:
            documents.remove(doc_dict)

    if user_input not in doc_number_list:
        for dir_list in directories.items():
            if user_input in dir_list[1]:
                dir_list[1].remove(user_input)
        print('\nДокумент с таким номером не найден в базе')
    else:
        return print('\nДокумент успешно удалён')


def doc_move(directories, input_doc_number=None, input_shelf_number=None):
    doc_number_list = []
    shelf_key_list = []

    if input_doc_number is None:
        input_doc_number = input('Введите номер документа: ')
    else:
        input_doc_number = '10006'

    for shelf_key, shelf_number in directories.items():
        shelf_key_list.append(shelf_key)
        if input_doc_number in shelf_number:
            doc_number_list.append(input_doc_number)

    result = ''

    if input_doc_number == ''.join(doc_number_list):

        if input_shelf_number is None:
            input_shelf_number = input('Введите номер полки: ')
        else:
            input_shelf_number = '3'

        if input_shelf_number in shelf_key_list:
            for shelf_number in directories.values():
                if input_doc_number in shelf_number:
                    shelf_number.remove(input_doc_number)
            directories[input_shelf_number] = doc_number_list + directories[input_shelf_number]
            result = ('\nДокумент с номером', '"' + input_doc_number + '"',
                      'успешно перемещён на полку №' + input_shelf_number)
        else:
            print('\nПолка с таким номером не существует')
    else:
        print('\nДокумент с таким номером не найден в базе')
    return print(result)


def shelf_add(directories, new_shelf=None):
    shelf_number_list = []

    if new_shelf is None:
        new_shelf = input('Введите номер новой полки: ')
    else:
        new_shelf = '4'

    for shelf_number in directories:
        shelf_number_list.append(shelf_number)

    if new_shelf in shelf_number_list:
        directories[new_shelf] = []
        print('\nПолка с таким номером уже существует')
    else:
        return print('\n Полка №' + new_shelf, 'успешно создана')


def initialize():
    print('Пользовательские команды:\n'
          + 'p - ищет ФИО по номеру документа\n'
          + 's - ищет полку по номеру документа\n'
          + 'l - выводит список документов\n'
          + 'a - добавляет документ\n'
          + 'd - удаляет документ по номеру\n'
          + 'm - переносит указаный документ на указаную полку\n'
          + 'as - добавляет указаную полку\n'
          + 'e - завершает работу программы')

    while True:
        user_input = input('\nВведите команду: ')
        if user_input == 'p':
            search_person(documents)
        elif user_input == 's':
            search_shelf(directories)
        elif user_input == 'l':
            doc_list_print(documents)
        elif user_input == 'a':
            doc_add(documents, directories)
        elif user_input == 'd':
            doc_delete(documents, directories)
        elif user_input == 'm':
            doc_move(directories)
        elif user_input == 'as':
            shelf_add(directories)
        elif user_input == 'e':
            break
        else:
            print('\nНеправильная команда')
    return


if __name__ == '__main__':
    initialize()
