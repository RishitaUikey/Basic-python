# Write a Python program to convert a list into a nested dictionary of keys.

def list_to_nested_dict(keys, value):
    if len(keys) == 1:
        return {keys[0]: value}
    else:
        return {keys[0]: list_to_nested_dict(keys[1:], value)}

def list_to_nested_dict_from_list(lst, value):
    result = {}
    for keys in lst:
        result.update(list_to_nested_dict(keys, value))
    return result
keys_list = [['a', 'b', 'c'], ['d', 'e'], ['f']]
value = 'value'
nested_dict = list_to_nested_dict_from_list(keys_list, value)
print(nested_dict)
