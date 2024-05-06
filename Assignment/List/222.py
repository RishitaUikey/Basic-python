'''Write a Python program to get the difference between two given lists, after applying the provided function to each list element of both.
Sample Output:
[1.2]
[{'x': 2}]'''

def apply_function(lst, func):
    return [func(x) for x in lst]

def get_list_difference(lst1, lst2, func):
    result = []
    lst1_transformed = apply_function(lst1, func)
    lst2_transformed = apply_function(lst2, func)
    for item in lst1_transformed:
        if item not in lst2_transformed:
            result.append(item)
    return result

def square(x):
    return x * x
list1 = [1, 2, 3]
list2 = [2, 3, 4]

difference = get_list_difference(list1, list2, square)
print(difference)

