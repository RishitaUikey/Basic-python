# Write a Python program to check if a dictionary is empty or not.

def is_empty(dictionary):
    if not dictionary:
        return True
    else:
        return False

empty_dict = {}
non_empty_dict = {'a': 1, 'b': 2}

print("Is the empty_dict empty?", is_empty(empty_dict))
print("Is the non_empty_dict empty?", is_empty(non_empty_dict))
