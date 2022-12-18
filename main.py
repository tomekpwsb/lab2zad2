import csv
import json
from PIL import ImageColor


def csv_to_json(csvFilePaths, jsonFilePath):
    jsonArray = []
    for file in csvFilePaths:
        with open(file, encoding='utf-8') as csvf:
            csvReader = csv.DictReader(csvf)
            for row in csvReader:
                jsonArray.append(row)

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)


def json_loads_and_print(json_file):
    with open(json_file, 'r', encoding='utf-8') as jsonf:
        data = json.load(jsonf)
        for i in data:
            rgbValue = ImageColor.getcolor(i['value'],'RGB')
            print(f"{i['color']} - {i['value']} - {rgbValue}")



jsonFilePath = r'data.json'
csv_to_json(['example.csv', 'example1.csv', 'example2.csv'], jsonFilePath)
json_loads_and_print(jsonFilePath)

