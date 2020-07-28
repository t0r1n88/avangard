import os
from datetime import datetime
import requests
import json
import xlsxwriter


def load_vacancy_trudvsem(region_code='0300000000000'):
    """
    Функция для загрузки записи в json  вакансий и с сайта Trudvsem
    :param region_code: Код региона(по умолчанию республика Бурятия)
    :return: Возращает список словарей, где каждый словарь это вакансия с соответстувующими признаками
    """

    link = "http://opendata.trudvsem.ru/api/v1/vacancies/region/"
    # Делаем одиночный запрос чтобы узнать количество вакансий в регионе и лимит выдачи вакансий на один запрос
    response = requests.get(f'{link}{region_code}?offset={str(0)}')
    # Создаем 2 переменные куда сохраняем количество вакансий и лимит
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
    #
    for i in range(0, quantity_iter):
        response = requests.get(f'{link}{region_code}?offset={str(i)}&limit=100')
        data = response.json()
        lst_100_vac = extract_vac(data)
        lst_vac.extend(lst_100_vac)
    return lst_vac


def extract_vac(data):
    """
    Функция для извлечения вакансий из файла
    :param data:словарь json
    :return:список словарей, где каждый словарь это вакансия.Ключом будет являться id вакансии
    """
    # Промежуточный список куда будем добавлять вакансии(100 за раз)
    arr = []
    # Забираем вакансии
    vacancies = data['results']['vacancies']
    for vacancy in vacancies:
        # Создаем временный словарь
        temp_dict = {}
        temp_dict[vacancy['vacancy']['id']] = vacancy['vacancy']
        arr.append(temp_dict)
    return arr


def write_vacancy_to_json_trudvsem(data):
    """
    Функция для дозаписи json файла, чтобы сформировать один большой файл дабы впоследствии спокойно с ним работать
    :param data: словарь
    :return: созданный файл json
    """
    name_file = get_name_file('c:/Users/1/PycharmProjects/avangard/data/')
    with open(name_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False,indent=4)


def export_json_excel(path_to_json_file):
    """
    Функция для обработки json файла и его экспорта в excel
    :param path_to_json_file: Путь к файлу json с вакансиями
    :param path_to_output_file: Адрес где будет создан файл xlsx(по умолчанию в текущей папке)
    :return:
    """
    with open(path_to_json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    # Счетчик строк
    count_rows = 0
    # Имя файла
    name_file = 'data/' + str(datetime.now())[:10] + '.xlsx'
    # Создаем объект
    workbook = xlsxwriter.Workbook(name_file)
    # Устанавливаем название листа
    worksheet = workbook.add_worksheet('Лист 1')
    # Указываем стиль для заголовков
    bold = workbook.add_format({'bold': True})
    # Создаем заголовки
    worksheet.write('A1', 'Источник вакансии', bold)
    worksheet.write('B1', 'Регион', bold)
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
    for dic in data:
        count_rows += 1
        # TODO  Сделать более изящное решение через map
        # Превращаем dict.values в список, чтобы было легче работать с ключами
        d = (list(dic.values()))[0]
        # Собираем строку которую будем записывать
        # Извлекаем адреса
        address = list(d['addresses'].values())[0][0]
        row = d['source'], d['region']['name'], d['company'].get('name'), d['company'].get('ogrn'), d[
            'company'].get('inn'), d['company'].get('kpp'), d['company'].get('phone'), d['company'].get('fax'), d[
                  'company'].get('email'), d['creation-date'], d.get('modify-date'), d['salary'], d.get(
            'salary_min'), d.get('salary_max'), d.get('job-name'), d['vac_url'], d['employment'], d['schedule'], d[
                  'category']['specialisation'], d['requirement'].get('education'), d.get(
            'qualification'), d['requirement'].get('experience'), address.get('location'), d.get(
            'social_protected'), d['term']['text'] if d.get('term') else None, d.get('currency'), d.get('duty'), \
              address.get('lng'), address.get('lat')
        worksheet.write_row(count_rows, 0, list(row))
    workbook.close()


# Зададим ширину колонок
# worksheet.set_column('A:A',60)
# worksheet.set_column('B:B',40)
# # Записываем данные из списков в колонки
# worksheet.write_column(1, 0, cat_lst)
# worksheet.write_column(1, 1, value_lst)


def get_name_file(path, name='/' + str(datetime.now())[:10], type='.json'):
    """
    Функцция для получения имени файла
    :param path: Путь к файлу(по умолчанию путь до текущей директории)
    :param name: Имя файла(по умолчанию текущая дата в формате ГГ-ММ-ДД)
    :param type: Расширение файла(по умолчанию json)
    :return: Строку с именем файла
    """
    print(path + name + type)
    return path + name + type


if __name__ == '__main__':
    data = load_vacancy_trudvsem()
    write_vacancy_to_json_trudvsem(data)
    # export_json_excel('data/2020-07-27.json')
