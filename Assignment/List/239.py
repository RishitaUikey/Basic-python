'''Write a Python program to find the value of the first element in the given list that satisfies the provided testing function.
Sample Output:
1
2'''

def find_first_value(lst, test_func):
    for item in lst:
        if test_func(item):
            return item
    return None
def is_positive(x):
    return x > 0
sample_list1 = [-1, -2, 1, 2, 3]
sample_list2 = [-2, -4, -6, -8, -10, 2, 4, 6, 8, 10]
first_value1 = find_first_value(sample_list1, is_positive)
print(first_value1)
first_value2 = find_first_value(sample_list2, is_positive)
print(first_value2)


