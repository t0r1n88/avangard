def load_dataset():
    # TODO Реализовать автоматическую загрузку датасетов выложеных на сайте trudvsem
    # TODO Реализовать обозначение датасета дотой в формате 21-07-2020
    # TODO Реализовать обработку исключений и ошибок при  загрузке
    pass


def parse_xml(data):
    import xml.etree.ElementTree as ET
    # Создаем структуру дерева с помощью parse
    tree = ET.parse(data)
    # Получаем корень дерева
    root = tree.getroot()
    print(root[0].attrib,root[0].text)
    print(root[1].attrib,root[1].text)
    print(root[1][1].attrib,root[1][1].text)
    print(root[1][2][0][3].attrib,root[1][2][0][3].text)

    # Так как объект element tree является связным графом мы можем легко ходить по нему
    # for elem in root:
    #     print(elem.find('statistics')).get('value')
    #     for subelem in elem:
    #         print('************')





def export_to_excel(data):
    # TODO Реализовать экспорт в файл формата xlsx удобный для анализа.
    pass
