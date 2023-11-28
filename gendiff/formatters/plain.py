from gendiff.utils import redactors


TWO_SPACES = ' ' * 2
FOUR_SPACES = ' ' * 4


def make_plain(diff):
    output = '{'
    if len(diff) > 0:
        output += '\n'
    for node in diff:
        output += node_to_str(node) + '\n'
    output += '}'
    return output


def node_to_str(node):
    node_type = redactors.get_node_type(node)
    result = []
    if node_type == redactors.UNCHANGED:
        result = (f"{FOUR_SPACES}{node['old_name']}: "
                  f"{redactors.value_to_json(node['old_value'])}")
    elif node_type == redactors.REMOVED:
        result = (f"{TWO_SPACES}- {node['old_name']}: "
                  f"{redactors.value_to_json(node['old_value'])}")
    elif node_type == redactors.ADDED:
        result = (f"{TWO_SPACES}+ {node['new_name']}: "
                  f"{redactors.value_to_json(node['new_value'])}")
    elif node_type == redactors.UPDATED:
        first_str = (f"{TWO_SPACES}- {node['old_name']}"
                     f": {redactors.value_to_json(node['old_value'])}")
        second_str = (f"{TWO_SPACES}+ {node['new_name']}"
                      f": {redactors.value_to_json(node['new_value'])}")
        result = first_str + '\n' + second_str
    else:
        raise ValueError(f"Node type '{node_type}' is unknown")
    return result
