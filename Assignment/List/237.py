'''Write a  Python program to convert a given list of dictionaries into a list of values corresponding to the specified key.
Sample Output:
[8, 36, 34, 10]'''

def extract_values(dicts, key):
    return [d[key] for d in dicts]
list_of_dicts = [
    {'a': 5, 'b': 8, 'c': 12},
    {'a': 12, 'b': 36, 'c': 40},
    {'a': 22, 'b': 34, 'c': 51},
    {'a': 4, 'b': 10, 'c': 14}
]
specified_key = 'b'
values = extract_values(list_of_dicts, specified_key)
print(values)

