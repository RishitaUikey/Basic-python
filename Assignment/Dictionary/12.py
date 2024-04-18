# Write a  Python program to remove a key from a dictionary.

my_dict = {'apple': 3, 'banana': 5, 'orange': 2}
key_to_remove = 'banana'
if key_to_remove in my_dict:
    del my_dict[key_to_remove]
    print(f"The key '{key_to_remove}' has been removed from the dictionary.")
else:
    print(f"The key '{key_to_remove}' does not exist in the dictionary.")

print("Updated dictionary:", my_dict)
