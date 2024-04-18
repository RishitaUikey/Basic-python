''' Write a  Python program to merge more than one dictionary into a single expression.
Sample Output:
Original dictionaries:
{'R': 'Red', 'B': 'Black', 'P': 'Pink'} {'G': 'Green', 'W': 'White'}
Merged dictionary:
{'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White'}
Original dictionaries:
{'R': 'Red', 'B': 'Black', 'P': 'Pink'} {'G': 'Green', 'W': 'White'} {'O': 'Orange', 'W': 'White', 'B': 'Black'}
Merged dictionary:
{'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}'''

dict1 = {'R': 'Red', 'B': 'Black', 'P': 'Pink'}
dict2 = {'G': 'Green', 'W': 'White'}
dict3 = {'O': 'Orange', 'W': 'White', 'B': 'Black'}

merged_dict = {**dict1, **dict2, **dict3}

print("Original dictionaries:")
print(dict1, dict2, dict3)

print("Merged dictionary:")
print(merged_dict)
