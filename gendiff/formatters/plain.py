from gendiff.utils.redactors import *


HALFINDENT = ' ' * 2
FULLINDENT = ' ' * 4


def make_plain(diff):
    output = '{'
    if len(diff) > 0:
        output += '\n'
    for node in diff:
        output += node_to_str(node) + '\n'
    output += '}'
    return output


def node_to_str(node):
    node_type = get_node_type(node)
    result = []
    if node_type == UNCHANGED:
        result = (f"{FULLINDENT}{node['old_name']}: "
                  f"{value_to_json(node['old_value'])}")
    elif node_type == REMOVED:
        result = (f"{HALFINDENT}- {node['old_name']}: "
                  f"{value_to_json(node['old_value'])}")
    elif node_type == ADDED:
        result = (f"{HALFINDENT}+ {node['new_name']}: "
                  f"{value_to_json(node['new_value'])}")
    elif node_type == UPDATED:
        first_str = (f"{HALFINDENT}- {node['old_name']}"
                     f": {value_to_json(node['old_value'])}")
        second_str = (f"{HALFINDENT}+ {node['new_name']}"
                      f": {value_to_json(node['new_value'])}")
        result = first_str + '\n' + second_str
    else:
        raise ValueError(f"Node type '{node_type}' is unknown")
    return result
