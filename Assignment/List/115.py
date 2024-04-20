'''Write a  Python program to check if the elements of a given list are unique or not.
Original list:
[1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]
Is the said list contains all unique elements!
False
Original list:
[2, 4, 6, 8, 10, 12, 14]
Is the said list contains all unique elements!
True'''

def are_elements_unique(lst):
    return len(lst) == len(set(lst))
original_list1 = [1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]
original_list2 = [2, 4, 6, 8, 10, 12, 14]
result1 = are_elements_unique(original_list1)
result2 = are_elements_unique(original_list2)
print("Original list:")
print(original_list1)
print("Is the said list contains all unique elements!")
print(result1)

print("\nOriginal list:")
print(original_list2)
print("Is the said list contains all unique elements!")
print(result2)
