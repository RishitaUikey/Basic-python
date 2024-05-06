'''Write a  Python program to display vertically each element of a given list, list of lists.
Original list:
['a', 'b', 'c', 'd', 'e', 'f']
Display each element vertically of the said list:
a
b
c
d
e
f
Original list:
[[1, 2, 5], [4, 5, 8], [7, 3, 6]]
Display each element vertically of the said list of lists:
1 4 7
2 5 3
5 8 6'''

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
