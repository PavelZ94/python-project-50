import json


file1 = '../modules/file1.json'
file2 = '../modules/file2.json'


def generate_diff(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)
        new_data1 = converter(data1)
        new_data2 = converter(data2)
        result_dict = make_diff(new_data1, new_data2)
        result_str = str(result_dict)
        result = result_str.replace(",", ",\n")
        return result


def converter(input_dict):
    output_dict = {}
    for key, value in input_dict.items():
        if isinstance(key, bool) or isinstance(key, type(None)):
            key = str(key).lower()
        if isinstance(value, bool) or isinstance(value, type(None)):
            value = str(value).lower()
        output_dict[key] = value
    return output_dict


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
    result_dict = dict(sorted(result_dict.items(), key = lambda x: x[0][2]))
    return result_dict
