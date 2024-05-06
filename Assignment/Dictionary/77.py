'''Write a  Python program to transform a dictionary into a list of tuples.
Sample Output:
Original Dictionary:
{'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
Convert the said dictionary to a list of tuples:
[('Red', 1), ('Green', 3), ('White', 5), ('Black', 2), ('Pink', 4)]'''

def dict_to_list_of_tuples(input_dict):
    return list(input_dict.items())

original_dict = {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
result_list = dict_to_list_of_tuples(original_dict)

print("Original Dictionary:")
print(original_dict)
print("Convert the said dictionary to a list of tuples:")
print(result_list)
