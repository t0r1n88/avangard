import os
from datetime import datetime

import tablib
import requests
import openpyxl
import json


# trudvsem
def load_vacancy_trudvsem(region_code='0300000000000'):
    """
    Функция для загрузки записи в json  вакансий и с сайта Trudvsem
    :param region_code: Код региона(по умолчанию республика Бурятия)
    :return: Возращает список словарей, где каждый словарь это вакансия с соответстувующими признаками
    """

    # TODO Переписать функцию так чтобы нужные данные собирались в один json и уже потом с ним работать
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
    name_file = get_name_file('data')
    # lst_vac = create_list_vacancies(data)
    if os.path.isfile(name_file):
        # Если файл существует
        # a+ Открывает файл для добавления и чтения. Указатель стоит в конце файла. Создает файл с именем имя_файла, если такового не существует.
        with open(name_file, 'a+', encoding='utf-8') as outfile:
            # outfile.seek(-1, os.SEEK_END)
            outfile.truncate()
            # Дописываем запятую
            outfile.write(',')
            # Записываем json
            json.dump(data, outfile, ensure_ascii=False)
            # Закрываем список
            outfile.write(']')
    else:
        # Если файла не существует, то создаем его
        with open(name_file, 'w', encoding='utf-8') as outfile:
            array = []
            # Задаем список как верхний элемент файла в котором будут содержаться остальные элементы.
            array.append(data)
            json.dump(array, outfile, ensure_ascii=False)


def export_json_excel(path_to_json_file, path_to_output_file=os.getcwd()):
    """
    Функция для обработки json файла и его экспорта в excel
    :param path_to_json_file: Путь к файлу json с вакансиями
    :param path_to_output_file: Адрес где будет создан файл xlsx(по умолчанию в текущей папке)
    :return:
    """
    with open(path_to_json_file, 'r') as file:
        data = json.loads(file)
        print(type(data))


def get_name_file(path=os.getcwd(), name='/' + str(datetime.now())[:10], type='.json'):
    """
    Функцция для получения имени файла
    :param path: Путь к файлу(по умолчанию путь до текущей директории)
    :param name: Имя файла(по умолчанию текущая дата в формате ГГ-ММ-ДД)
    :param type: Расширение файла(по умолчанию json)
    :return: Строку с именем файла
    """
    path = 'data'
    return path + name + type


if __name__ == '__main__':
    load_vacancy_trudvsem()
    # data = json.load('data/2020-07-27.json')
    # print(data)

    # get_name_file()

    # wb = openpyxl.load_workbook('c:/Users/1/PycharmProjects/avangard/data/trudvsem.xlsx')
    # sheet = wb['1']
    # i = 0
    # raw = 2
    # for i in range(0, 30):
    #     print("http://opendata.trudvsem.ru/api/v1/vacancies/region/0300000000000?offset=" + str(i) + "&limit=100")
    #     response = requests.get("http://opendata.trudvsem.ru/api/v1/vacancies/region/0300000000000?offset=" + str(i) + "&limit=100")
    #     print(response.json())
    #     for element in response.json()['results']['vacancies']:
    #         sheet['A' + str(raw)] = element['vacancy']['job-name']
    #         sheet['B' + str(raw)] = element['vacancy']['source']
    #         sheet['C' + str(raw)] = element['vacancy']['company']['name']
    #         sheet['D' + str(raw)] = element['vacancy']['salary_min']
    #         sheet['E' + str(raw)] = element['vacancy']['salary_max']
    #         sheet['F' + str(raw)] = element['vacancy']['employment']
    #         sheet['G' + str(raw)] = element['vacancy']['schedule']
    #         sheet['H' + str(raw)] = element['vacancy']['category']['specialisation']
    #         sheet['I' + str(raw)] = element['vacancy']['duty']
    #         try:
    #             sheet['J' + str(raw)] = element['vacancy']['requirement']['education']
    #         except KeyError:
    #             print("education")
    #         raw = raw + 1
    #         print(raw)
    #     i = i + 1
    # wb.save('c:/Users/1/PycharmProjects/avangard/data/trudvsem.xlsx')
