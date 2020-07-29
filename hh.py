import requests
import openpyxl


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
        for i in range(0, quantity_iter):
            response = requests.get(f'{link}?area={region}&page={str(i)}&per_page={limit}')
            data = response.json()
            print(data.keys())
            arr = []
            # Забираем вакансии
            vacancies = data['items']
            for vacancy in vacancies:
                # Добавляем вакансии в список
                arr.append(vacancy)
            lst_vac.extend(arr)
        return lst_vac
    except KeyError:
        # print(response.json()['errors'][0]['value'],response.json()['errors'][1]['type'])
        print(response.status_code)
        print(response.json())


# if __name__ == '__main__':
#     data = load_vacancy_hh()
    # print(len(data))
# wb = openpyxl.load_workbook('C:/1/hh.xlsx')
# sheet = wb['1']
# raw = 2
# for i in range(0, 18):
#     print("https://api.hh.ru/vacancies?area=20&page=" + str(i) + "&per_page=100")
#     response = requests.get("https://api.hh.ru/vacancies?area=20&page=" + str(i) + "&per_page=100")
#     print(response.json())
#     for element in response.json()['items']:
#         sheet['A' + str(1)] = 'Вакансия'
#         sheet['A' + str(raw)] = element['name']
#         sheet['B' + str(1)] = 'Компания'
#         sheet['B' + str(raw)] = element['employer']['name']
#         sheet['C' + str(1)] = 'Обязанности'
#         sheet['C' + str(raw)] = element['snippet']['responsibility']
#         # sheet['D' + str(raw)] = element['vacancy']['salary_max']
#         # sheet['E' + str(raw)] = element['vacancy']['employment']
#         # sheet['F' + str(raw)] = element['vacancy']['schedule']
#         # sheet['G' + str(raw)] = element['vacancy']['category']['specialisation']
#         # sheet['H' + str(raw)] = element['vacancy']['duty']
#         # try:
#         #     sheet['I' + str(raw)] = element['vacancy']['requirement']['education']
#         # except KeyError:
#         #    print("education")
#         raw = raw + 1
#         print(raw)
# i = + 1
#
# for i in range(0, 9):
#     print("https://api.hh.ru/vacancies?area=1119&area=4640&area=4641&area=5058&area=4642&area=5073&area=5063&area=1120&area=5060&area=4643&area=1121&area=4644&area=5076&area=5062&area=5059&area=4645&area=4646&area=4647&area=4660&area=5074&area=5080&area=5065&area=4648&area=4649&area=1122&area=4650&area=5082&area=4651&area=5079&area=5069&area=5061&area=4652&area=5077&area=5083&area=4653&area=4654&area=5067&area=5072&area=1123&area=4661&area=4655&area=5078&area=4656&area=2648&area=5075&area=5064&area=5071&area=4657&area=4658&area=5068&area=4659&area=5070&area=5081&area=5066&area=4662&page=" + str(i) + "&per_page=100")
#     response = requests.get("https://api.hh.ru/vacancies?area=1119&area=4640&area=4641&area=5058&area=4642&area=5073&area=5063&area=1120&area=5060&area=4643&area=1121&area=4644&area=5076&area=5062&area=5059&area=4645&area=4646&area=4647&area=4660&area=5074&area=5080&area=5065&area=4648&area=4649&area=1122&area=4650&area=5082&area=4651&area=5079&area=5069&area=5061&area=4652&area=5077&area=5083&area=4653&area=4654&area=5067&area=5072&area=1123&area=4661&area=4655&area=5078&area=4656&area=2648&area=5075&area=5064&area=5071&area=4657&area=4658&area=5068&area=4659&area=5070&area=5081&area=5066&area=4662&page=" + str(i) + "&per_page=100")
#     print(response.json())
#     for element in response.json()['items']:
#         sheet['A' + str(raw)] = element['name']
#         sheet['B' + str(raw)] = element['employer']['name']
#         sheet['C' + str(raw)] = element['snippet']['responsibility']
#         # sheet['D' + str(raw)] = element['vacancy']['salary_max']
#         # sheet['E' + str(raw)] = element['vacancy']['employment']
#         # sheet['F' + str(raw)] = element['vacancy']['schedule']
#         # sheet['G' + str(raw)] = element['vacancy']['category']['specialisation']
#         # sheet['H' + str(raw)] = element['vacancy']['duty']
#         # try:
#         #     sheet['I' + str(raw)] = element['vacancy']['requirement']['education']
#         # except KeyError:
#         #    print("education")
#         raw = raw + 1
#         print(raw)
# i = + 1
#
# wb.save('C:/1/hh.xlsx')
