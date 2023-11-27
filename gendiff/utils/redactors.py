
ADDED = "added"
REMOVED = "removed"
UNCHANGED = "unchanged"
UPDATED = "updated"
BOTH_HAVE_CHILDREN = "both_have_children"


def value_to_json(value):
    if value is None:
        result = 'null'
    elif type(value) is bool:
        result = 'true' if value else 'false'
    else:
        result = str(value)
    return result


def get_node_type(node):
    if node["children"]:
        node_type = BOTH_HAVE_CHILDREN
    elif node["old_name"] is None and node["new_name"] is not None:
        node_type = ADDED
    elif node["old_name"] is not None and node["new_name"] is None:
        node_type = REMOVED
    elif node["old_value"] == node["new_value"]:
        node_type = UNCHANGED
    elif node["old_value"] != node["new_value"]:
        node_type = UPDATED
    else:
        raise ValueError(f"Unable to determine type of {node}")
    return node_type
