import json

def gen_diff(first_dict, second_dict):
    
    f_dict=json.load(open(first_dict)) #чтение и конвертация в словарь 1 аргумента
    s_dict=json.load(open(second_dict)) #чтение и конвертация в словарь 2 аргумента
    new_list=[] # список в который добавляем ф-строки согласно условиям
    
    for key,value in s_dict.items():
        if key in f_dict:
            if f_dict[key]==value:
                new_list.append(f'  {key}: {s_dict[key]}') # одинаковые key,value
        if key not in f_dict:
            new_list.append(f'+ {key}: {s_dict[key]}') # отсутсвуют в первом словаре
        if key in f_dict:
            if f_dict[key]!=value:
                new_list.append(f'+ {key}: {s_dict[key]}') #разные по value
    
    for key,value in f_dict.items():
        if key in s_dict and s_dict[key]!=value:
            new_list.append(f'- {key}: {f_dict[key]}') #разные по value
        if key not in s_dict:
            new_list.append(f'- {key}: {f_dict[key]}') # отсутсвуют во втором словаре

    
    return '\n'.join(sorted(new_list, key=lambda x:x[2])) # возвращаем отсортированный список
                                                          






    




