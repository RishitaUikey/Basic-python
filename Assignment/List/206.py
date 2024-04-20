'''Write a  Python program to remove additional spaces from a given list.
Original list:
['abc ', ' ', ' ', 'sdfds ', ' ', ' ', 'sdfds ', 'huy']
Remove additional spaces from the said list:
['abc', '', '', 'sdfds', '', '', 'sdfds', 'huy']'''

def remove_additional_spaces(lst):
    cleaned_list = []
    for item in lst:
        cleaned_list.append(item.strip())
    return cleaned_list

original_list = ['abc ', ' ', ' ', 'sdfds ', ' ', ' ', 'sdfds ', 'huy']
print("Original list:")
print(original_list)
print("Remove additional spaces from the given list:")
print(remove_additional_spaces(original_list))
