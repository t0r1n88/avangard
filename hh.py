import requests
import openpyxl

wb = openpyxl.load_workbook('C:/COPP/avangard/data/hh.xlsx')
sheet = wb['1']
raw = 2
for i in range(0, 18):
    print("https://api.hh.ru/vacancies?area=20&page=" + str(i) + "&per_page=100")
    response = requests.get("https://api.hh.ru/vacancies?area=20&page=" + str(i) + "&per_page=100")
    print(response.json())
    for element in response.json()['items']:
        sheet['A' + str(1)] = 'Вакансия'
        sheet['A' + str(raw)] = element['name']
        sheet['B' + str(1)] = 'Компания'
        sheet['B' + str(raw)] = element['employer']['name']
        sheet['C' + str(1)] = 'Обязанности'
        sheet['C' + str(raw)] = element['snippet']['responsibility']
        # sheet['D' + str(raw)] = element['vacancy']['salary_max']
        # sheet['E' + str(raw)] = element['vacancy']['employment']
        # sheet['F' + str(raw)] = element['vacancy']['schedule']
        # sheet['G' + str(raw)] = element['vacancy']['category']['specialisation']
        # sheet['H' + str(raw)] = element['vacancy']['duty']
        # try:
        #     sheet['I' + str(raw)] = element['vacancy']['requirement']['education']
        # except KeyError:
        #    print("education")
        raw = raw + 1
        print(raw)
i = + 1

for i in range(0, 9):
    print("https://api.hh.ru/vacancies?area=1119&area=4640&area=4641&area=5058&area=4642&area=5073&area=5063&area=1120&area=5060&area=4643&area=1121&area=4644&area=5076&area=5062&area=5059&area=4645&area=4646&area=4647&area=4660&area=5074&area=5080&area=5065&area=4648&area=4649&area=1122&area=4650&area=5082&area=4651&area=5079&area=5069&area=5061&area=4652&area=5077&area=5083&area=4653&area=4654&area=5067&area=5072&area=1123&area=4661&area=4655&area=5078&area=4656&area=2648&area=5075&area=5064&area=5071&area=4657&area=4658&area=5068&area=4659&area=5070&area=5081&area=5066&area=4662&page=" + str(i) + "&per_page=100")
    response = requests.get("https://api.hh.ru/vacancies?area=1119&area=4640&area=4641&area=5058&area=4642&area=5073&area=5063&area=1120&area=5060&area=4643&area=1121&area=4644&area=5076&area=5062&area=5059&area=4645&area=4646&area=4647&area=4660&area=5074&area=5080&area=5065&area=4648&area=4649&area=1122&area=4650&area=5082&area=4651&area=5079&area=5069&area=5061&area=4652&area=5077&area=5083&area=4653&area=4654&area=5067&area=5072&area=1123&area=4661&area=4655&area=5078&area=4656&area=2648&area=5075&area=5064&area=5071&area=4657&area=4658&area=5068&area=4659&area=5070&area=5081&area=5066&area=4662&page=" + str(i) + "&per_page=100")
    print(response.json())
    for element in response.json()['items']:
        sheet['A' + str(raw)] = element['name']
        sheet['B' + str(raw)] = element['employer']['name']
        sheet['C' + str(raw)] = element['snippet']['responsibility']
        # sheet['D' + str(raw)] = element['vacancy']['salary_max']
        # sheet['E' + str(raw)] = element['vacancy']['employment']
        # sheet['F' + str(raw)] = element['vacancy']['schedule']
        # sheet['G' + str(raw)] = element['vacancy']['category']['specialisation']
        # sheet['H' + str(raw)] = element['vacancy']['duty']
        # try:
        #     sheet['I' + str(raw)] = element['vacancy']['requirement']['education']
        # except KeyError:
        #    print("education")
        raw = raw + 1
        print(raw)
i = + 1

wb.save('C:/COPP/avangard/data/hh.xlsx')