from parse_xml import *
import xml

tree = ET.parse(PATH_TO_FILE)
root = tree.getroot()

PATH_TO_FILE = 'data/test.xml'


def test_get_chosen_element():
    text = 'Республика Бурятия'
    assert isinstance(get_chosen_element(root, text), xml.etree.ElementTree.Element)


def test_get_root():
    assert isinstance(get_root(PATH_TO_FILE), xml.etree.ElementTree.Element)
