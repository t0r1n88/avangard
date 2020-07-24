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
    :return:excel file
    """

    # TODO Переписать функцию так чтобы нужные данные собирались в один json и уже потом с ним работать
    link = "http://opendata.trudvsem.ru/api/v1/vacancies/region/"
    # Делаем одиночный запрос чтобы узнать количество вакансий в регионе и лимит выдачи вакансий на один запрос
    response = requests.get(f'{link}{region_code}?offset={str(0)}')
    # Создаем 2 переменные куда сохраняем количество вакансий и лимит
    quantity_vacances = response.json()['meta']['total']
    limit = response.json()['meta']['limit']
    # Имя файла
    name_file = str(datetime.now())[:10]
    # Если  получаем остаток, то количество вакансий очевидно не делится на 100 начисто, а значит нужно добавить
    # еще одну итерацию
    if quantity_vacances % limit:
        quantity_iter = (quantity_vacances // limit) + 1
    else:
        quantity_iter = quantity_vacances // limit
    #
    for i in range(0, 2):
        response = requests.get(f'{link}{region_code}?offset={str(i)}&limit=100')
        data = response.json()
        with open(f'data/{name_file}.json', 'a', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)


def export_json_excel(path_to_json_file, path_to_output_file=os.getcwd()):
    """
    Функция для обработки json файла и его экспорта в excel
    :param path_to_json_file: Путь к файлу json с вакансиями
    :param path_to_output_file: Адрес где будет создан файл xlsx(по умолчанию в текущей папке)
    :return:
    """



if __name__ == '__main__':
    load_vacancy_trudvsem()
    # export_json_excel()

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
