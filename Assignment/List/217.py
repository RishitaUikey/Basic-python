'''Write a Python program to split values into two groups, based on the result of the given filtering function.
Sample Output:
[['white'], ['red', 'green', 'black']]'''

def split_values(values, filter_func):
    group1 = []
    group2 = []
    for value in values:
        if filter_func(value):
            group1.append(value)
        else:
            group2.append(value)
    return [group1, group2]

def is_white(color):
    return color == 'white'
values = ['white', 'red', 'green', 'black']
result = split_values(values, is_white)
print(result)
