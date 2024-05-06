'''Write a Python program to find items starting with a specific character from a list.
Expected Output:
Original list:
['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
Items start with a from the said list:
['abcd', 'abc', 'acjd']
Items start with d from the said list:
['dagfa']
Items start with w from the said list:
[]'''

original_list = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
def find_items_starting_with_character(lst, char):
    
    return [item for item in lst if item.startswith(char)]

test_characters = ['a', 'd', 'w']
for char in test_characters:
    matching_items = find_items_starting_with_character(original_list, char)
    print(f"Items start with {char} from the said list:")
    print(matching_items)