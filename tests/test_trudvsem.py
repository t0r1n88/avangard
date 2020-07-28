from trudvsem import *
import pytest

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

@pytest.mark.skip
def test_write_vacancy_to_json_trudvsem():
    assert False

@pytest.mark.skip
def test_get_name_file():
    assert 'data/2020-07-27.json' == get_name_file('data')
