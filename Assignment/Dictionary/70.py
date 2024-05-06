'''Write a  Python program to map the values of a given list to a dictionary using a function, where the key-value pairs consist of the original value as the key and the result of the function as the value.
Sample Output:
{1: 1, 2: 4, 3: 9, 4: 16}'''

def map_to_dict(lst, func):
    return {value: func(value) for value in lst}

lst = [1, 2, 3, 4]
func = lambda x: x**2
result = map_to_dict(lst, func)
print(result)
