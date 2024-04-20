'''Write a  Python program to find the common tuples between two given lists.
Original lists:
[('red', 'green'), ('black', 'white'), ('orange', 'pink')]
[('red', 'green'), ('orange', 'pink')]
Common tuples between two said lists
[('orange', 'pink'), ('red', 'green')]
Original lists:
[('red', 'green'), ('orange', 'pink')]
[('red', 'green'), ('black', 'white'), ('orange', 'pink')]
Common tuples between two said lists
[('orange', 'pink'), ('red', 'green')]'''

def find_common_tuples(list1, list2):

    set1 = set(list1)
    set2 = set(list2)
    common = list(set1 & set2)
    return common

list1 = [('red', 'green'), ('black', 'white'), ('orange', 'pink')]
list2 = [('red', 'green'), ('orange', 'pink')]
print("Original lists:")
print(list1)
print(list2)
print("Common tuples between two said lists")
print(find_common_tuples(list1, list2))

list3 = [('red', 'green'), ('orange', 'pink')]
list4 = [('red', 'green'), ('black', 'white'), ('orange', 'pink')]
print("\nOriginal lists:")
print(list3)
print(list4)
print("Common tuples between two said lists")
print(find_common_tuples(list3, list4))
