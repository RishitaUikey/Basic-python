'''Write a  Python program to check whether a specified list is sorted or not.
Original list:
[1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
Is the said list is sorted!
True
Original list:
[1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
Is the said list is sorted!
False'''

def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

original_list1 = [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
original_list2 = [1, 2, 4, 6, 8, 10, 12, 14, 16, 17, 15]
print("Original list:")
print(original_list1)
print("Is the said list sorted?")
print(is_sorted(original_list1))
print("\nOriginal list:")
print(original_list2)
print("Is the said list sorted?")
print(is_sorted(original_list2))
