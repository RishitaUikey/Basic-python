'''Write a  Python program to retrieve the value of the nested key indicated by the given selector list from a dictionary or list.
Sample Output:
Russell
2'''

def map_to_dict(lst, func):
    return {value: func(value) for value in lst}
lst = [1, 2, 3, 4]
func = lambda x: x**2
result = map_to_dict(lst, func)
print(result)
