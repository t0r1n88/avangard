import xml.etree.ElementTree as ET

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


if __name__ == "__main__":
    # Получаем корень дерева
    # root = get_root(PATH_TO_FILE)
    # Получаем корень с нужным названием.
    # chosen_root = get_chosen_element(root,TEXT)
    tree = ET.parse(PATH_TO_FILE)
    root = tree.getroot()
    for element in tree.findall("region"):  # or tree.findall('globalVariables/globalVariable/name')
        name = element.find("name")
        # print(element.tag, name.text, element.attrib)
        if name.text == 'Республика Бурятия':
            chosen_elem = element
            break

    # for elem in chosen_elem:
    #     print(elem.tag, elem.text, elem.attrib)
    #     for subelem in elem:
    #         print(subelem.tag, subelem.text, subelem.attrib)
    print(type(chosen_elem))

    for elem in chosen_elem.findall('statistics/statistic'):
        name = elem.find("name")
        value = elem.find('value')
        print(name.text,value.text)

