'''Write a  Python program to calculate the maximum and minimum sum of a sublist in a given list of lists.
Original list:
[[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
Maximum sum of sub list of the said list of lists:
[2, 3, 5, 4]
Minimum sum of sub list of the said list of lists:
[1, 2, 1, 2]'''

def max_min_sum_sublist(list_of_lists):
    max_sum_sublist = None
    min_sum_sublist = None
    max_sum = float('-inf')
    min_sum = float('inf')
    
    for sublist in list_of_lists:
        sublist_sum = sum(sublist)
        if sublist_sum > max_sum:
            max_sum = sublist_sum
            max_sum_sublist = sublist
        if sublist_sum < min_sum:
            min_sum = sublist_sum
            min_sum_sublist = sublist
    
    return max_sum_sublist, min_sum_sublist
original_list = [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
max_sum_sublist, min_sum_sublist = max_min_sum_sublist(original_list)

print("Original list:")
for sublist in original_list:
    print(sublist)
print("Maximum sum of sub list of the said list of lists:")
print(max_sum_sublist)
print("Minimum sum of sub list of the said list of lists:")
print(min_sum_sublist)
