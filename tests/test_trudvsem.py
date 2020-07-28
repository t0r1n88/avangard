from trudvsem import *
import pytest
import os


def test_serviceability_trudvsem(input_data_serviceabylity_trudvsem):
    """
    GIVEN(Дано) Адрес api trudvsem
    WHEN(Когда) Делаем запрос к api
    THEN(Тогда) Должны получать корректный ответ
    :param input_data_serviceabylity_trudvsem: response.json со 100 вакансиями
    :return:
    """

    assert input_data_serviceabylity_trudvsem['status'] == '200'
    assert input_data_serviceabylity_trudvsem['request']['api'] == 'v1'


def test_type_output_extract_vac_trudvsem(input_data_serviceabylity_trudvsem):
    """
    GIVEN(Дано) response.json
    WHEN(КОГДА) он передается на обработку функции extract_vac для создания списка вакансий
    THEN(ТОГДА) Результат должен быть списком
    :param input_data_serviceabylity_trudvsem:
    :return:
    """
    assert type(extract_vac(input_data_serviceabylity_trudvsem)) == list


def test_extract_vac_trudvsem(input_data_serviceabylity_trudvsem):
    """
    GIVEN(Дано) response.json
    WHEN(КОГДА) он передается на обработку функции extract_vac для создания списка вакансий
    THEN(ТОГДА) Результат должен быть списком словарей, где ключ это id а значение это словарь который содержит все данные
    по вакансии
    :param input_data_serviceabylity_trudvsem:
    :return:
    """
    vacancies = input_data_serviceabylity_trudvsem['results']['vacancies']
    d = extract_vac(input_data_serviceabylity_trudvsem)
    for i in range(100):
        assert vacancies[i]['vacancy']['id'] == list(d[i].keys())[0]


@pytest.mark.skip(reason='Пока не нужно')
def test_load_vacancy_trudvsem(input_data_serviceabylity_trudvsem):
    """
    GIVEN(Дано) Количество вакансий хранящееся в response.json['meta']['total]
    WHEN(Когда) Когда мы запускаем функцию для скачивания вакансий
    THEN(Тогда) Длина списка который получается после работы функции load_vacancy_trudvsem должна быть равна количеству существующих вакансий
    :param input_data_serviceabylity_trudvsem:
    :return:
    """
    assert input_data_serviceabylity_trudvsem['meta']['total'] == len(load_vacancy_trudvsem())


@pytest.mark.skip
def test_export_json_excel():
    assert False


def test_write_vacancy_to_json_trudvsem(input_data_trudvsem):
    """
    GIVEN(Дано) json файл содержащий все нужные вакансии с trudvsem
    WHEN(Когда) этот файл записывается на жесткий диск
    THEN(Тогда) Должен появиться файл с именем формата ГГ-ММ-ДД.json
    :param input_data_trudvsem:
    :return:
    """
    write_vacancy_to_json_trudvsem(input_data_trudvsem)
    path = 'c:/Users/1/PycharmProjects/avangard/data/' + str(datetime.now())[:10] + '.json'
    assert os.path.isfile(path)


@pytest.mark.skip
def test_get_name_file():
    assert 'data/2020-07-28.json' == get_name_file('data')
