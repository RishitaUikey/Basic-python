'''Write a Python program to create a flat list of all the values in a flat dictionary.
Sample Output:
Original dictionary elements:
{'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
Create a flat list of all the values of the said flat dictionary:
[19, 20, 21, 20]'''

def flat_values(input_dict):
    return list(input_dict.values())

original_dict = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
values_list = flat_values(original_dict)

print("Original dictionary elements:")
print(original_dict)
print("Create a flat list of all the values of the said flat dictionary:")
print(values_list)

