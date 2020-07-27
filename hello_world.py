from datetime import datetime
import os
import xlsxwriter




# path = os.getcwd()
# name_file = str(datetime.now())[:10] + '.xlsx'
# print(path+name_file)

workbook = xlsxwriter.Workbook('data/tex.xlsx')
# Устанавливаем название листа
worksheet = workbook.add_worksheet('Лист 1')
d = [1,2,3,'Lindy Booth']
worksheet.write_row(1,0,d)
workbook.close()