'''Write a  Python program to check if a given function returns True for at least one element in the list.
Sample Output:
True
False
'''

def check_any(lst, func):
    return any(func(item) for item in lst)

def is_positive(x):
    return x > 0
sample_list1 = [1, 2, 3, 4, 5]
sample_list2 = [-1, -2, -3, -4, -5]
result1 = check_any(sample_list1, is_positive)
result2 = check_any(sample_list2, is_positive)
print(result1)
print(result2)

