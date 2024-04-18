'''Write a  Python program to find all keys in a dictionary that have the given value.
Sample Output:
Original dictionary elements:
{'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
Find all keys in the said dictionary that have the specified value:
['Roxanne', 'Betty']'''

def find_keys_by_value(data, value):
    return [key for key, val in data.items() if val == value]

original_dict = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
specified_value = 20
result = find_keys_by_value(original_dict, specified_value)

print("Original dictionary elements:")
print(original_dict)
print("Find all keys in the said dictionary that have the specified value:")
print(result)
