'''Write a  Python program to create a list taking alternate elements from a given list.
Original list:
['red', 'black', 'white', 'green', 'orange']
List with alternate elements from the said list:
['red', 'white', 'orange']
Original list:
[2, 0, 3, 4, 0, 2, 8, 3, 4, 2]
List with alternate elements from the said list:
[2, 3, 0, 8, 4]'''

def alternate_elements(lst):
    return lst[::2]

original_list1 = ['red', 'black', 'white', 'green', 'orange']
original_list2 = [2, 0, 3, 4, 0, 2, 8, 3, 4, 2]

result1 = alternate_elements(original_list1)
result2 = alternate_elements(original_list2)

print("Original list:")
print(original_list1)
print("List with alternate elements from the said list:")
print(result1)
print("Original list:")
print(original_list2)
print("List with alternate elements from the said list:")
print(result2)
