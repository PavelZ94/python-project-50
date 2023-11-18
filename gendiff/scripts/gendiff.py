#!/usr/bin/env python3
from gendiff.generate import generate_diff
from gendiff.cli import parse_args


file1 = 'gendiff/modules/file1.json'
file2 = 'gendiff/modules/file2.json'


def main():
    args = parse_args
    diff = generate_diff(args.file1, args.file2)
    print(diff)


if __name__ == '__main__':
    main()
