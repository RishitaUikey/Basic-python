'''Write a  Python program to remove duplicate dictionary entries from a given list.
Original list with duplicate dictionary:
[{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]
After removing duplicate dictionary of the said list:
[{'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]'''

def remove_duplicate_dicts(lst):
    tuple_set = {tuple(sorted(d.items())) for d in lst}
    return [dict(t) for t in tuple_set]

original_list = [{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]
result_list = remove_duplicate_dicts(original_list)
print("Original list with duplicate dictionaries:")
print(original_list)
print("After removing duplicate dictionaries:")
print(result_list)

