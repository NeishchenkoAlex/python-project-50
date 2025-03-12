import json

import yaml


def load_file(file):
    extension = file.split('.')[-1]
    if extension == 'json':
        with open(f'{file}', 'r') as file:  # открытие json
            return json.load(file)
    if extension == 'yaml' or extension == 'yml':
        with open(f'{file}') as file:
            return yaml.load(file, Loader=yaml.FullLoader)
    else:
        raise ValueError(f"Unknown format: {extension}")