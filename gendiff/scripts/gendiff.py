from gendiff.scripts.generate_diff import gen_diff as gendiff
import argparse
def main():
    #Название и описание
    parser = argparse.ArgumentParser(prog='gendiff',description='Compares two configuration files and shows a difference.')
    #позиционные аргументы
    parser.add_argument('first_file',help='- Enter first argument',type=str)
    parser.add_argument('second_file', help='- Enter second argument',type=str)
    #опциональные аргументы
    parser.add_argument('-f', '--format', help='set format of output')
    
    args = parser.parse_args()
    #вывод утилиты
    print(gendiff(args.first_file, args.second_file))

    
    


if __name__ == "__main__":
    main()
