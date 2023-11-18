
def converter(input_dict):
    output_dict = {}
    for key, value in input_dict.items():
        if isinstance(key, bool) or isinstance(key, type(None)):
            key = str(key).lower()
        if isinstance(value, bool) or isinstance(value, type(None)):
            value = str(value).lower()
        output_dict[key] = value
    return output_dict


def string_redactor(input_dict):
    input_string = str(input_dict)
    result = input_string.replace(",", ",\n").replace("'", "")
    return result
