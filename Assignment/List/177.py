''' Write a  Python program to find common elements in a given list of lists.
Original list:
[[7, 2, 3, 4, 7], [9, 2, 3, 2, 5], [8, 2, 3, 4, 4]]
Common elements of the said list of lists:
[2, 3]
Original list:
[['a', 'b', 'c'], ['b', 'c', 'd'], ['c', 'd', 'e']]
Common elements of the said list of lists:
['c']'''

def find_common_elements(list_of_lists):
    common_elements = set(list_of_lists[0])
    for lst in list_of_lists[1:]:
        common_elements = common_elements.intersection(lst)
    
    return list(common_elements)

list1 = [[7, 2, 3, 4, 7], [9, 2, 3, 2, 5], [8, 2, 3, 4, 4]]
list2 = [['a', 'b', 'c'], ['b', 'c', 'd'], ['c', 'd', 'e']]
print("Original list 1:")
print(list1)
print("Common elements of the said list of lists:")
print(find_common_elements(list1))
print("\nOriginal list 2:")
print(list2)
print("Common elements of the said list of lists:")
print(find_common_elements(list2))
