'''Write a  Python program to convert a given list of strings into a list of lists.
Original list of strings:
['Red', 'Maroon', 'Yellow', 'Olive']
Convert the said list of strings into list of lists:
[['R', 'e', 'd'], ['M', 'a', 'r', 'o', 'o', 'n'], ['Y', 'e', 'l', 'l', 'o', 'w'], ['O', 'l', 'i', 'v', 'e']]'''

original_list = ['Red', 'Maroon', 'Yellow', 'Olive']
list_of_lists = [[char for char in string] for string in original_list]
print("Original list of strings:")
print(original_list)
print("Convert the said list of strings into list of lists:")
print(list_of_lists)
