'''Write a  Python program to count the number of unique sublists within a given list.
Original list:
[[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
Number of unique lists of the said list:
{(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
Original list:
[['green', 'orange'], ['black'], ['green', 'orange'], ['white']]
Number of unique lists of the said list:
{('green', 'orange'): 2, ('black',): 1, ('white',): 1}'''

from collections import Counter

def count_unique_sublists(lst):
    tuples_lst = [tuple(sublist) for sublist in lst]
    unique_counts = Counter(tuples_lst)
    return unique_counts

lists1 = [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
lists2 = [['green', 'orange'], ['black'], ['green', 'orange'], ['white']]

unique_counts1 = count_unique_sublists(lists1)
unique_counts2 = count_unique_sublists(lists2)

print("Original list:")
print(lists1)
print("Number of unique lists of the said list:")
print(unique_counts1)

print("\nOriginal list:")
print(lists2)
print("Number of unique lists of the said list:")
print(unique_counts2)
