import requests
import openpyxl
import json
#trudvsem

wb = openpyxl.load_workbook('C:/COPP/avangard/data/trudvsem.xlsx')
sheet = wb['1']
i = 0
raw = 2
for i in range(0, 30):
    print("http://opendata.trudvsem.ru/api/v1/vacancies/region/0300000000000?offset=" + str(i) + "&limit=100")
    response = requests.get("http://opendata.trudvsem.ru/api/v1/vacancies/region/0300000000000?offset=" + str(i) + "&limit=100")
    print(response.json())
    for element in response.json()['results']['vacancies']:
        sheet['A' + str(raw)] = element['vacancy']['job-name']
        sheet['B' + str(raw)] = element['vacancy']['source']
        sheet['C' + str(raw)] = element['vacancy']['company']['name']
        sheet['D' + str(raw)] = element['vacancy']['salary_min']
        sheet['E' + str(raw)] = element['vacancy']['salary_max']
        sheet['F' + str(raw)] = element['vacancy']['employment']
        sheet['G' + str(raw)] = element['vacancy']['schedule']
        sheet['H' + str(raw)] = element['vacancy']['category']['specialisation']
        sheet['I' + str(raw)] = element['vacancy']['duty']
        try:
            sheet['J' + str(raw)] = element['vacancy']['requirement']['education']
        except KeyError:
            print("education")
        raw = raw + 1
        print(raw)
    i = i + 1
wb.save('C:/COPP/avangard/data/vacancies.xlsx')
