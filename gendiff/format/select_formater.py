from gendiff.format.json import json_formater
from gendiff.format.plain import plain
from gendiff.format.stylish import stylish


def select_formater(formater, data_tree):
    if formater == 'stylish':
        return stylish(data_tree)
    if formater == 'plain':
        return plain(data_tree)
    if formater == 'json':
        return json_formater(data_tree)
    else:
        return print(f'Unknown format {formater}')