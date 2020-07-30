import json
import re
from datetime import datetime
import pandas
import requests
import openpyxl
import xlsxwriter


def get_parameters_hh(region=1118):
    """
    Функция для получения количества вакансий которые есть на сайте и лимита вакансий на каждый запрос
    region: код региона(по умолчанию 1118 Бурятия)
    :return: кортеж из двух параметров: число вакансий и лимит вакансий на каждый запрос
    """
    response = requests.get("https://api.hh.ru/vacancies?area=1118&page=0&per_page=100")
    limit = response.json()['per_page']
    quantity_vacances = response.json()['found']
    # Если  получаем остаток, то количество вакансий очевидно не делится на 100 начисто, а значит нужно добавить
    # еще одну итерацию
    if quantity_vacances % limit:
        quantity_iter = (quantity_vacances // limit) + 1
    else:
        quantity_iter = quantity_vacances // limit

    return quantity_iter, limit


def extract_vac_hh(data):
    """
    Функция для извлечения данных вакансий
    :param data: Список с вакансиями
    :return:
    """
    arr = []
    # Забираем вакансии
    vacancies = data['items']
    for vacancy in vacancies:
        # Добавляем вакансии в список
        arr.append(vacancy)
    return arr


def load_vacancy_hh(region=1118, link='https://api.hh.ru/vacancies'):
    """
    Функция для загрузки вакансий с hh
    :param region: код региона(по умолчанию 1118 Бурятия)
            link = Ссылка на api(по умолчанию https://api.hh.ru/vacancies )
    :return: список с словарями где каждый словарь это вакансия
    """
    quantity_iter, limit = get_parameters_hh()
    # Список где будем хранить все найденные вакансии
    lst_vac = []
    try:
        # Ввиду ограничения hh на количество выдаываемых результатов (не более 2000)
        # Временно придется ограничиться этим. Потом нужно будет продумать как получить больше.
        for i in range(0, 20):
            response = requests.get(f'{link}?area={region}&page={str(i)}&per_page={limit}')
            data = response.json()
            lst_100_vac = extract_vac_hh(data)
            lst_vac.extend(lst_100_vac)
        return lst_vac
    except KeyError:
        print(response.status_code)
        print(response.json())


def write_vacancy_to_json_hh(data, mark='thin'):
    """
    Функция для записи
    :param data:
    :return:
    """
    if mark == 'thin':
        name_file = get_name_file_hh('c:/Users/1/PycharmProjects/avangard/data/')
    else:
        name_file = 'c:/Users/1/PycharmProjects/avangard/data/' + str(datetime.now())[:10] + '_full_hh' + '.json'
    with open(name_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def get_name_file_hh(path, name='/' + str(datetime.now())[:10], type='.json'):
    """
    Функцция для получения имени файла
    :param path: Путь к файлу(по умолчанию путь до текущей директории)
    :param name: Имя файла(по умолчанию текущая дата в формате ГГ-ММ-ДД)
    :param type: Расширение файла(по умолчанию json)
    :return: Строку с именем файла
    """
    return path + name + '_hh' + type


def load_full_data_vacancy_hh(path_to_json_file, link='https://api.hh.ru/vacancies/'):
    """
    Функция для загрузки полных данных вакансии
    :param path_to_json_file: путь до файла  где лежать сокращенные данные
    :return: json файл с полными данными по вакансиям
    """
    with open(path_to_json_file, encoding='utf-8') as file:
        data = json.load(file)
    lst_vac = []
    # Перебираем вакансии, получаем id, по этому id делаем запрос
    for vac in data:
        response = requests.get(f'{link}{vac["id"]}')
        data = response.json()
        lst_vac.append(data)
    return lst_vac


def export_json_to_excel_hh(path_to_json_file):
    """
    Функция для обработки json файла и его экспорта в excel
    :param path_to_json_file: Путь к файлу json с вакансиями
    :return:
    """
    with open(path_to_json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    # Счетчик строк
    count_rows = 0
    # Имя файла
    name_file = 'data/' + str(datetime.now())[:10] + '_hh' + '.xlsx'
    # Создаем объект
    workbook = xlsxwriter.Workbook(name_file)
    # Устанавливаем название листа
    worksheet = workbook.add_worksheet('Лист 1')
    # Указываем стиль для заголовков
    bold = workbook.add_format({'bold': True})
    # Создаем заголовки
    worksheet.write('A1', 'ID вакансии', bold)
    worksheet.write('B1', 'Населенный пункт', bold)
    worksheet.write('C1', 'Название вакансии', bold)
    worksheet.write('D1', 'Минимальная зарплата', bold)
    worksheet.write('E1', 'Максимальная зарплата', bold)
    worksheet.write('F1', 'Оклад указан до вычета налогов', bold)
    worksheet.write('G1', 'Название организации', bold)
    worksheet.write('H1', 'Населенный пункт', bold)
    worksheet.write('I1', 'Улица', bold)
    worksheet.write('J1', 'Дом', bold)
    worksheet.write('K1', 'Полный адрес', bold)
    worksheet.write('L1', 'Требуемый опыт', bold)
    worksheet.write('M1', 'График работы', bold)
    worksheet.write('N1', 'Тип занятости', bold)
    worksheet.write('O1', 'ФИО контактного лица', bold)
    worksheet.write('P1', 'Адрес электронной почты', bold)
    worksheet.write('Q1', 'Телефон работодателя', bold)
    worksheet.write('R1', 'Требуемые навыки', bold)
    worksheet.write('S1', 'Требуемые категории водительских прав', bold)
    worksheet.write('T1', 'Для инвалидов', bold)
    worksheet.write('U1', 'Для детей', bold)
    worksheet.write('V1', 'Дата публикации вакансии', bold)
    worksheet.write('W1', 'Дата создания вакансии', bold)
    worksheet.write('X1', 'Описание вакансии', bold)
    worksheet.write('Y1', 'Архивная вакансия', bold)
    worksheet.write('Z1', 'Долгота ', bold)
    worksheet.write('AA1', 'Широта', bold)

    for vac in data:
        count_rows += 1
        # Собираем строку которую будем записывать
        # Обрабатываем телефоны работодателя
        phones = extract_phones_employment_hh(vac)
        # Обрабатываем специализации
        specializations = extract_specialization_vacance_hh(vac)
        # Обрабатываем список водительских прав
        driver_licence = extract_driver_licence_vacance_hh(vac)
        # Обработка описания вакансии.Удаление html-тегов
        description = purification_text_from_html(vac['description'])
        row = create_row_for_write_to_excel_hh(vac, phones, specializations, driver_licence, description)
        worksheet.write_row(count_rows, 0, list(row))
    workbook.close()


def extract_phones_employment_hh(data):
    """
    Функция для извлечения телефонов работодателя
    :param data: Словарь с данными вакансии
    :return: Строку с номерами телефонов
    """
    arr = []
    tmp = data['contacts']['phones'] if data.get('contacts') else []
    for el in tmp:
        phone = el['country'] + el['city'] + el['number']
        arr.append(phone)
    return ','.join(arr)


def extract_specialization_vacance_hh(data):
    """
    Функция для извлечения навыков необходимых для работы
    :param data: Словарь с данными вакансии
    :return: Строку с перечислением навыков
    """
    tmp_set_s = set()
    for el in data['specializations']:
        tmp_set_s.add(el['name'])
    return ','.join(tmp_set_s)


def extract_driver_licence_vacance_hh(data):
    """
    Функция для извлечения категорий водительских прав
    :param data: Словарь с данными вакансии
    :return: Строка с перечислением требуемых категорий или None
    """
    tmp_set_d = set()
    if data['driver_license_types']:
        for val in data['driver_license_types']:
            tmp_set_d.add(val['id'])
        driver_license = ','.join(tmp_set_d)
        return driver_license
    else:
        return None


def create_row_for_write_to_excel_hh(vac, phones, specializations, driver_licence, description):
    """
    Функция для создания строки , для записи в файл Excel
    :param phones: Строка с телефонами работодателя
    :param specializations: навыки для вакансии
    :param driver_licence: водительские права
    :param description: Описание вакансии
    :return: Кортеж
    """
    # Конвертация булевых значений

    row = vac['id'], vac['area']['name'], vac['name'], vac['salary'].get('from') if vac.get('salary', {}) else None, \
          vac['salary'].get('to') if vac.get('salary', {}) else None, \
          replace_bool(vac['salary'].get('gross')) if vac.get('salary', {}) else None, vac['employer']['name'], \
          vac['address'].get('city') if vac.get('address', {}) else None, \
          vac['address'].get('street') if vac.get('address', {}) else None, \
          vac['address'].get('building') if vac.get('address', {}) else None, \
          vac['address'].get('raw') if vac.get('address', {}) else None, \
          replace_experience(vac['experience']['name']), \
          vac[
              'schedule']['name'], vac['employment']['name'], \
          vac['contacts'].get('name') if vac.get('contacts', {}) else None, \
          vac['contacts'].get('email') if vac.get('contacts', {}) else None, phones, specializations, \
          driver_licence, replace_bool(vac['accept_handicapped']), replace_bool(vac['accept_kids']), vac[
                                                                                                         'published_at'][
                                                                                                     :10], \
          vac['created_at'][:10], description, replace_bool(vac['archived']), vac['address'].get('lat') if vac.get(
        'address',
        {}) else None, \
          vac['address'].get('lng') if vac.get('address', {}) else None
    return row


def replace_experience(text):
    """
    Функция для замены фразы 'Нет опыта' на фразу 'Не требуется'
    :param text:Строка
    :return:Строка
    """
    return 'Не требуется' if text == 'Нет опыта' else text


def replace_bool(text):
    """
    Функция для замены булевых значений на Да,Нет
    :param text:
    :return: Строку Да,если text==true ,если text==false Нет
    """
    if text == True:
        return 'Да'
    elif text == False:
        return 'Нет'
    else:
        return text


def purification_text_from_html(text):
    """
    Функция для очистки текста от html-тегов
    :param text:
    :return:
    """
    return re.sub(r'</?\w*?>|&\w+;|<[^а-яА-ЯёЁ]+>', '', text)


if __name__ == '__main__':
    # data = load_vacancy_hh()
    # write_vacancy_to_json_hh(data)
    # export_json_to_excel_hh('data/2020-07-29_hh.json')
    # data = load_full_data_vacancy_hh('data/2020-07-29_hh.json')
    # write_vacancy_to_json_hh(data, mark='full')
    export_json_to_excel_hh('data/2020-07-29_full_hh.json')
