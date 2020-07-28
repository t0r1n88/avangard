from trudvsem import *
import pytest
import os
import json


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


def test_load_vacancy_trudvsem(input_data_serviceabylity_trudvsem):
    """
    GIVEN(Дано) Количество вакансий хранящееся в response.json['meta']['total]
    WHEN(Когда) Когда мы запускаем функцию для скачивания вакансий
    THEN(Тогда) Длина списка который получается после работы функции load_vacancy_trudvsem должна быть равна количеству существующих вакансий
    :param input_data_serviceabylity_trudvsem:
    :return:
    """
    assert input_data_serviceabylity_trudvsem['meta']['total'] == len(load_vacancy_trudvsem())


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


def test_correct_write_json_trudvsem(input_data_serviceabylity_trudvsem):
    """
    GIVEN(Дано) json файл содержащий все нужные вакансии с trudvsem
    WHEN(Когда) мы считываем его в память
    THEN(Тогда) Тип объекта должен быть список, количество элементов в списке должно совпадать
    с input_data_serviceabylity_trudvsem['meta']['total']
    :param input_data_serviceabylity_trudvsem:
    :return:
    """
    path = 'c:/Users/1/PycharmProjects/avangard/data/' + str(datetime.now())[:10] + '.json'
    with open(path, encoding='utf-8') as file:
        data = json.load(file)
    assert type(data) == list
    assert len(data) == input_data_serviceabylity_trudvsem['meta']['total']


def test_purification_text_from_html(text_from_html):
    """
    GIVEN(Дано) Текст содержащий html теги, также возможна пустая строка
    WHEN(Когда) Используем функцию purification_text
    THEN(Тогда) Должны быть корректно удалены  все html-теги
    :param text_from_html:
    :return:
    """
    d = list(map(purification_text_from_html, text_from_html))
    verification_strings = ['', '1234', 'afdswt', 'вапвпвап', '', ' Варрава', 'Иванов', ' Lindy Booth', 'Агранов',
                            'Костицин',
                            'Cassandra Cilian ']
    assert verification_strings == d
