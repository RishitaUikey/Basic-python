'''Write a PWrite a Python program to get the symmetric difference between two lists, after applying the provided function to each list element of both.
Sample Output:
[1.2, 3.4]ython program to get a list of elements that exist in both lists, after applying the provided function to each list element of both.
Sample Output:
[2.1]'''

def apply_function(lst, func):
    return [func(x) for x in lst]

def get_common_elements(lst1, lst2, func):
    transformed_lst1 = apply_function(lst1, func)
    transformed_lst2 = apply_function(lst2, func)
    return list(set(transformed_lst1) & set(transformed_lst2))

def square_root(x):
    return x ** 0.5
list1 = [1, 4, 9]
list2 = [4.41, 0.25, 1]
common_elements = get_common_elements(list1, list2, square_root)
print(common_elements)

