'''Write a  Python program to get the minimum value of a list, after mapping each element to a value using a given function.
Sample Output:
2'''

def map_and_get_min(lst, func):
    mapped_values = [func(x) for x in lst]
    return min(mapped_values)

def double(x):
    return x * 2

sample_list = [1, 2, 3, 4]
min_value = map_and_get_min(sample_list, double)
print(min_value)

