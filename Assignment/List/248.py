'''Write a Python program to get the maximum value of a list, after mapping each element to a value using a given function.
Sample Output:
8'''

def map_and_get_max(lst, func):
    mapped_values = [func(x) for x in lst]
    return max(mapped_values)

def square(x):
    return x ** 2
sample_list = [1, 2, 3, 4]
max_value = map_and_get_max(sample_list, square)
print(max_value)

