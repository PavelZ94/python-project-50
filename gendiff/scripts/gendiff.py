#!/usr/bin/env python3
from gendiff import generate_diff, parse_args

file1 = 'gendiff/modules/file1.json'
file2 = 'gendiff/modules/file2.json'


def main():
    args = parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
