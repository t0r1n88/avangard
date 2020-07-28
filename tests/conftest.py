import pytest
import requests
import json
# Файл в котором будут хранится фикстуры для тестов

# Константы
REGION_CODE_TRUDVSEM ="0300000000000"
REGION_CODE_HH = ''
LINK_VACANCY_TRUDVSEM = "http://opendata.trudvsem.ru/api/v1/vacancies/region/"
LINK_VACANCY_HH = ''


@pytest.fixture()
def input_data_serviceabylity_trudvsem():
    """
    Фикстура для проверки доступности и версии api  trudvsem
    :return:
    """

    response = requests.get(LINK_VACANCY_TRUDVSEM + REGION_CODE_TRUDVSEM + '?offset=0')
    return response.json()

@pytest.fixture()
def input_data_trudvsem():
    """
    Фикстура для загрузки всех данных по вакансиям в Республике Бурятия
    :return: Список со всеми вакансиями: в виде словарей.
    """
    response = requests.get(LINK_VACANCY_TRUDVSEM + REGION_CODE_TRUDVSEM + '?offset=0')
    quantity_vacances = response.json()['meta']['total']
    limit = response.json()['meta']['limit']
    # Список с вакансиями
    lst_vac = []
    # Имя файла
    # Если  получаем остаток, то количество вакансий очевидно не делится на 100 начисто, а значит нужно добавить
    # еще одну итерацию
    if quantity_vacances % limit:
        quantity_iter = (quantity_vacances // limit) + 1
    else:
        quantity_iter = quantity_vacances // limit

    for i in range(0, quantity_iter):
        response = requests.get(f'{LINK_VACANCY_TRUDVSEM}{REGION_CODE_TRUDVSEM}?offset={str(i)}&limit=100')
        data = response.json()
        arr = []
        # Забираем вакансии
        vacancies = data['results']['vacancies']
        for vacancy in vacancies:
            # Создаем временный словарь
            temp_dict = {}
            temp_dict[vacancy['vacancy']['id']] = vacancy['vacancy']
            arr.append(temp_dict)
        lst_vac.extend(arr)
    return lst_vac