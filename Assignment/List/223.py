''' Write a  Python program to create a list with non-unique values filtered out.
Sample Output:
[1, 3, 5]'''

def filter_non_unique(lst):
    return [item for item in lst if lst.count(item) == 1]
sample_list = [1, 2, 3, 3, 4, 5, 5]
filtered_list = filter_non_unique(sample_list)
print(filtered_list)


