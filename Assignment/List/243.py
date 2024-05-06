'''Write a  Python program to check if a given function returns True for every element in a list.
Sample Output:
True
False
False'''

def check_all(lst, func):
    return all(func(item) for item in lst)

def is_positive(x):
    return x > 0
sample_list1 = [1, 2, 3, 4, 5]
sample_list2 = [1, 2, -3, 4, 5]
sample_list3 = [-1, -2, -3, -4, -5]
result1 = check_all(sample_list1, is_positive)
result2 = check_all(sample_list2, is_positive)
result3 = check_all(sample_list3, is_positive)
print(result1)
print(result2)
print(result3)

