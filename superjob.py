import requests
import openpyxl

wb = openpyxl.load_workbook('C:/COPP/avangard/data/superjob.xlsx')
sheet = wb['1']
i = 0
raw = 2
for i in range(0, 6):

    response = requests.get('https://api.superjob.ru/2.33/vacancies?o=81&page='+str(i)+'&count=100',
                            headers={'X-Api-App-Id': 'v3.r.132669037.4786a72c63a7c44d37ed04485940a075becd9a0b.1f53a3156cfc2de6ecb01577b65be80447f9d0ac'},
                            )

    print(response.json())
    for element in response.json()['objects']:
        sheet['A' + str(raw)] = element['profession']
        # sheet['B' + str(raw)] = element['vacancy']['source']
        # sheet['C' + str(raw)] = element['vacancy']['company']['name']
        # sheet['D' + str(raw)] = element['vacancy']['salary_min']
        # sheet['E' + str(raw)] = element['vacancy']['salary_max']
        # sheet['F' + str(raw)] = element['vacancy']['employment']
        # sheet['G' + str(raw)] = element['vacancy']['schedule']
        # sheet['H' + str(raw)] = element['vacancy']['category']['specialisation']
        # sheet['I' + str(raw)] = element['vacancy']['duty']
        # try:
        #   sheet['J' + str(raw)] = element['vacancy']['requirement']['education']
        # except KeyError:
        #   print("education")
        raw = raw + 1
        print(raw)
    i = i + 1
wb.save('C:/COPP/avangard/data/superjob.xlsx')
