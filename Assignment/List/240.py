''' Write a  Python program to find the value of the last element in the given list that satisfies the provided testing function.
Sample Output:
3
4'''

def find_last_value(lst, test_func):
    for item in reversed(lst):
        if test_func(item):
            return item
    return None
def is_even(x):
    return x % 2 == 0
sample_list1 = [1, 2, 3, 4, 5]
sample_list2 = [2, 4, 6, 8, 10, 3, 5, 7]
last_value1 = find_last_value(sample_list1, is_even)
print(last_value1)
last_value2 = find_last_value(sample_list2, is_even)
print(last_value2)

