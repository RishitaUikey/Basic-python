'''Write a  Python program to convert a given list of lists to a dictionary.
Original list of lists:
[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
Convert the said list of lists to a dictionary:
{1: ['Jean Castro', 'V'], 2: ['Lula Powell', 'V'], 3: ['Brian Howell', 'VI'], 4: ['Lynne Foster', 'VI'], 5: ['Zachary Simon', 'VII']}'''

def list_of_lists_to_dict(list_of_lists):
    return {sublist[0]: sublist[1:] for sublist in list_of_lists}

original_list = [
    [1, 'Jean Castro', 'V'],
    [2, 'Lula Powell', 'V'],
    [3, 'Brian Howell', 'VI'],
    [4, 'Lynne Foster', 'VI'],
    [5, 'Zachary Simon', 'VII']
]

result_dict = list_of_lists_to_dict(original_list)
print("Convert the said list of lists to a dictionary:")
print(result_dict)
