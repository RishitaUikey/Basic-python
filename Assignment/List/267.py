'''Write a  Python program to get the cumulative sum of the elements of a given list.
Sample Output:
Original list elements:
[1, 2, 3, 4]
Cumulative sum of the elements of the said list:
[1, 3, 6, 10]
Original list elements:
[-1, -2, -3, 4]
Cumulative sum of the elements of the said list:
[-1, -3, -6, -2]'''

from itertools import accumulate

def cumulative_sum(lst):
    return list(accumulate(lst))

sample_lists = [
    [1, 2, 3, 4],
    [-1, -2, -3, 4]
]

for lst in sample_lists:
    print("Original list elements:")
    print(lst)
    print("Cumulative sum of the elements of the said list:")
    print(cumulative_sum(lst))

