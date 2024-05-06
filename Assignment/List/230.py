'''Write a Python program to find the indexes of all elements in the given list that satisfy the provided testing function.
Sample Output:
[0, 2]'''

def find_indexes(lst, test_func):
    indexes = []
    for index, item in enumerate(lst):
        if test_func(item):
            indexes.append(index)
    return indexes

def is_even(x):
    return x % 2 == 0
sample_list = [1, 3, 4, 6, 8, 9]
indexes = find_indexes(sample_list, is_even)
print(indexes)
