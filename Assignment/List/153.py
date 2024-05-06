'''Write a  Python program to check if a given element occurs at least n times in a list.
Original list:
[0, 1, 3, 5, 0, 3, 4, 5, 0, 8, 0, 3, 6, 0, 3, 1, 1, 0]
Check if 3 occurs at least 4 times in a list:
True
Check if 0 occurs at least 5 times in a list:
True
Check if 8 occurs at least 3 times in a list:
False'''

def check_occurrences(lst, element, min_count):
    return lst.count(element) >= min_count
original_list = [0, 1, 3, 5, 0, 3, 4, 5, 0, 8, 0, 3, 6, 0, 3, 1, 1, 0]
print("Check if 3 occurs at least 4 times in the list:")
print(check_occurrences(original_list, 3, 4))
print("Check if 0 occurs at least 5 times in the list:")
print(check_occurrences(original_list, 0, 5))
print("Check if 8 occurs at least 3 times in the list:")
print(check_occurrences(original_list, 8, 3))
