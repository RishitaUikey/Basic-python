'''Write a  Python program to create a flat list of all the keys in a flat dictionary.
Sample Output:
Original directory elements:
{'Laura': 10, 'Spencer': 11, 'Bridget': 9, 'Howard ': 10}
Flat list of all the keys of the said dictionary:
['Laura', 'Spencer', 'Bridget', 'Howard ']'''

def flat_list_of_keys(dictionary):
    return list(dictionary.keys())
sample_dict = {'Laura': 10, 'Spencer': 11, 'Bridget': 9, 'Howard ': 10}
print("Original directory elements:")
print(sample_dict)
flat_keys = flat_list_of_keys(sample_dict)
print("Flat list of all the keys of the said dictionary:")
print(flat_keys)
