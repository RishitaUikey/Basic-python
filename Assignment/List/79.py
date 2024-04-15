''' Write a Python program to remove the K'th element from a given list, and print the updated list.
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
After removing an element at the kth position of the said list:
[1, 1, 3, 4, 4, 5, 1]'''

original_list = [1, 1, 2, 3, 4, 4, 5, 1]
a = 2
if a < 0 or a >= len(original_list):
    print("Invalid value for k. The list index is out of range.")
else:    
    del original_list[a]
    print("Original list:", original_list)
