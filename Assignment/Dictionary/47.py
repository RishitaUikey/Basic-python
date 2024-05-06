'''Write a  Python program to split a given dictionary of lists into lists of dictionaries.
Original dictionary of lists:
{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
Split said dictionary of lists into list of dictionaries:
[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]'''

dict_of_lists = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
list_of_dicts = [{key: values[i] for key, values in dict_of_lists.items()} for i in range(len(dict_of_lists[next(iter(dict_of_lists))]))]

print("Splitting the dictionary of lists into list of dictionaries:")
print(list_of_dicts)
