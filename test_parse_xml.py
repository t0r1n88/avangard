from parse_xml import *
import xml
import os
from datetime import datetime
# Это все надо затолкать в фикстуру
PATH_TO_FILE = 'data/test.xml'

tree = ET.parse(PATH_TO_FILE)
root = tree.getroot()
for element in tree.findall("region"):  # or tree.findall('globalVariables/globalVariable/name')
    name = element.find("name")
    if name.text == 'Республика Бурятия':
        chosen_elem = element
        break

def test_get_chosen_element():
    text = 'Республика Бурятия'
    assert isinstance(get_chosen_element(root, text), xml.etree.ElementTree.Element)


def test_get_root():
    assert isinstance(get_root(PATH_TO_FILE), xml.etree.ElementTree.Element)


def test_export_to_excel():
    path = os.getcwd()
    name_file = '/data/' + str(datetime.now())[:10] + '.xlsx'
    assert os.path.isfile(path + name_file)


def test_parsing_chosen_element():
    return_value = parsing_chosen_element(chosen_elem)
    assert type(return_value) == tuple
    assert len(return_value) == 2
    assert (type(return_value[0]) and type(return_value[1])) == list
