'''Write a Python program to find the index of the last element in the given list that satisfies the provided testing function.
Sample Output:
2'''

def find_last_index(lst, test_func):
    for index in range(len(lst) - 1, -1, -1):
        if test_func(lst[index]):
            return index
    return None

def is_even(x):
    return x % 2 == 0
sample_list = [1, 3, 4, 6, 8, 9, 4]
index = find_last_index(sample_list, is_even)
print(index)

