'''Write a Python program to create a list with unique values filtered out.
Sample Output:
[2, 4]'''

def filter_unique(lst):
    return [item for item in lst if lst.count(item) > 1]
sample_list = [1, 2, 3, 3, 4, 4, 5]
filtered_list = filter_unique(sample_list)
print(filtered_list)


