'''Write a  Python program to map the values of a list to a dictionary using a function, where the key-value pairs consist of the original value as the key and the result of the function as the value.
Sample Output:
{1: 1, 2: 4, 3: 9}'''

def square_function(x):
    return x ** 2

def map_list_to_dictionary(lst, func):
    return {value: func(value) for value in lst}

sample_list = [1, 2, 3]
result_dict = map_list_to_dictionary(sample_list, square_function)
print(result_dict)
