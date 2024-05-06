'''Write a  Python program to insert a specified element in a given list after every nth element.
Original list:
[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
Insert 20 in said list after every 4 th element:
[1, 3, 5, 7, 20, 9, 11, 0, 2, 20, 4, 6, 8, 10, 20, 8, 9, 0, 4, 20, 3, 0]
Original list:
['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']
Insert Z in said list after every 3 th element:
['s', 'd', 'f', 'Z', 'j', 's', 'a', 'Z', 'j', 'd', 'f', 'Z', 'd']
'''

def insert_element_after_nth(lst, element, n):
    result = []
    for i, item in enumerate(lst):
        result.append(item)
        if (i + 1) % n == 0:
            result.append(element)
    return result

original_list1 = [1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
element1 = 20
n1 = 4
print("Original list 1:")
print(original_list1)
print("Insert", element1, "in said list after every", n1, "th element:")
print(insert_element_after_nth(original_list1, element1, n1))
original_list2 = ['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']
element2 = 'Z'
n2 = 3
print("\nOriginal list 2:")
print(original_list2)
print("Insert", element2, "in said list after every", n2, "th element:")
print(insert_element_after_nth(original_list2, element2, n2))
