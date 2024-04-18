# Write a Python program to remove duplicates from the dictionary.

def remove_duplicates(dictionary):
    unique_dict = {}
    
    for key, value in dictionary.items():
        if key not in unique_dict:
            unique_dict[key] = value
    
    return unique_dict

original_dict = {'a': 1, 'b': 2, 'c': 3, 'b': 4, 'd': 5, 'a': 6}
result_dict = remove_duplicates(original_dict)
print("Original Dictionary:", original_dict)
print("Dictionary after removing duplicates:", result_dict)
