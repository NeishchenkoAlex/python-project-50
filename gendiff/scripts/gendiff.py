from gendiff.logic_gendiff import gen_diff
from gendiff.parse_arg import parse_args


def main():
    args = parse_args()
    print(gen_diff(args.first_file, args.second_file))


if __name__ == "__main__":
    main()
