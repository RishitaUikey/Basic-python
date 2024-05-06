'''Write a  Python program to drop empty items from a given dictionary.
Original Dictionary:
{'c1': 'Red', 'c2': 'Green', 'c3': None}
New Dictionary after dropping empty items:
{'c1': 'Red', 'c2': 'Green'}'''

original_dict = {'c1': 'Red', 'c2': 'Green', 'c3': None}
new_dict = {key: value for key, value in original_dict.items() if value is not None}

print("New Dictionary after dropping empty items:")
print(new_dict)
