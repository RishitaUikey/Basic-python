'''Write a Python program to check if the first digit or character of each element in a list is the same.
Original list:
[1234, 122, 1984, 19372, 100]
Check if first digit in each element of the said given list is same or not!
True
Original list:
[1234, 922, 1984, 19372, 100]
Check if first digit in each element of the said given list is same or not!
False
Original list:
['aabc', 'abc', 'ab', 'a']
Check if first character in each element of the said given list is same or not!
True
Original list:
['aabc', 'abc', 'ab', 'ha']
Check if first character in each element of the said given list is same or not!
False'''

def check_first_character_or_digit(lst):
    first_char_or_digit = str(lst[0])[0]
    for element in lst[1:]:
        current_char_or_digit = str(element)[0]
        if current_char_or_digit != first_char_or_digit:
            return False
    return True
original_list1 = [1234, 122, 1984, 19372, 100]
print("Original list:")
print(original_list1)
print("Check if first digit in each element of the given list is the same or not:")
print(check_first_character_or_digit(original_list1))

original_list2 = [1234, 922, 1984, 19372, 100]
print("\nOriginal list:")
print(original_list2)
print("Check if first digit in each element of the given list is the same or not:")
print(check_first_character_or_digit(original_list2))

original_list3 = ['aabc', 'abc', 'ab', 'a']
print("\nOriginal list:")
print(original_list3)
print("Check if first character in each element of the given list is the same or not:")
print(check_first_character_or_digit(original_list3))

original_list4 = ['aabc', 'abc', 'ab', 'ha']
print("\nOriginal list:")
print(original_list4)
print("Check if first character in each element of the given list is the same or not:")
print(check_first_character_or_digit(original_list4))
