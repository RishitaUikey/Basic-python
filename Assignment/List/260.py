'''Write a Python program to check if all the elements of a list are included in another given list.
Sample Output:
True
False'''

def all_elements_included(list1, list2):
    return all(elem in list2 for elem in list1)

list1 = [1, 2, 3]
list2 = [1, 2, 3, 4, 5]
list3 = [1, 2, 4]
print(all_elements_included(list1, list2))
print(all_elements_included(list1, list3))


