# Write a Python program to sort a list alphabetically in a dictionary.

my_dict = {'list1': ['banana', 'apple', 'cherry'],
           'list2': ['orange', 'grape', 'pear']}

sorted_dict = {key: sorted(value) for key, value in my_dict.items()}

print(sorted_dict)
