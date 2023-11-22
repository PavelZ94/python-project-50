import json
import yaml


def open_file(file_path):
    if file_path.endswith('.json'):
        with open(file_path, 'r') as file:
            return json.load(file)
    elif file_path.endswith(('.yml', '.yaml')):
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    else:
        raise NameError(f'The {file_path} have to be json or yaml format')
