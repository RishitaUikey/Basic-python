'''Write a Python program to convert a dictionary into a list of lists.
Original Dictionary:
{1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
Convert the said dictionary into a list of lists:
[[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]
Original Dictionary:
{'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
Convert the said dictionary into a list of lists:
[['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 'Jamie Rowe']]'''

original_dict1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
original_dict2 = {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}

list_of_lists1 = [[key, value] for key, value in original_dict1.items()]
list_of_lists2 = [[key, value] for key, value in original_dict2.items()]

print("Original Dictionary:")
print(original_dict1)
print("Convert the said dictionary into a list of lists:")
print(list_of_lists1)

print("\nOriginal Dictionary:")
print(original_dict2)
print("Convert the said dictionary into a list of lists:")
print(list_of_lists2)
