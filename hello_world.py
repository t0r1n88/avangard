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

c="""
<ul>
<li>Работа с документами.</li>
<li>Решать организационные вопросы.</li>
<li>Работа на компьютере</li>
<li>Подготовка ежемесячной отчетности</li>
<li>Прием звонков</li>
</ul>
"""
print(c)
print(purification_text_from_html(c))