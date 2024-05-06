'''Write a  Python program to create a flat list of all the keys in a flat dictionary.
Sample Output:
Original dictionary elements:
{'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
Create a flat list of all the keys of the said flat dictionary:
['Theodore', 'Roxanne', 'Mathew', 'Betty']'''

def flat_keys(input_dict):
    return list(input_dict.keys())

original_dict = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
keys_list = flat_keys(original_dict)

print("Original dictionary elements:")
print(original_dict)
print("Create a flat list of all the keys of the said flat dictionary:")
print(keys_list)
