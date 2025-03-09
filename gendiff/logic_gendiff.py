import json


def gen_diff(file1, file2):
    with open(f'{file1}', 'r') as file:  # открытие json
        data1 = json.load(file)  # чтение json
    with open(f'{file2}', 'r') as file:
        data2 = json.load(file)
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


print(gen_diff('tests/files/file1.json', 'tests/files/file2.json'))

    




