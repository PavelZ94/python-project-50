from gendiff.utils.conversion import open_file
from gendiff.formatters.format import get_result


def generate_diff(file1, file2, format_name='STYLISH'):
    data1 = open_file(file1)
    data2 = open_file(file2)
    diff = generate(data1, data2)
    return get_result(diff, format_name)


def generate(data1, data2):
    all_keys = get_all_keys(data1, data2)
    difference = []
    for key in sorted(list(all_keys)):
        old_name = key if key in data1 else None
        new_name = key if key in data2 else None
        val1 = data1.get(key)
        val2 = data2.get(key)
        both_nodes_have_children = bool(
            type(val1) == type(val2) == dict)
        if both_nodes_have_children:
            old_value = None
            new_value = None
            children = generate(val1, val2)
        else:
            old_value = val1
            new_value = val2
            children = None
        diff_node = {
            'old_name': old_name,
            'new_name': new_name,
            'old_value': old_value,
            'new_value': new_value,
            'children': children
        }
        check_invariant(diff_node)
        difference.append(diff_node)
    return difference


def get_all_keys(dict1, dict2):
    set1 = set(dict1.keys())
    set2 = set(dict2.keys())
    return set1 | set2


def check_invariant(diff_node):
    if diff_node['old_name'] != diff_node['new_name'] and \
            diff_node['old_name'] is not None and \
            diff_node['new_name'] is not None:
        raise ValueError(f"old_name '{diff_node['old_name']} and new_name "
                         f"{diff_node['new_name']} can't be unequal")
