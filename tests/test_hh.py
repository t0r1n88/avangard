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

def test_load_vacancy_hh(input_data_serviceabylity_hh):
    assert input_data_serviceabylity_hh.json()['found'] == len(load_vacancy_hh())

