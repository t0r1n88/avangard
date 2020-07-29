import os

from hh import *
import pytest


def test_serviceability_hh(input_data_serviceabylity_hh):
    """
    GIVEN(Дано) Адрес api hh
    WHEN(Когда) Делаем запрос к api
    THEN(Тогда) Должны получать корректный ответ
    :param input_data_serviceabylity_hh: response.json со 100 вакансиями
    :return:
    """
    assert input_data_serviceabylity_hh.status_code == 200

@pytest.mark.skip
def test_load_vacancy_hh(input_data_serviceabylity_hh):
    # assert input_data_serviceabylity_hh.json()['found'] == len(load_vacancy_hh())# Временно придется ограничиться 2000
    assert len(load_vacancy_hh()) == 2000


def test_write_vacancy_to_json_trudvsem(input_data_hh):
    """
    GIVEN(Дано) json файл содержащий все нужные вакансии с trudvsem
    WHEN(Когда) этот файл записывается на жесткий диск
    THEN(Тогда) Должен появиться файл с именем формата ГГ-ММ-ДД.json
    :param input_data_trudvsem:
    :return:
    """
    write_vacancy_to_json_hh(input_data_hh)
    path = 'c:/Users/1/PycharmProjects/avangard/data/' + str(datetime.now())[:10] + '_hh' + '.json'
    assert os.path.isfile(path)

def test_correct_write_json_trudvsem(input_data_serviceabylity_hh):
    """
    GIVEN(Дано) json файл содержащий все нужные вакансии с hh
    WHEN(Когда) мы считываем его в память
    THEN(Тогда) Тип объекта должен быть список, количество элементов в списке должно совпадать c 2000

    :param input_data_serviceabylity_trudvsem:
    :return:
    """
    path = 'c:/Users/1/PycharmProjects/avangard/data/' + str(datetime.now())[:10]+'_hh' + '.json'
    with open(path, encoding='utf-8') as file:
        data = json.load(file)
    assert type(data) == list
    assert len(data) == 2000