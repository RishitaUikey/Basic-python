'''Write a  Python program to sort a given list of lists by length and value.
Original list:
[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
Sort the list of lists by length and value:
[[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]'''

def sort_by_length_and_value(lst):
    sorted_lst = sorted(lst, key=lambda x: (len(x), x))
    return sorted_lst

original_list = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
sorted_list = sort_by_length_and_value(original_list)

print("Original list:")
print(original_list)
print("Sort the list of lists by length and value:")
print(sorted_list)
