# Write a Python program to check if multiple keys exist in a dictionary.

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
keys_to_check = ['a', 'b', 'e']
all_keys_exist = all(key in my_dict for key in keys_to_check)
print("All keys exist:", all_keys_exist)
