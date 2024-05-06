# Write a  Python program to find the length of a dictionary of values.


original_dict = {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
def dict_values_length(dictionary):
    return sum(len(values) for values in dictionary.values())

length = dict_values_length(original_dict)
print("Length of dictionary values:", length)