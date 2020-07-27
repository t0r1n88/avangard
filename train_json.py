import json

dictData = {'values': [["ID": 210450,
                       "login": "admin",
                       "name": "John Smith",
                       "password": "root",
                       "телефон": 5550505,
                       "email": "smith@mail.com",
                       "online": True]]}

dictData1 = {"ID": 4353453,
             "login": "admin",
             "name": "LOGAn",
             "password": "root",
             "телефон": 4535353,
             "email": "smith@mail.com",
             "online": True}
# jsonData = json.dumps(dictData,ensure_ascii=False)
# with open('data/data.json','w',encoding='utf-8') as file:
#     file.write((jsonData))
with open('data/data.json') as file:
    data = json.load(file)
