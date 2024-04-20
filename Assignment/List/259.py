'''Write a  Python program to check if a given function returns True for at least one element in the list.
Sample Output:
False
True
False'''

def check_function_true(lst, func):
    return any(func(x) for x in lst)

def is_positive(x):
    return x > 0

sample_lists = [
    [-1, -2, -3],
    [-1, 2, -3],
    [-1, -2, -3]
]

for lst in sample_lists:
    print(check_function_true(lst, is_positive))

