'''Write a  Python program to get the total length of all values in a given dictionary with string values.
Original dictionary:
{'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
Total length of all values of the said dictionary with string values:
20'''

def total_length_of_values(input_dict):
    return sum(len(value) for value in input_dict.values() if isinstance(value, str))

original_dict = {'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}

total_length = total_length_of_values(original_dict)
print("Total length of all values of the said dictionary with string values:")
print(total_length)
