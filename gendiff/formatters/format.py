from gendiff.formatters.plain import make_plain
from gendiff.formatters.stylish import make_stylish


def get_result(diff, format_name):
    if format_name == 'STYLISH':
        return make_stylish(diff)
    if format_name == 'PLAIN':
        return make_plain(diff)
