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
        

def gen_diff(file1, file2):
    data1 = load_file(file1)
    data2 = load_file(file2)
    merge = sorted(set(data1) | set(data2))  # мердж-обеденение-сортировка по ключам в список

    s = []  # строка для вывода

    for i in range(len(merge)):  # цикл по ключам в 2 фаилах json согласно условиям задачи
        if merge[i] in data1 and merge[i] in data2 and data1[merge[i]] == data2[merge[i]]: 
            s.append(f"    {merge[i]}: {data1[merge[i]]}")
        if merge[i] in data1 and merge[i] not in data2: 
            s.append(f"  - {merge[i]}: {data1[merge[i]]}")
        if merge[i] in data1 and merge[i] in data2 and data1[merge[i]] != data2[merge[i]]:
            s.append(f"  - {merge[i]}: {data1[merge[i]]}")
            s.append(f"  + {merge[i]}: {data2[merge[i]]}")
        if merge[i] not in data1 and merge[i] in data2:
            s.append(f"  + {merge[i]}: {data2[merge[i]]}")
    s.insert(0, '{')
    s.insert(999, '}')

    return '\n'.join(s).replace('False', 'false').replace('True', 'true').replace('None', 'null')  # возвращаем строку(заменяем булевы значения)




    




