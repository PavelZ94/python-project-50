from gendiff.utils.redactors import *


FULLINDENT = ' ' * 4
HALFINDENT = ' ' * 2


def make_stylish(diff, depth=0):
    output = '{'
    if len(diff) > 0:
        output += '\n'
    for node in diff:
        output += node_to_str(node, depth) + '\n'
    output += FULLINDENT * depth + '}'
    return output


def node_to_str(node, depth):
    node_type = get_node_type(node)
    result = []
    if node_type == BOTH_HAVE_CHILDREN:
        result = (f"{FULLINDENT * depth}{FULLINDENT}{node['old_name']}: "
                  f"{make_stylish(node['children'], depth + 1)}")
    elif node_type == UNCHANGED:
        result = (f"{FULLINDENT * depth}{FULLINDENT}{node['old_name']}: "
                  f"{value_to_json(node['old_value'])}")
    elif node_type == REMOVED:
        result = (f"{FULLINDENT * depth}{HALFINDENT}- {node['old_name']}: "
                  f"{value_to_str(node['old_value'], depth)}")
    elif node_type == ADDED:
        result = (f"{FULLINDENT * depth}{HALFINDENT}+ {node['new_name']}: "
                  f"{value_to_str(node['new_value'], depth)}")
    elif node_type == UPDATED:
        first_str = (f"{FULLINDENT * depth}{HALFINDENT}- {node['old_name']}"
                     f": {value_to_str(node['old_value'], depth)}")
        second_str = (f"{FULLINDENT * depth}{HALFINDENT}+ {node['new_name']}"
                      f": {value_to_str(node['new_value'], depth)}")
        result = first_str + '\n' + second_str
    else:
        raise ValueError(f"Node type '{node_type}' is unknown")
    return result


def value_to_str(value, depth):
    if not isinstance(value, dict):
        return value_to_json(value)
    return dict_to_str(value, depth + 1)


def dict_to_str(dictionary, depth):
    output = '{'
    if len(dictionary) > 0:
        output += '\n'
    for key in sorted(dictionary.keys()):
        value = dictionary[key]
        if not isinstance(value, dict):
            output += (f'{FULLINDENT * (depth + 1)}{key}: '
                       f'{value_to_json(value)}' + '\n')
        else:
            output += (f'{FULLINDENT * (depth + 1)}{key}: '
                       f'{dict_to_str(value, depth + 1)}' + '\n')
    output += FULLINDENT * depth + '}'
    return output
