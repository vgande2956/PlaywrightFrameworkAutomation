import json


def read_json_file(file_name):
    with open(file_name, "r") as file:
        data = json.load(file)
        print(data)
        return data