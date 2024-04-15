'''Write a Python program to split a given list into two parts where the length of the first part of the list is given.
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
Length of the first part of the list: 3
Splited the said list into two parts:
([1, 1, 2], [3, 4, 4, 5, 1])'''

original_list = [1, 1, 2, 3, 4, 4, 5, 1]
length_first_part = 3
first_part = original_list[:length_first_part]
second_part = original_list[length_first_part:]

print("Length of the first part of the list:", length_first_part)
print("Splited the said list into two parts:", (first_part, second_part))
