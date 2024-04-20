'''Write a  Python program to shift last element to first position and first element to last position in a given list.
Original list:
[1, 2, 3, 4, 5, 6, 7]
Shift last element to first position and first element to last position of the said list:
[7, 2, 3, 4, 5, 6, 1]
Original list:
['s', 'd', 'f', 'd', 's', 's', 'd', 'f']
Shift last element to first position and first element to last position of the said list:
['f', 'd', 'f', 'd', 's', 's', 'd', 's']'''

def shift_elements(lst):
    return lst[-1:] + lst[1:-1] + lst[:1]

original_list1 = [1, 2, 3, 4, 5, 6, 7]
print("Original list:")
print(original_list1)
print("Shift last element to first position and first element to last position of the said list:")
print(shift_elements(original_list1))
original_list2 = ['s', 'd', 'f', 'd', 's', 's', 'd', 'f']
print("\nOriginal list:")
print(original_list2)
print("Shift last element to first position and first element to last position of the said list:")
print(shift_elements(original_list2))
