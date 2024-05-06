'''Write a  Python program to get every nth element in a given list.
Sample Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[2, 4, 6, 8, 10]
[5, 10]
[6]'''

def get_every_nth_element(lst, n):
    return lst[n - 1::n]

sample_lists = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
]
sample_values = [1, 2, 5, 6]
for lst, n in zip(sample_lists, sample_values):
    print(get_every_nth_element(lst, n))

