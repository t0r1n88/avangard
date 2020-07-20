import requests
import openpyxl
import json

wb = openpyxl.load_workbook('C:/COPP/avangard/data/vacancies.xlsx')
sheet = wb['test']
i = 0
raw = 1
for i in range(0, 30):
    print("http://opendata.trudvsem.ru/api/v1/vacancies/region/0300000000000?offset=" + str(i) + "&limit=100")
    response = requests.get("http://opendata.trudvsem.ru/api/v1/vacancies/region/0300000000000?offset=" + str(i) + "&limit=100")
    print(response.json())
    for element in response.json()['results']['vacancies']:
        sheet['A' + str(raw)] = element['vacancy']['job-name']
        raw = raw + 1
        print(raw)
    i = i + 1
wb.save('C:/COPP/avangard/data/vacancies.xlsx')