'''Write a  Python program to combine two or more dictionaries, creating a list of values for each key.
Sample Output:
Original dictionaries:
{'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
{'x': 300, 'y': 'Red', 'z': 600}
Combined dictionaries, creating a list of values for each key:
{'w': [50], 'x': [100, 300], 'y': ['Green', 'Red'], 'z': [400, 600]}'''

def combine_dictionaries(*dicts):
    combined_dict = {}
    for d in dicts:
        for key, value in d.items():
            if key not in combined_dict:
                combined_dict[key] = [value]
            else:
                combined_dict[key].append(value)
    return combined_dict

dict1 = {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
dict2 = {'x': 300, 'y': 'Red', 'z': 600}
combined_dict = combine_dictionaries(dict1, dict2)

print("Combined dictionaries, creating a list of values for each key:")
print(combined_dict)
