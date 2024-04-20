'''Write a  Python program to find the index of the first element in the given list that satisfies the provided testing function.
Sample Output:
0'''

def find_index(lst, test_func):
    for index, item in enumerate(lst):
        if test_func(item):
            return index
    return None
def is_even(x):
    return x % 2 == 0
sample_list = [1, 3, 4, 6, 8, 9]
index = find_index(sample_list, is_even)
print(index)

