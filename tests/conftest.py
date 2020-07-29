import pytest
import requests
import json
# Файл в котором будут хранится фикстуры для тестов

# Константы
REGION_CODE_TRUDVSEM ="0300000000000"
REGION_CODE_HH = '1118'
LINK_VACANCY_TRUDVSEM = "http://opendata.trudvsem.ru/api/v1/vacancies/region/"
LINK_VACANCY_HH = 'https://api.hh.ru/vacancies'


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

@pytest.fixture()
def text_from_html():
    """
    Фикстура для создания списка строк для проверки очистки текста от html тегов
    :return: Список строковых значений
    """
    testing_strings = ['','1234','afdswt','вапвпвап','<a>',' Варрава','<ol>Иванов','<p> Lindy Booth</p>','Агранов</p>','Костицин<br><ol></l>',
                       '<p>Cassandra Cilian </head>']
    return testing_strings

@pytest.fixture()
def input_data_serviceabylity_hh():
    """
    Фикстура для проверки работоспособности api HH
    :return: Возвращает json файл
    """
    response = requests.get(LINK_VACANCY_HH+'?area='+REGION_CODE_HH+'&page=0&per_page=100')
    return response

@pytest.fixture()
def input_data_hh():
    """
    Фикстура для загрузки данных по вакансиям с hh
    :return: Список вакансий
    """
    response = requests.get(LINK_VACANCY_HH+'?area='+REGION_CODE_HH+'&page=0&per_page=100')
    limit = response.json()['per_page']
    quantity_vacances = response.json()['found']
    lst_vac = []
    # Имя файла
    # Если  получаем остаток, то количество вакансий очевидно не делится на 100 начисто, а значит нужно добавить
    # еще одну итерацию
    if quantity_vacances % limit:
        quantity_iter = (quantity_vacances // limit) + 1
    else:
        quantity_iter = quantity_vacances // limit

    for i in range(0, quantity_iter):
        response = requests.get(f'{LINK_VACANCY_HH}?area={REGION_CODE_HH}&page={str(i)}&per_page={limit}')
        data = response.json()
        arr = []
        # Забираем вакансии
        vacancies = data['items']
        for vacancy in vacancies:
            # Добавляем вакансии в список
            arr.append(vacancy)
        lst_vac.extend(arr)
    return lst_vac
