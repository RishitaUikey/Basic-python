''' Write a  Python program that creates key-value list pairings within a dictionary.
Original dictionary:
{1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
A key-value list pairings of the said dictionary:
[{1: 'Jean Castro', 2: 'Lula Powell', 3: 'Brian Howell', 4: 'Lynne Foster', 5: 'Zachary Simon'}]'''

def key_value_list_pairings(input_dict):
    return [dict(zip(input_dict.keys(), [value[0] for value in input_dict.values()]))]

original_dict = {
    1: ['Jean Castro'],
    2: ['Lula Powell'],
    3: ['Brian Howell'],
    4: ['Lynne Foster'],
    5: ['Zachary Simon']
}

pairings = key_value_list_pairings(original_dict)
print("A key-value list pairings of the said dictionary:")
print(pairings)
