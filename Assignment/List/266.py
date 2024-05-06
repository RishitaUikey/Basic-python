'''Write a  Python program to cast the provided value as a list if it's not one.
Sample Output:
<class 'list'>
[1]
<class 'tuple'>
['Red', 'Green']
<class 'set'>
['Green', 'Red']
<class 'dict'>
[1, 2, 3]'''

def cast_to_list(value):
    if not isinstance(value, list):
        return list(value)
    return value

sample_values = [
    [1],
    ('Red', 'Green'),
    {'Green', 'Red'},
    {'a': 1, 'b': 2, 'c': 3}
]

for value in sample_values:
    print(type(cast_to_list(value)))
    print(cast_to_list(value))
