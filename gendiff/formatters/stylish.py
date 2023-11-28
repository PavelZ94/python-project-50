from gendiff.utils import redactors


FOUR_SPACES = ' ' * 4
TWO_SPACES = ' ' * 2


def make_stylish(diff, depth=0):
    output = '{'
    if len(diff) > 0:
        output += '\n'
    for node in diff:
        output += node_to_str(node, depth) + '\n'
    output += FOUR_SPACES * depth + '}'
    return output


def node_to_str(node, depth):
    node_type = redactors.get_node_type(node)
    result = []
    if node_type == redactors.BOTH_HAVE_CHILDREN:
        result = (f"{FOUR_SPACES * depth}{FOUR_SPACES}{node['old_name']}: "
                  f"{make_stylish(node['children'], depth + 1)}")
    elif node_type == redactors.UNCHANGED:
        result = (f"{FOUR_SPACES * depth}{FOUR_SPACES}{node['old_name']}: "
                  f"{redactors.value_to_json(node['old_value'])}")
    elif node_type == redactors.REMOVED:
        result = (f"{FOUR_SPACES * depth}{TWO_SPACES}- {node['old_name']}: "
                  f"{value_to_str(node['old_value'], depth)}")
    elif node_type == redactors.ADDED:
        result = (f"{FOUR_SPACES * depth}{TWO_SPACES}+ {node['new_name']}: "
                  f"{value_to_str(node['new_value'], depth)}")
    elif node_type == redactors.UPDATED:
        first_str = (f"{FOUR_SPACES * depth}{TWO_SPACES}- {node['old_name']}"
                     f": {value_to_str(node['old_value'], depth)}")
        second_str = (f"{FOUR_SPACES * depth}{TWO_SPACES}+ {node['new_name']}"
                      f": {value_to_str(node['new_value'], depth)}")
        result = first_str + '\n' + second_str
    else:
        raise ValueError(f"Node type '{node_type}' is unknown")
    return result


def value_to_str(value, depth):
    if not isinstance(value, dict):
        return redactors.value_to_json(value)
    return dict_to_str(value, depth + 1)


def dict_to_str(dictionary, depth):
    output = '{'
    if len(dictionary) > 0:
        output += '\n'
    for key in sorted(dictionary.keys()):
        value = dictionary[key]
        if not isinstance(value, dict):
            output += (f'{FOUR_SPACES * (depth + 1)}{key}: '
                       f'{redactors.value_to_json(value)}' + '\n')
        else:
            output += (f'{FOUR_SPACES * (depth + 1)}{key}: '
                       f'{dict_to_str(value, depth + 1)}' + '\n')
    output += FOUR_SPACES * depth + '}'
    return output
