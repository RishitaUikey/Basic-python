'''Write a Python program to pack consecutive duplicates of a given list of elements into sublists.
Original list:
[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
After packing consecutive duplicates of the said list elements into sublists:
[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]'''

original_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
packed_list = []

i = 0
while i < len(original_list):
    current = original_list[i]
    sublist = [current]
    j = i + 1
    while j < len(original_list) and original_list[j] == current:
        sublist.append(original_list[j])
        j += 1
    
    packed_list.append(sublist)
    
    i = j


print("After packing consecutive duplicates of the said list elements into sublists:")
print(packed_list)
