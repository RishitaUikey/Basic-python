'''Write a  Python program to invert a given dictionary with non-unique hashable values.
Sample Output:
{8: ['Ora Mckinney', 'Mathew Gilbert'], 7: ['Theodore Hollandl', 'Mae Fleming', 'Ivan Little']}'''

def invert_dictionary(original_dict):
    inverted_dict = {}
    for key, value in original_dict.items():
        if value not in inverted_dict:
            inverted_dict[value] = [key]
        else:
            inverted_dict[value].append(key)
    return inverted_dict

original_dict = {
    1: 'Alice',
    2: 'Bob',
    3: 'Alice',
    4: 'Charlie',
    5: 'Bob',
    6: 'Alice'
}

inverted_dict = invert_dictionary(original_dict)
print("Inverted Dictionary:")
print(inverted_dict)
