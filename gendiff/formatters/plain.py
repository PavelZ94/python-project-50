from gendiff.utils import redactors


def make_plain(diff, path=''):
    result = []
    for node in diff:
        node_type = redactors.get_node_type(node)
        curr_path = ".".join(filter(bool, [path, node["new_name"]]))

        old_val = val_to_str(node['old_value'])
        new_val = val_to_str(node['new_value'])

        if node_type == redactors.BOTH_HAVE_CHILDREN:
            result.append(make_plain(node['children'], curr_path))
        elif node_type == redactors.REMOVED:
            result.append(f"Property '{node['old_name']}' was removed")
        elif node_type == redactors.ADDED:
            result.append(f"Property '{curr_path}' was added with "
                          f"value: {new_val}")
        elif node_type == redactors.UPDATED:
            result.append(f"Property '{curr_path}' was updated. "
                          f"From {old_val} to {new_val}")
        else:
            pass
    return "\n".join(result)


def val_to_str(node):
    if isinstance(node, dict):
        return '[complex value]'
    elif node in ['true', 'false', 'null']:
        return redactors.value_to_json(node)
    else:
        return f"'{redactors.value_to_json(node)}'"
