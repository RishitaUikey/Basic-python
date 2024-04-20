'''Write a  Python program to convert a given list of strings and characters to a single list of characters.
Original list:
['red', 'white', 'a', 'b', 'black', 'f']
Convert the said list of strings and characters to a single list of characters:
['r', 'e', 'd', 'w', 'h', 'i', 't', 'e', 'a', 'b', 'b', 'l', 'a', 'c', 'k', 'f']
'''

original_list = ['a', 'b', 'c', 'd', 'e', 'f']
print("Original list:")
print(original_list)
print("Display each element vertically of the said list:")
for item in original_list:
    print(item)
list_of_lists = [[1, 2, 5], [4, 5, 8], [7, 3, 6]]
print("\nOriginal list of lists:")
print(list_of_lists)
print("Display each element vertically of the said list of lists:")
for i in range(len(list_of_lists[0])):
    for lst in list_of_lists:
        print(lst[i], end=" ")
    print()
