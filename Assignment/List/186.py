'''Write a  Python program to swap two sublists in a given list.
Original list:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Swap two sublists of the said list:
[0, 6, 7, 8, 9, 3, 4, 5, 1, 2, 10, 11, 12, 13, 14, 15]
Swap two sublists of the said list:
[0, 9, 3, 8, 6, 7, 4, 5, 1, 2, 10, 11, 12, 13, 14, 15]'''

def swap_sublists(lst, start1, end1, start2, end2):
    sublist1 = lst[start1:end1]
    sublist2 = lst[start2:end2]
    lst[start1:end1] = sublist2
    lst[start2:end2] = sublist1
    return lst
original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print("Original list:")
print(original_list)
result = swap_sublists(original_list, 1, 4, 5, 9)
print("Swap two sublists of the said list:")
print(result)
result = swap_sublists(original_list, 1, 5, 5, 9)
print("Swap two sublists of the said list:")
print(result)
