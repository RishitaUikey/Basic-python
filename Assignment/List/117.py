'''Write a  Python program to remove all elements from a given list that are present in another list.
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]
Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]'''

def remove_elements(list1, list2):
    return [x for x in list1 if x not in list2]

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]
result = remove_elements(list1, list2)

print("Original lists:")
print("list1:", list1)
print("list2:", list2)
print("Remove all elements from 'list1' present in 'list2':")
print(result)
