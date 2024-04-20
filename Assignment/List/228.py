''' Write a  Python program to get every element that exists in any of the two given lists once, after applying the provided function to each element of both.
Sample Output:
[2.2, 4.1]'''

def apply_function(lst, func):
    return [func(x) for x in lst]

def get_unique_elements(lst1, lst2, func):
    transformed_lst1 = apply_function(lst1, func)
    transformed_lst2 = apply_function(lst2, func)
    combined_set = set(transformed_lst1) | set(transformed_lst2)
    return list(combined_set)

def add_one(x):
    return x + 1
list1 = [1, 2, 3]
list2 = [3.1, 4, 5]
unique_elements = get_unique_elements(list1, list2, add_one)
print(unique_elements)


