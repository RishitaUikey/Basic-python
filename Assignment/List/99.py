''' Write a  Python program to find the maximum and minimum values in a given heterogeneous list.
Original list:
['Python', 3, 2, 4, 5, 'version']
Maximum and Minimum values in the said list:
(5, 2)'''

def find_max_min(lst):
    numeric_values = [x for x in lst if isinstance(x, int) or isinstance(x, float)]
    
    if numeric_values:
    
        maximum_value = max(numeric_values)
        minimum_value = min(numeric_values)
        return maximum_value, minimum_value
    else:
        return None, None

original_list = ['Python', 3, 2, 4, 5, 'version']
max_val, min_val = find_max_min(original_list)

print("Original list:")
print(original_list)
print("Maximum and Minimum values in the said list:")
print((max_val, min_val))
