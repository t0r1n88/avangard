import xml.etree.ElementTree as ET
import os
from datetime import datetime
import xlsxwriter

PATH_TO_FILE = 'data/test.xml'
TEXT = 'Республика Бурятия'


def get_chosen_element(root, text: str):
    """
    Функция для получения конкретного элемента в дереве. Конкректно в этом модуле используется для получения
    данных только по Бурятии.
    :param
    text: Значение элемента по которому его можно определить
    root: Объект дерева
    :return: Поддерево содержащее вложеные в найденный элемент элменты
    """
    # Итерируемся по элементам под названием  region
    for element in root.findall("region"):
        # Получем элемент name
        name = element.find("name")
        # Если текст равен заданному возвращаем найденый элемент
        if name.text == 'Республика Бурятия':
            return element


def get_root(path_to_file: str) -> object:
    # Создаем дерево при помощи parse
    tree = ET.parse(path_to_file)
    # Получаем корень и возвращаем его
    root = tree.getroot()
    return root


def parsing_chosen_element(chosen_element):
    """
    Функция извлекающая данные из выбранного элемента xml
    :param chosen_element: выбранный элемент
    :return:Кортеж из  2 списков :cat_lst -список содержащий наименования категорий и value_lst-список содержащий значения этих категорий
    """
    # Создаем 2 списка
    cat_lst = []
    value_lst = []
    # Перебираем элементы по указанному пути
    for elem in chosen_element.findall('statistics/statistic'):
        # Находим аттрибут name
        name = elem.find("name")
        # Добавляем значение этого аттрибута
        cat_lst.append(name.text)
        # Аналогично
        value = elem.find('value')
        value_lst.append(value.text)
    return cat_lst, value_lst


def export_to_excel(cat_lst,value_lst, path_to_dir=os.getcwd()):
    """
    Функция предназначенная для экспорта значений полученных из xml в файл с разрешением xlsx
    :param cat_lst: список содержащий в себе категории
    :param value_lst: список содержащий значения которые принимают эти категории
    :param path_to_dir: путь к к создаваемому файлу.По умолчанию создается в той же директории что и скрипт
    :return: Создает файл с разрешением xlsx с названием 2020-07-24(текущая дата)
    """
    name_file = '/data/' + str(datetime.now())[:10] + '.xlsx'
    # Открываем новый файл на запись
    workbook = xlsxwriter.Workbook(path_to_dir + name_file)
    # Создаем лист
    worksheet = workbook.add_worksheet('Лист 1')
    bold = workbook.add_format({'bold':True})

    # Создаем заголовок
    worksheet.write('A1', 'Категория компании',bold)
    worksheet.write('B1', 'Количество компаний в данной категории',bold)
    # Зададим ширину колонок
    worksheet.set_column('A:A',60)
    worksheet.set_column('B:B',40)
    # Записываем данные из списков в колонки
    worksheet.write_column(1, 0, cat_lst)
    worksheet.write_column(1, 1, value_lst)
    # # Создадим график
    # chart = workbook.add_chart({'type':'column'})
    # # Добавляем значения на базе которых будем строить график
    # chart.add_series({'values':'Лист 1!$B$3:$B$6'})
    # # Вставляем график в нужную ячейку
    # worksheet.insert_chart('C3',chart)
    # Закрываем файл
    workbook.close()


if __name__ == "__main__":
    # Получаем корень дерева
    root = get_root(PATH_TO_FILE)
    # Получаем элемент с нужным именем
    chosen_element = get_chosen_element(root,TEXT)
    # Получаем данные из нужного элемента
    cat_lst,val_lst = parsing_chosen_element(chosen_element)
    # Экспортиртируем данные в excel
    export_to_excel(cat_lst,val_lst)



    #
    # # Получаем корень дерева
    # # root = get_root(PATH_TO_FILE)
    # # Получаем корень с нужным названием.
    # # chosen_root = get_chosen_element(root,TEXT)
    # tree = ET.parse(PATH_TO_FILE)
    # root = tree.getroot()
    # chosen_elem = None
    # for element in tree.findall("region"):  # or tree.findall('globalVariables/globalVariable/name')
    #     name = element.find("name")
    #     # print(element.tag, name.text, element.attrib)
    #     if name.text == 'Республика Бурятия':
    #         chosen_elem = element
    #         break
    # cat_lst = []
    # value_lst = []
    # for elem in chosen_elem.findall('statistics/statistic'):
    #     name = elem.find("name")
    #     cat_lst.append(name.text)
    #     value = elem.find('value')
    #     value_lst.append(value.text)
    #     print(name.text, value.text)
    # print(cat_lst, value_lst)
    # path = os.getcwd()
    # name_file = '/' + str(datetime.now())[:10] + '.xlsx'
    # # Открываем новый файл на запись
    # workbook = xlsxwriter.Workbook(path + name_file)
    # # Создаем лист
    # worksheet = workbook.add_worksheet('Лист 1')
    #
    # worksheet.write('A1', 'Категория компании')
    # worksheet.write('B1', 'Количество компаний в данной категории')
    # worksheet.write_column(1, 0, cat_lst)
    # worksheet.write_column(1, 1, value_lst)
    # workbook.close()
