'''Write a  Python program to find the difference between consecutive numbers in a given list.
Original list:
[1, 1, 3, 4, 4, 5, 6, 7]
Difference between consecutive numbers of the said list:
[0, 2, 1, 0, 1, 1, 1]
Original list:
[4, 5, 8, 9, 6, 10]
Difference between consecutive numbers of the said list:
[1, 3, 1, -3, 4]'''

def consecutive_differences(lst):
    return [lst[i] - lst[i-1] for i in range(1, len(lst))]

original_list1 = [1, 1, 3, 4, 4, 5, 6, 7]
original_list2 = [4, 5, 8, 9, 6, 10]
differences1 = consecutive_differences(original_list1)
differences2 = consecutive_differences(original_list2)
print("Original list:")
print(original_list1)
print("Difference between consecutive numbers of the said list:")
print(differences1)
print("\nOriginal list:")
print(original_list2)
print("Difference between consecutive numbers of the said list:")
print(differences2)
