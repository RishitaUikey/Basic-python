# Write a Python program to get the depth of a dictionary.

def get_dict_depth(dictionary):
    if not isinstance(dictionary, dict):
        return 0
    depths = [get_dict_depth(value) for value in dictionary.values()]
    return max(depths, default=0) + 1

test_dict = {'a': {'b': {'c': {'d': 1}}}, 'x': 2, 'y': {'z': 3}}
depth = get_dict_depth(test_dict)
print("Depth of the dictionary:", depth)
