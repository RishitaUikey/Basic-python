# Write a  Python program to remove spaces from dictionary keys.

original_dict = {'key 1': 1, 'key 2': 2, 'key 3': 3}
modified_dict = {key.replace(' ', ''): value for key, value in original_dict.items()}
print(modified_dict)
