'''. Write a  Python program to remove all values except integer values from a given array of mixed values.
Original list: [34.67, 12, -94.89, 'Python', 0, 'C#']
After removing all the values except integer values from the said array of mixed values: [12, 0]'''

def filter_integers_from_list(mixed_list):
    return [item for item in mixed_list if isinstance(item, int)]
original_list = [34.67, 12, -94.89, 'Python', 0, 'C#']
print("Original list:")
print(original_list)
filtered_list = filter_integers_from_list(original_list)
print("After removing all the values except integer values from the said array of mixed values:")
print(filtered_list)
