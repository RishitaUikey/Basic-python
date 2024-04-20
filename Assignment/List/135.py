''' Write a  Python program to iterate over all pairs of consecutive items in a given list.
Original lists:
[1, 1, 2, 3, 3, 4, 4, 5]
Iterate over all pairs of consecutive items of the said list:
[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]'''

def consecutive_pairs(lst):
    return [(lst[i], lst[i+1]) for i in range(len(lst) - 1)]

original_list = [1, 1, 2, 3, 3, 4, 4, 5]
result = consecutive_pairs(original_list)
print("Iterate over all pairs of consecutive items of the said list:")
print(result)
