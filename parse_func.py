import os
import xml.etree.ElementTree as ET

def load_dataset():
# TODO Реализовать автоматическую загрузку датасетов выложеных на сайте trudvsem
# TODO Реализовать обозначение датасета дотой в формате 21-07-2020
# TODO Реализовать обработку исключений и ошибок при  загрузке
    pass


def parse_xml(data):
# TODO Реализовать парсинг полученных xml файлов
    pass
    tree = ET.parse('8.xml')
    root = tree.getroot()


def export_to_excel(data):
# TODO Реализовать экспорт в файл формата xlsx удобный для анализа.
    pass