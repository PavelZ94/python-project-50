#!/usr/bin/env python3
from gendiff import generate_diff, parse_args


def main():
    args = parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
