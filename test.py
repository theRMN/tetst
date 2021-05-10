from buh import documents, directories, search_person, search_shelf, doc_list_print
from buh import doc_add, doc_delete, doc_move, shelf_add
import requests
import pytest


class TestBookkeeping:
    def setup(self):
        print('method setup')

    def teardown(self):
        print('method teardown')

    def test_search_person(self):
        assert search_person(documents, '10006') == print('\n' + 'ФИО -', 'Аристарх Павлов')

    def test_search_shelf(self):
        assert search_shelf(directories, '10006') == print('\n' + 'Документ находится на полке №' + '2')

    def test_doc_list_print(self):
        doc_list = [('passport', '"2207 876234"', '"Василий Гупкин"'),
                    ('invoice', '"11-2"', '"Геннадий Покемонов"'),
                    ('insurance', '"10006"', '"Аристарх Павлов"')]
        assert doc_list_print(documents) == print(doc_list)

    def test_doc_add(self):
        assert doc_add(documents, directories,
                       doc_type='passport', doc_number='5555555',
                       directory_number='2', doc_name='Ivan Ivanovich') == print('\nДокумент успешно добавлен')

    def test_doc_delete(self):
        assert doc_delete(documents, directories, user_input='10006') == print('\nДокумент успешно удалён')

    def test_doc_move(self):
        assert doc_move(directories, input_doc_number='10006',
                        input_shelf_number='3') == print('\nДокумент с номером', '"' + '10006' + '"',
                                                         'успешно перемещён на полку №' + '3')

    def test_shelf_add(self):
        assert shelf_add(directories, new_shelf='4') == print('\n Полка №' + '4', 'успешно создана')


class TestRestAPI:

    def setup(self):
        print('method setup')

    def teardown(self):
        print('method teardown')

    @staticmethod
    def create_directory():
        ya_token = ''
        d_name = 'test'

        d_create = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                params={'path': d_name},
                                headers={'Authorization': ya_token}
                                )

        return d_create.status_code

    @staticmethod
    def check_folder():
        ya_token = ''
        d_path = ''

        directory = requests.get('https://cloud-api.yandex.net/v1/disk/resources',
                                 params={'path': '/'},
                                 headers={'Authorization': ya_token})

        for dd in directory.json()['_embedded']['items']:
            d_path = dd['path']

        return d_path

    def test_create_directory(self):
        assert TestRestAPI.create_directory() == 201

    @pytest.mark.parametrize('result', [(200), (400), (401), (403), (404), (406),
                                        (423), (429), (503), (507)])
    def test_create_directory_2(self, result):
        assert TestRestAPI.create_directory() != result

    def test_check_folder(self):
        assert TestRestAPI.check_folder() == 'disk:/test'
