''' Write a Python program to check if a specific key and a value exist in a dictionary.
Original dictionary:
[{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]
Check if a specific Key and a value exist in the said dictionary:
True
True
True
False
False
False'''

def check_key_value_existence(list_of_dicts, key, value):
    return any(d.get(key) == value for d in list_of_dicts)

original_list = [
    {'student_id': 1, 'name': 'Jean Castro', 'class': 'V'},
    {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
    {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'},
    {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'},
    {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}
]


key_to_check = 'name'
value_to_check = 'Brian Howell'


print("Check if a specific Key and a value exist in the said dictionary:")
print(check_key_value_existence(original_list, key_to_check, value_to_check))

key_to_check = 'class'
value_to_check = 'V'
print(check_key_value_existence(original_list, key_to_check, value_to_check))

key_to_check = 'class'
value_to_check = 'IX'
print(check_key_value_existence(original_list, key_to_check, value_to_check))

key_to_check = 'name'
value_to_check = 'Ruth Jones'
print(check_key_value_existence(original_list, key_to_check, value_to_check))

key_to_check = 'student_id'
value_to_check = 10
print(check_key_value_existence(original_list, key_to_check, value_to_check))
