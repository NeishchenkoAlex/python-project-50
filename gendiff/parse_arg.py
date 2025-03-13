import argparse


def parse_args():
    # Инит утилиты 
    parser = argparse.ArgumentParser(prog='gendiff', 
    description='Compares two configuration files and shows a difference.')
    # позиционные аргументы
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    # опциональные аргументы
    parser.add_argument('-f', '--format', dest='format', type=str, 
                        default='stylish', help='set format of output')
    return parser.parse_args()
