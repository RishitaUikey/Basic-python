'''Write a Python program to reverse each list in a given list of lists.
Original list of lists:
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
Reverse each list in the said list of lists:
[[4, 3, 2, 1], [8, 7, 6, 5], [12, 11, 10, 9], [16, 15, 14, 13]]'''

def reverse_lists(list_of_lists):
    return [sublist[::-1] for sublist in list_of_lists]

original_list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
reversed_lists = reverse_lists(original_list)

print("Original list of lists:")
print(original_list)
print("Reverse each list in the said list of lists:")
print(reversed_lists)
