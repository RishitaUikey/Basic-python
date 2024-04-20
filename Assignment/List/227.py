'''Write a Python program to get the symmetric difference between two lists, after applying the provided function to each list element of both.
Sample Output:
[1.2, 3.4]'''

def apply_function(lst, func):
    return [func(x) for x in lst]

def get_symmetric_difference(lst1, lst2, func):
    transformed_lst1 = apply_function(lst1, func)
    transformed_lst2 = apply_function(lst2, func)
    symmetric_diff = list(set(transformed_lst1) ^ set(transformed_lst2))
    return symmetric_diff

def square(x):
    return x * x
list1 = [1, 2, 3]
list2 = [1.44, 3.4, 4]
symmetric_difference = get_symmetric_difference(list1, list2, square)
print(symmetric_difference)


