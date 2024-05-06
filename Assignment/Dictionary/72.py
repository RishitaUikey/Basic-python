'''Write a Python program to invert a dictionary with unique hashable values.
Sample Output:
{10: 'Theodore', 11: 'Mathew', 9: 'Roxanne'}'''

def invert_dictionary(dictionary):
    inverted_dict = {value: key for key, value in dictionary.items()}
    return inverted_dict

sample_dict = {10: 'Theodore', 11: 'Mathew', 9: 'Roxanne'}
inverted_dict = invert_dictionary(sample_dict)
print(inverted_dict)
