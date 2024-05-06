'''Write a  Python program to extract values from a given dictionary and create a list of lists from those values.
Original Dictionary:
[{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]
Extract values from the said dictionarie and create a list of lists using those values:
[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
[[1, 'Jean Castro'], [2, 'Lula Powell'], [3, 'Brian Howell'], [4, 'Lynne Foster'], [5, 'Zachary Simon']]
[['Jean Castro', 'V'], ['Lula Powell', 'V'], ['Brian Howell', 'VI'], ['Lynne Foster', 'VI'], ['Zachary Simon', 'VII']]'''

def extract_values(dictionary_list, keys):
    result = []
    for d in dictionary_list:
        values = [d[key] for key in keys]
        result.append(values)
    return result

original_dict_list = [
    {'student_id': 1, 'name': 'Jean Castro', 'class': 'V'},
    {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
    {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'},
    {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'},
    {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}
]

keys1 = ['student_id', 'name', 'class']
result1 = extract_values(original_dict_list, keys1)
print("Extract values from the said dictionaries and create a list of lists using those values:")
print(result1)

keys2 = ['student_id', 'name']
result2 = extract_values(original_dict_list, keys2)
print("\nExtract values but only student_id and name, and create a list of lists:")
print(result2)

keys3 = ['name', 'class']
result3 = extract_values(original_dict_list, keys3)
print("\nExtract values but only name and class, and create a list of lists:")
print(result3)
