'''Write a Python program to split values into two groups, based on the result of the given filter list.
Sample Output:
[['red', 'green', 'pink'], ['blue']]'''

def split_by_filter(values, filters):
    group1 = []
    group2 = []
    for value, filter_value in zip(values, filters):
        if filter_value:
            group1.append(value)
        else:
            group2.append(value)
    return [group1, group2]

values = ['red', 'blue', 'green', 'pink']
filters = [True, False, True, True]
groups = split_by_filter(values, filters)
print(groups)


