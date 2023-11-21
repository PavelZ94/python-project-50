from gendiff.utils.redactors import converter
from gendiff.utils.redactors import string_redactor
from gendiff.utils.conversion import open_file


def generate_diff(file1, file2):
    data1 = open_file(file1)
    data2 = open_file(file2)
    new_data1 = converter(data1)
    new_data2 = converter(data2)
    result_dict = make_diff(new_data1, new_data2)
    result = string_redactor(result_dict)
    return result


def make_diff(new_data1, new_data2):
    result_dict = {}
    for k, v in new_data1.items():
        if k in new_data2 and new_data1[k] == new_data2[k]:
            new_k = '  ' + k
            result_dict[new_k] = v
        elif new_data1[k] not in new_data2:
            new_k = '- ' + k
            result_dict[new_k] = v
    for k, v in new_data2.items():
        if k not in new_data1 or new_data1[k] != new_data2[k]:
            new_k = '+ ' + k
            result_dict[new_k] = v
    result_dict = dict(sorted(result_dict.items(), key=lambda x: x[0][2]))
    return result_dict
