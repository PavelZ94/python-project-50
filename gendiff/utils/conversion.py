import json


def open_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
