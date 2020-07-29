import json
from datetime import datetime

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

def write_vacancy_to_json_hh(data,mark='thin'):
    """
    Функция для записи
    :param data:
    :return:
    """
    if mark == 'thin':
        name_file = get_name_file_hh('c:/Users/1/PycharmProjects/avangard/data/')
    else:
        name_file ='c:/Users/1/PycharmProjects/avangard/data/' +str(datetime.now())[:10]+'_full_hh' + '.json'
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
    return path + name +'_hh'+ type


def load_full_data_vacancy_hh(path_to_json_file, link='https://api.hh.ru/vacancies/'):
    """
    Функция для загрузки полных данных вакансии
    :param path_to_json_file: путь до файла  где лежать сокращенные данные
    :return: json файл с полными данными по вакансиям
    """
    with open(path_to_json_file,encoding='utf-8') as file:
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
    with open(path_to_json_file,'r',encoding='utf-8') as file:
        data = json.load(file)
    # Счетчик строк
    count_rows = 0
    # Имя файла
    name_file = 'data/' + str(datetime.now())[:10]+'_hh' + '.xlsx'
    # Создаем объект
    workbook = xlsxwriter.Workbook(name_file)
    # Устанавливаем название листа
    worksheet = workbook.add_worksheet('Лист 1')
    # Указываем стиль для заголовков
    bold = workbook.add_format({'bold': True})
    # Создаем заголовки
    worksheet.write('A1', 'ID вакансии', bold)
    worksheet.write('B1', 'Населенный пункт', bold)
    worksheet.write('C1', 'Название организации', bold)
    worksheet.write('D1', 'ОГРН', bold)
    worksheet.write('E1', 'ИНН', bold)
    worksheet.write('F1', 'КПП', bold)
    worksheet.write('G1', 'Телефон организации', bold)
    worksheet.write('H1', 'Факс организации', bold)
    worksheet.write('I1', 'E-mail', bold)
    worksheet.write('J1', 'Дата размещения вакансии', bold)
    worksheet.write('K1', 'Дата изменения вакансии', bold)
    worksheet.write('L1', 'Вилка зарплаты', bold)
    worksheet.write('M1', 'Минимальная зарплата', bold)
    worksheet.write('N1', 'Максимальная зарплата', bold)
    worksheet.write('O1', 'Название вакансии', bold)
    worksheet.write('P1', 'Ссылка на вакансию', bold)
    worksheet.write('Q1', 'Тип занятости', bold)
    worksheet.write('R1', 'Рабочий график', bold)
    worksheet.write('S1', 'Отрасль', bold)
    worksheet.write('T1', 'Образование', bold)
    worksheet.write('U1', 'Квалификация', bold)
    worksheet.write('V1', 'Опыт работы', bold)
    worksheet.write('W1', 'Адрес организации', bold)
    worksheet.write('X1', 'Социальная защит', bold)
    worksheet.write('Y1', 'Примечания', bold)
    worksheet.write('Z1', 'Валюта зарплаты', bold)
    worksheet.write('AA1', 'Описание вакансии', bold)
    worksheet.write('AB1', 'Долгота', bold)
    worksheet.write('AC1', 'Широта', bold)

    for vac in data:
        count_rows += 1
        # TODO  Сделать более изящное решение через map
        # Собираем строку которую будем записывать
        # Извлекаем адреса
        row =vac['id'], vac['area']['name'], d['company'].get('name'), d['company'].get('ogrn'), d[
            'company'].get('inn'), d['company'].get('kpp'), d['company'].get('phone'), d['company'].get('fax'), d[
                  'company'].get('email'), d['creation-date'], d.get('modify-date'), d['salary'], d.get(
            'salary_min'), d.get('salary_max'), d.get('job-name'), d['vac_url'], d['employment'], d['schedule'], d[
                  'category']['specialisation'], d['requirement'].get('education'), d.get(
            'qualification'), d['requirement'].get('experience'), address.get('location'), d.get(
            'social_protected'), d['term']['text'] if d.get('term') else None, d.get('currency'),text, \
              address.get('lng'), address.get('lat')
        worksheet.write_row(count_rows, 0, list(row))
    workbook.close()


if __name__ == '__main__':
    # data = load_vacancy_hh()
    # write_vacancy_to_json_hh(data)
    # export_json_to_excel_hh('data/2020-07-29_hh.json')
    data = load_full_data_vacancy_hh('data/2020-07-29_hh.json')
    write_vacancy_to_json_hh(data,mark='full')


