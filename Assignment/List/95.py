'''Write a  Python program to sort each sublist of strings in a given list of lists.
Original list:
[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
Sort the list of lists by length and value:
[[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]'''

def sort_sublists(lst):
    sorted_sublists = [sorted(sublist) for sublist in lst]
    sorted_lst = sorted(sorted_sublists, key=lambda x: (len(x), x))
    return sorted_lst

original_list = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]

sorted_list = sort_sublists(original_list)

print("Original list:")
print(original_list)
print("Sort the list of lists by length and value:")
print(sorted_list)
