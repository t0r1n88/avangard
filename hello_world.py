from datetime import datetime
import os
import xlsxwriter
import requests
import json
from trudvsem import *

# path = os.getcwd()
# name_file = str(datetime.now())[:10] + '.xlsx'
# print(path+name_file)

# workbook = xlsxwriter.Workbook('data/tex.xlsx')
# # Устанавливаем название листа
# worksheet = workbook.add_worksheet('Лист 1')
# d = [1,2,3,'Lindy Booth']
# worksheet.write_row(1,0,d)
# workbook.close()
# with open('data/example_json_trudvsem.json','w',encoding='utf-8') as file:
#     response = requests.get("http://opendata.trudvsem.ru/api/v1/vacancies/region/0300000000000?offset=0")
#     json.dump(response.json(),file,ensure_ascii=False,indent=4)

# response = requests.get("https://api.hh.ru/vacancies?area=1118&page=" + str(0) + "&per_page=100")
# print(response.json()['items'])
# # with open('data/example_json_hh.json', 'w', encoding='utf-8') as file:
# #     json.dump(response.json(),file, ensure_ascii=False, indent=4)
#
# response = requests.get("https://api.hh.ru/vacancies?area=1118&page=" + str(0) + "&per_page=100")
# data = response.json()
# arr = []
# # Забираем вакансии
# vacancies = data['items']
# for vacancy in vacancies:
#     # Добавляем вакансии в список
#     arr.append(vacancy)
# print(arr)
d = set()
print(type(d))