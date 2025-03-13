from gendiff.data_load import load_file
from gendiff.format.select_formater import select_formater
from gendiff.gendiff_tree import build_tree


def generate_diff(file1, file2, format='stylish'):
    data1 = load_file(file1)
    data2 = load_file(file2)
    
    diff_tree = build_tree(data1, data2)
    
    return select_formater(format, diff_tree)




